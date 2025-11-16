# 🖥️ **CLI Reference – tree2cmd**

The `tree2cmd` command-line interface converts a text-based directory tree (`struct.txt`) into shell commands (`mkdir -p` and `touch`), or directly creates folders and files.

This page documents every available CLI option with examples.

---

# 📦 **Basic Syntax**

```
tree2cmd <input_file> [options]
```

Or read from stdin:

```
tree2cmd --stdin
```

---

# 📁 **Input Options**

### **`<input_file>`**

Path to a text file containing the folder structure.

Example:

```bash
tree2cmd struct.txt
```

### **`--stdin`**

Reads structure input from standard input.

Example:

```bash
cat struct.txt | tree2cmd --stdin
```

---

# ⚙️ **Execution Options**

### **`--run`**

Executes the generated commands directly, creating folders & files.

```bash
tree2cmd struct.txt --run
```

### **Dry-run (default)**

If `--run` is not used, commands are printed but not executed.

```bash
tree2cmd struct.txt
```

---

# 📜 **Script Output**

### **`--save <file.sh>`**

Saves generated commands into a shell script.

```bash
tree2cmd struct.txt --save struct.sh
```

---

# 🧭 **Output Transformation Options**

### **`--tree`**

Displays a reconstructed tree (based on generated commands) instead of command output.

```bash
tree2cmd struct.txt --tree
```

Example output:

```
Project
├── src
│   └── main.py
└── README.md

1 directories, 2 files
```

---

# 🔊 **Logging Options**

### **`--no-verbose`**

Suppresses informational output.
Only final commands are shown.

```bash
tree2cmd struct.txt --no-verbose
```

### Verbose mode (default)

Shows logging information like created directories and files.

---

# 🔐 **Strict Mode**

### **`--strict`**

Stop immediately on any error (e.g., invalid file path).

```bash
tree2cmd struct.txt --strict
```

---

# 🔢 **Indentation Options**

### **`--indent-width <N>`**

Specify indentation width in spaces.
Default: **2**

Example (for 4-space indents):

```bash
tree2cmd struct.txt --indent-width 4
```

---

# 🔖 **Version**

### **`--version`**

Show tree2cmd version and exit.

```bash
tree2cmd --version
```

---

# 📚 **Full Option Summary**

| Option             | Description                       |
| ------------------ | --------------------------------- |
| `--stdin`          | Read input from standard input    |
| `--run`            | Execute mkdir/touch commands      |
| `--save <file>`    | Save commands to a shell script   |
| `--strict`         | Stop on first error               |
| `--no-verbose`     | Suppress logging                  |
| `--tree`           | Print reconstructed tree          |
| `--indent-width N` | Set indentation width (default 2) |
| `--version`        | Print version info and exit       |

---

# 🧪 Example Workflows

### **1. Generate commands and preview**

```bash
tree2cmd struct.txt
```

### **2. Create folders & files instantly**

```bash
tree2cmd struct.txt --run
```

### **3. Save a reusable script**

```bash
tree2cmd struct.txt --save setup.sh
```

### **4. Pipeline usage**

```bash
printf "App/\n  main.py" | tree2cmd --stdin --run
```

---


* **[Usage Guide](usage.md)**
* **[Parser Internals](parser.md)**
* **[API Documentation](api.md)**

---

