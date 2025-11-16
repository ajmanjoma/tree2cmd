
# 📚 API Documentation – tree2cmd

`tree2cmd` exposes a small but powerful internal API.
These functions allow you to use the parser programmatically or embed it into other tools.

This document explains all public functions inside:

* `tree2cmd.parser`
* `tree2cmd.cli`
* `tree2cmd.utils`

---

# 🧩 MODULE: `tree2cmd.parser`

The parser module converts raw text (from struct.txt) into structured data.

---

## ### 1. `clean_name(raw: str) -> str`

**Description:**
Clean a raw line by removing tree symbols while preserving real names, spaces, and emojis.

**Example:**

```python
clean_name("  ├── src/")   # → "src"
clean_name("📦 App/")      # → "📦 App"
```

---

## ### 2. `detect_indent(raw: str, indent_width: int) -> int`

**Description:**
Calculate indentation level based purely on leading spaces.

**Example:**

```python
detect_indent("    main.py", 2)  # → 2
detect_indent("  file", 2)       # → 1
```

---

## ### 3. `parse_tree(text: str, indent_width: int = 2) -> List[(path, is_dir)]`

**Description:**
The core parser function.
Turns text tree into a normalized list of:

```
(path, is_directory)
```

**Example:**

```python
parse_tree("""
App/
  backend/
    api.py
""")
```

Returns:

```python
[
  ("App", True),
  ("App/backend", True),
  ("App/backend/api.py", False)
]
```

---

# 🧩 MODULE: `tree2cmd.cli`

The CLI module provides the conversion to shell commands.

---

## ### 4. `convert_tree_to_commands(tree_text: str, **options) -> List[str]`

**Description:**
Convert parsed tree text into executable `mkdir` and `touch` commands.

**Arguments:**

| Parameter      | Description                                  |
| -------------- | -------------------------------------------- |
| `tree_text`    | raw text input                               |
| `dry_run`      | do not execute commands (default)            |
| `verbose`      | print detailed logs                          |
| `save_script`  | write commands to a `.sh` file               |
| `strict`       | stop on error                                |
| `indent_width` | number of spaces per indentation (default 2) |

**Example:**

```python
commands = convert_tree_to_commands("""
Project/
  src/
    main.py
""")
```

Returns:

```
[
  'mkdir -p "Project/"',
  'mkdir -p "Project/src/"',
  'touch "Project/src/main.py"'
]
```

---

## ### 5. `main()`

**Description:**
Entry point for CLI command:

```bash
tree2cmd
```

Not intended for direct imports.

---

# 🧩 MODULE: `tree2cmd.utils`

Utility helpers used internally and exposed for advanced use cases.

---

## ### 6. `tree_from_shell_commands(commands: List[str]) -> str`

**Description:**
Reconstruct a directory tree from a list of shell commands.

**Useful for:**

* verifying a generated struct
* testing
* displaying a clean tree after parsing

**Example:**

```python
tree_from_shell_commands([
  'mkdir -p "Project/"',
  'mkdir -p "Project/src/"',
  'touch "Project/src/main.py"'
])
```

**Output:**

```
Project
├── src
│   └── main.py

1 directories, 1 files
```

---

# 🧪 Example: Using API Directly in Python

```python
from tree2cmd.parser import parse_tree
from tree2cmd.cli import convert_tree_to_commands

text = """
App/
  backend/
    api.py
"""

# Parse tree
paths = parse_tree(text)

# Convert to commands
commands = convert_tree_to_commands(text)

for cmd in commands:
    print(cmd)
```

---

# 🔒 Stability of API

These functions are **public and stable**.
Future releases may add new helper functions but will not break existing API without clear version changes.

---

# 📌 See Also

* **[Parser Internals](parser.md)**
* **[Usage Guide](usage.md)**
* **[CLI Reference](cli.md)**

