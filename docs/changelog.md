
# 📝 **Changelog – tree2cmd**

This document tracks all notable changes to **tree2cmd**.
The project follows **semantic versioning (SEMVER)**:

```
MAJOR.MINOR.PATCH
```

---

# 📌 **Version History**

---

## 🟢 **0.4.2 – Latest Release**

### ✨ Added

* Fully stable parser with improved whitespace and indent detection
* Cleaner CLI output with color and emoji-safe text handling
* Improved command normalization (`mkdir` / `touch`)
* Added automatic versioning workflows (`bump`, `publish`, `python_tests`)
* New GitHub Action badges and CI/CD workflow consistency
* Added filtering/log extraction scripts

### 🛠 Fixed

* Fixed incorrect directory stack behavior
* Fixed missing parent directory creation in deeper nesting
* Fixed unicode/emoji spacing stripping
* Fixed duplicate tag pushes breaking PyPI deploy workflow
* Resolved GitHub workflow YAML syntax errors

### 🔧 Improved

* Code thoroughly formatted using **Black**
* Updated test suite for Python `3.8 → 3.12`
* More robust path resolution logic
* Better error messaging in CLI

---

## 🟢 **0.4.1**

### ✨ Added

* Improved PyPI metadata
* Internal cleanup after tag collision issues
* More stable wheel + sdist build

### 🛠 Fixed

* Fix GitHub push-protection token leak false positives
* Fixed incorrect bump2version message format

---

## 🟢 **0.4.0**

### ✨ Added

* Major parser rewrite for consistency & correctness
* Restored full Unicode support (emoji, accented chars)
* Better CLI UX with structured messages

### 🛠 Fixed

* "File already exists" error due to reused build artifacts
* Many indentation & tree-symbol parsing issues

---

## 🟢 **0.2.4 → 0.2.5 (Pre-Rewrite Stabilization)**

### ✨ Added

* Added basic CI cleanup scripts
* Started introducing automated workflows

### 🛠 Fixed

* Multiple formatting issues detected by Black
* Early CLI inconsistencies

---

## 🟢 **0.2.1 (Original Public Release)**

### ✨ Added

* Basic parser implementation
* CLI improvements
* Initial documentation (`usage`, `cli`, `parser`, etc.)
* `examples/` and `scripts/` directories

### 🛠 Fixed

* Incorrect indentation logic
* Emoji spacing bug (`📦 App` → `📦App`)
* Incorrect folder/file detection
* Broken nested directory logic

---

## 🟢 **0.1.2**

### ✨ Added

* Added stdin support
* Debug log support

### 🛠 Fixed

* Minor normalization bugs

---

## 🟢 **0.1.1**

### ✨ Added

* Basic CLI
* First tree parser heuristic

---

## 🟢 **0.1.0 – First Release**

### ✨ Added

* Prototype “tree-to-commands” engine
* Support for Unicode tree symbols
* Minimal indentation detection
* Basic mkdir/touch generation

---

# 🚀 **Upcoming Roadmap (0.5.x / 1.0.x)**

### Planned Features

* Windows PowerShell command output
* User-configurable file templates
* Ignorable nodes (`.treeignore`)
* Multi-root struct-file support
* YAML/JSON export support
* Interactive web version of `tree2cmd`

---

# 🔗 **See Also**

* **CLI Reference** – `cli.md`
* **Parser Internals** – `parser.md`
* **Usage Guide** – `usage.md`
* **Contribution Guide** – `contributing.md`


