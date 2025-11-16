# ❓ **FAQ – tree2cmd**

This FAQ covers common questions and issues when using `tree2cmd`.

---

# 🔹 **1. What is tree2cmd?**

`tree2cmd` converts a text-based folder structure (like `struct.txt`) into actual directories and files using simple shell commands:

* `mkdir -p`
* `touch`

Useful for project scaffolding, tutorials, and automation.

---

# 🔹 **2. Does tree2cmd modify my existing files?**

No.
It only **creates** folders and files.

It never deletes or overwrites anything.

---

# 🔹 **3. Does tree2cmd support emojis and Unicode folder names?**

Yes.
The parser preserves:

* emojis (📦, 📁, etc.)
* spaces
* accented characters
* unicode text
* RTL characters

Example:

```
📦 App/
  🔧 config.yaml
```

---

# 🔹 **4. Why does my emoji folder become `📦App` without a space?**

This was a bug in earlier versions due to a flawed cleaning method.
The new parser **keeps all spaces and emojis correctly**.

If you still see this issue, upgrade to the newest release.

---

# 🔹 **5. What indentation styles are supported?**

tree2cmd supports:

* 2-space indentation
* 4-space indentation
* consistent indentation (recommended)

If your file uses 4-space indents:

```bash
tree2cmd struct.txt --indent-width 4
```

---

# 🔹 **6. Why is a name sometimes detected as a folder automatically?**

Folders are detected by:

1. Ending with `/`
2. Or having deeper indentation on the next line

Examples:

```
src/
```

→ always folder

```
src
  main.py
```

→ folder even without trailing `/`

---

# 🔹 **7. Does tree2cmd work on Windows?**

Partially.

tree2cmd **generates bash-compatible commands**, not Windows CMD or PowerShell commands.

On Windows, use:

* Git Bash
* WSL (Windows Subsystem for Linux)
* Cygwin

---

# 🔹 **8. Can I convert commands back into a tree?**

Yes.

```bash
tree2cmd struct.txt --tree
```

This reconstructs a clean folder tree from generated commands.

---

# 🔹 **9. Why do I get “Unexpected indentation level” warnings?**

It means your struct file has inconsistent indentation:

```
Project/
      src/
  README.md
```

Fix: use consistent 2- or 4-space indentation.

---

# 🔹 **10. Can tree2cmd save a .sh script?**

Yes:

```bash
tree2cmd struct.txt --save setup.sh
```

Generates an executable script.

---

# 🔹 **11. Does it overwrite existing files?**

No.
tree2cmd does not touch existing content.

---

# 🔹 **12. How do I use tree2cmd in a Python script?**

Example:

```python
from tree2cmd.cli import convert_tree_to_commands

commands = convert_tree_to_commands("""
Project/
  src/
    main.py
""")

print(commands)
```

---

# 🔹 **13. Can I generate multiple project templates?**

Yes — create multiple `struct.txt` files inside the `examples/` folder:

```
examples/python_project.txt
examples/react_template.txt
examples/django_basic.txt
```

---

# 🔹 **14. Does tree2cmd require any dependencies?**

No.
It is a **pure Python** tool with **zero external dependencies**.

---

# 🔹 **15. Where can I report a bug or request a feature?**

You can open an issue or pull request at:

👉 [https://github.com/ajmanjoma/tree2cmd](https://github.com/ajmanjoma/tree2cmd)

---

# 🔗 Next Steps

* **[CLI Reference](cli.md)**
* **[Usage Guide](usage.md)**
* **[Parser Internals](parser.md)**
* **[Contributing Guide](contributing.md)**

