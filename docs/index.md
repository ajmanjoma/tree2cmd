
# 📘 tree2cmd Documentation

Convert text-based directory trees (`struct.txt`) into real folders and files.

---

## ⭐ Overview

`tree2cmd` is a lightweight command-line tool that converts a text description of a folder structure into actual directories and files using:

* `mkdir -p`
* `touch`

It is designed for:

* Rapid project scaffolding
* Teaching folder structures
* Testing directory layouts
* Automating setup scripts
* Generating reproducible project templates

---

## 🚀 Quick Start

### 1. Create a `struct.txt` file:

```
Project/
  src/
    main.py
  README.md
```

### 2. Run tree2cmd:

```bash
tree2cmd struct.txt
```

### Output (dry run):

```
mkdir -p "Project/"
mkdir -p "Project/src/"
touch "Project/src/main.py"
touch "Project/README.md"
```

### 3. Create actual directories & files:

```bash
tree2cmd struct.txt --run
```

---

## 📂 Example Project Structure

```
my_app/
  config/
    settings.json
  app/
    server.py
  tests/
    test_main.py
```

Run:

```bash
tree2cmd my_tree.txt --run
```

---

## 🔧 Key Features

* Supports tree-style text, indentation, and Unicode characters
* Handles `├──`, `│`, `└──`, emojis, and ASCII symbols
* Detects folders automatically
* Saves commands to `.sh` scripts
* Works with `stdin`, files, and multiple indentation styles
* No dependencies, pure Python

---

## 📑 Documentation Index

* **[Usage Guide](usage.md)** — full CLI examples
* **[CLI Reference](cli.md)** — all flags & commands
* **[Parser Internals](parser.md)** — how the tree parser works
* **[API Docs](api.md)** — functions available for developers
* **[FAQ](faq.md)** — common issues & solutions
* **[Contributing Guide](contributing.md)** — how to improve the project
* **[Changelog](changelog.md)** — version history

---

## 🧩 When Should You Use tree2cmd?

Use it when you want to:

✔ Quickly bootstrap a project
✔ Share a structure example with your team
✔ Convert documentation folder trees into real directories
✔ Produce consistent setups across teams
✔ Create reproducible examples in tutorials

---

## ❤️ Open Source

tree2cmd is open-source and welcomes contributions.
Submit improvements, new features, or bug fixes anytime.
