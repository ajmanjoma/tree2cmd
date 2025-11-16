# 🧩 Parser Internals – tree2cmd

This document explains how the internal parser of `tree2cmd` converts a text-based directory structure into a structured list of directories and files.

The parser converts *visual* folder trees (with indentation, symbols, or emojis) into machine-readable paths.

---

# 📚 Overview

The parser is responsible for turning this:

```
Project/
  src/
    main.py
  README.md
```

Into this:

```python
[
  ("Project", True),
  ("Project/src", True),
  ("Project/src/main.py", False),
  ("Project/README.md", False)
]
```

The CLI later turns these into `mkdir` and `touch` commands.

---

# 🛠 Parser Components

The parser is divided into three core functions:

1. **`clean_name(raw)`**
2. **`detect_indent(raw, indent_width)`**
3. **`parse_tree(text, indent_width)`** ← main function

These functions live inside:

```
tree2cmd/parser.py
```

---

# 1️⃣ `clean_name(raw: str) -> str`

### Purpose:

Removes *visual* tree characters but **preserves real names**, including:

* spaces
* unicode characters
* emojis
* non-ASCII text

### Example input:

```
"  ├── src/"
```

### Output:

```
"src"
```

### Why important?

Your original implementation removed spaces, turning:

```
📦 App
```

into:

```
📦App   ❌ WRONG
```

The cleaned parser **preserves spaces correctly**.

---

# 2️⃣ `detect_indent(raw: str, indent_width: int) -> int`

### Purpose:

Detect the indentation level *purely from leading spaces*.

### Example:

```
"    main.py"   → indent level = 2 (if indent_width=2)
```

This avoids all issues with:

* emojis
* symbols (`├─`, `│`)
* inconsistent spacing
* Unicode characters

### Why important?

Your previous version incorrectly replaced symbols with spaces, causing indentation drift.

---

# 3️⃣ `parse_tree(text: str, indent_width: int = 2) -> List[(path, is_dir)]`

This is the **core parser**.

### It performs:

#### ✔ Parse lines

Skips empty or blank lines.

#### ✔ Compute indentation level per line

Using `detect_indent`.

#### ✔ Clean names

Using `clean_name`.

#### ✔ Determine full path

Using a stack of parent directories.

#### ✔ Infer folder vs file

Rules:

1. Ends with `/` → folder
2. Next line has deeper indent → folder
3. Otherwise → file

#### ✔ Store results as tuples

Example:

```
("Project/src", True)
```

---

# 📐 How the Stack Works (Directory Depth)

Example:

```
Project/
  src/
    main.py
```

### Step 1:

```
Project  (indent=0)
stack = ["Project"]
```

### Step 2:

```
src  (indent=1)
stack = ["Project", "src"]
```

### Step 3:

```
main.py (indent=2)
stack = ["Project", "src"]
```

Full path = `"Project/src/main.py"`

---

# 🧪 Example Parsing Output

For this tree:

```
App/
  backend/
    api.py
  frontend/
    ui.js
```

Parser output:

```python
[
  ("App", True),
  ("App/backend", True),
  ("App/backend/api.py", False),
  ("App/frontend", True),
  ("App/frontend/ui.js", False)
]
```

---

# 🛑 Why the parser is in `parser.py` and not `cli.py`

Industry best practices:

* `cli.py` → only command-line interface
* `parser.py` → core logic
* `utils.py` → reusable helpers

This separation improves:

* testability
* reliability
* readability
* maintainability

Your previous parser inside cli.py caused bugs because multiple concerns were mixed.

---

# 🧱 Parser Workflow Diagram

```
struct.txt
    ↓
read lines
    ↓
detect indent
    ↓
clean names
    ↓
folder/file detection
    ↓
build full paths
    ↓
list of (path, is_dir)
```

---

# 🧠 Known Limitations

These are intentional design choices:

* Windows CMD paths are not supported
* No automatic detection of tabs mixed with spaces
* Indentation must remain consistent
* Multi-root documents are not yet supported

These may be improved in future releases.

---

# 🚀 Next Steps

* **[CLI Reference](cli.md)**
* **[Usage Guide](usage.md)**
* **[API Documentation](api.md)**

---

