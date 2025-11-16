# tree2cmd/parser.py

import re
import unicodedata
from typing import List, Tuple


def is_ascii_tree(text: str) -> bool:
    return any(ch in text for ch in ("├", "└", "│"))


def _count_prefix_groups(prefix: str) -> int:
    """
    Count groups that represent one visual level in ASCII tree:
    - either "│   " (pipe + three spaces)
    - or exactly 4 spaces "    "
    We count non-overlapping occurrences from left to right.
    """
    if not prefix:
        return 0
    i = 0
    count = 0
    L = len(prefix)
    while i + 4 <= L:
        chunk = prefix[i : i + 4]
        if chunk == "│   " or chunk == "    ":
            count += 1
            i += 4
        else:
            # skip single char if not a group to try next alignment
            i += 1
    return count


def ascii_to_struct(text: str, indent_width: int = 2) -> str:
    """
    Convert an ASCII-drawn tree into indentation-based struct text.
    Each visual level becomes indent_width spaces.
    """
    out_lines: List[str] = []
    for raw in text.splitlines():
        if not raw.strip():
            continue

        # find first connector char (├ or └). If none, treat as top-level line.
        m = re.search(r"[├└]", raw)
        if m:
            pos = m.start()
            prefix = raw[:pos]
            # Count visual groups in prefix (│   or 4 spaces)
            groups = _count_prefix_groups(prefix)
            # depth is groups + 1 because connector denotes one more level
            depth = groups + 1
            # slice tail starting at connector
            tail = raw[pos:]
            # remove leading connector patterns like '├── ' or '└── ' if present
            tail = re.sub(r"^[├└]\s*──\s*", "", tail)
            # also remove any remaining leading connectors/spaces
            tail = re.sub(r"^[\s│]+", "", tail)
            name = tail.strip()
        else:
            # no connector char: assume a structural/top-level line already
            # but may have leading spaces — treat leading spaces as indent groups (4 spaces)
            leading_ws = re.match(r"^([ \t]*)", raw).group(1)
            groups = _count_prefix_groups(leading_ws)
            depth = groups
            name = raw.strip()

        struct_line = (" " * (depth * indent_width)) + name
        out_lines.append(struct_line)

    return "\n".join(out_lines)


def clean_name(raw: str) -> str:
    """
    Remove any leading tree-drawing characters and return the pure node name.
    Works with both ASCII and struct-style input lines.
    """
    s = raw.rstrip()

    # Remove common unicode tree glyphs and surrounding spaces at start
    s = re.sub(r"^[\s│├└┌─┐┬┴┼━┃╭╰╯╮\u2500-\u257F]*", "", s)

    # Remove ASCII connectors like '├──', '└──', '|--', '+--', '--', '|  '
    s = re.sub(r"^(?:[|\+\-`*>•●○\s]*)?(?:├──|└──|[|\+\-]{1,3})\s*", "", s)

    # Normalize and strip remaining leading/trailing whitespace
    s = unicodedata.normalize("NFKC", s).strip()

    # Remove trailing slash if present (we track directories via raw line anyway)
    return s.rstrip("/")


def detect_indent(raw: str, indent_width: int = 2) -> int:
    """
    Count indentation levels in struct-style lines (after ascii_to_struct).
    Tabs are expanded to indent_width spaces.
    """
    leading = re.match(r"^([ \t]*)", raw).group(1)
    expanded = leading.replace("\t", " " * indent_width)
    return len(expanded) // indent_width


def parse_tree(text: str, indent_width: int = 2) -> List[Tuple[str, bool]]:
    """
    Parse input text (ASCII or struct) and return list of (path, is_dir).
    """
    if not text:
        return []

    if is_ascii_tree(text):
        text = ascii_to_struct(text, indent_width=indent_width)

    lines = [ln for ln in text.splitlines() if ln.strip()]
    results: List[Tuple[str, bool]] = []
    stack: List[str] = []

    for idx, raw in enumerate(lines):
        # compute indent from raw (struct-style now)
        indent = detect_indent(raw, indent_width=indent_width)
        # compute name (without leading connectors/spaces)
        name = clean_name(raw)
        if not name:
            continue

        # peek next line to infer directory when ambiguous
        next_line = lines[idx + 1] if idx + 1 < len(lines) else ""

        # adjust stack to current depth
        while len(stack) > indent:
            stack.pop()

        # determine if directory
        if raw.strip().endswith("/"):
            is_dir = True
        elif "." in name:
            is_dir = False
        else:
            # If next line is deeper -> this is a directory
            is_dir = detect_indent(next_line, indent_width=indent_width) > indent

        # build full path using current stack
        full_path = "/".join(stack + [name])
        results.append((full_path, is_dir))

        if is_dir:
            stack.append(name)

    return results
