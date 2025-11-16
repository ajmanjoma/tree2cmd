
# 📘 Usage Guide – tree2cmd

This guide shows how to use `tree2cmd` with real-world examples.
tree2cmd converts a text-based directory structure (`struct.txt`) into real files and folders.

---

# 📄 1. Basic Usage

### Create a structure file:

**struct.txt**

```
Project/
  src/
    main.py
  README.md
```

### Preview the commands (dry run):

```bash
tree2cmd struct.txt
```

### Output:

```
mkdir -p "Project/"
mkdir -p "Project/src/"
touch "Project/src/main.py"
touch "Project/README.md"
```

### Create actual folders & files:

```bash
tree2cmd struct.txt --run
```

---

# 📥 2. Read Input from Standard Input

You can pipe text directly:

```bash
cat struct.txt | tree2cmd --stdin
```

or type manually:

```bash
printf "App/\n  main.py" | tree2cmd --stdin
```

---

# 📝 3. Save Output to a Shell Script

To generate a reusable `.sh` file:

```bash
tree2cmd struct.txt --save struct.sh
```

It creates:

```sh
#!/bin/sh

mkdir -p "Project/"
mkdir -p "Project/src/"
touch "Project/src/main.py"
touch "Project/README.md"
```

---

# 📂 4. Example: Nested Folders

```
API/
  v1/
    users.py
    models.py
  v2/
    billing.py
```

Run:

```bash
tree2cmd struct.txt --run
```

Resulting structure:

```
API/
  v1/users.py
  v1/models.py
  v2/billing.py
```

---

# 🔧 5. Using Indentation Width

Default indentation = **2 spaces**.
If your file uses 4-space indents:

```bash
tree2cmd struct.txt --indent-width 4
```

---

# 🔍 6. View Tree From Generated Commands

tree2cmd can reconstruct a folder tree from the generated command list:

```bash
tree2cmd struct.txt --tree
```

Output:

```
Project
├── src
│   └── main.py
└── README.md

1 directories, 2 files
```

---

# 🎛 7. CLI Options Summary

| Option             | Description                       |
| ------------------ | --------------------------------- |
| `--run`            | Execute generated commands        |
| `--stdin`          | Read input from standard input    |
| `--save FILE`      | Save commands to a script         |
| `--strict`         | Stop execution on errors          |
| `--indent-width N` | Set indentation level (default 2) |
| `--tree`           | Print tree instead of commands    |
| `--no-verbose`     | Suppress logs                     |
| `--version`        | Show tool version                 |

---

# 💡 8. Tips & Best Practices

* Always preview the structure with a **dry run** before using `--run`.
* Store reusable tree files in `examples/struct.txt`.
* Good for initializing boilerplate folders (React, Django, ML projects, etc).
* Works well inside Makefiles and setup scripts.

---

* **[CLI Reference](cli.md)**
* **[Parser Internals](parser.md)**
* **[Full Project Overview](index.md)**

