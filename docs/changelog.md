# 📝 **Changelog – tree2cmd**

This document tracks all notable changes to **tree2cmd**.
The project follows **semantic versioning (SEMVER)**:

```
MAJOR.MINOR.PATCH
```

---

# 📌 **Version History**

---

## 🟢 **0.1.4 – (Current Release)**

**Status:** *In development*

### ✨ Added

* New `parser.py` module with clean, stable parser
* New industry-standard project structure
* Full documentation system under `docs/`
* Added `usage.md`, `cli.md`, `parser.md`, `api.md`, `faq.md`, `contributing.md`, `changelog.md`
* Added `examples/` folder with struct files
* Added `scripts/` folder for automated builds
* Added integration test layout
* Emoji and Unicode folder name handling
* Proper folder/file detection
* Consistent indentation parsing
* Improved CLI logging
* Clean path normalization
* Deduplicated mkdir/touch commands
* New `tree` mode to visualize output commands

### 🛠 Fixed

* Incorrect indent detection in older versions
* Emoji spacing bug (`📦 App` became `📦App`)
* Missing parent folder creation
* Inconsistent folder detection
* Broken stack logic for nested directories
* Tree symbols removing valid characters
* Incorrect behavior for inconsistent indentation
* Duplicate directory creation

---

## 🟢 **0.1.3**

### ✨ Added

* Initial PyPI-ready formatting
* Basic parser (early version)
* Handling of tree characters
* CLI improvements
* Basic tests

### ⚠️ Known Issues (fixed in 0.1.4)

* Incorrect indentation handling
* Emoji spacing issues
* Folder/file misclassification
* Incorrect path joining
* Deeply nested structures fail

---

## 🟢 **0.1.2**

### ✨ Added

* Added stdin support
* Basic debug logs
* Early folder parsing

### 🛠 Fixed

* Some minor normalization bugs

---

## 🟢 **0.1.1**

### ✨ Added

* Initial code upload
* Basic CLI
* folder detection heuristics

---

## 🟢 **0.1.0 – First Release**

### ✨ Added

* Basic implementation of tree-to-commands
* Support for visual tree symbols
* Minimal indentation detection
* mkdir/touch generation

---

# 🚀 **Upcoming Roadmap**

### **Planned for 0.2.x**

* Windows PowerShell support
* Custom file templates
* Ability to ignore certain nodes
* Support for multiple roots in one struct file
* YAML/JSON output mode

---

# 🔗 See Also

* **[CLI Reference](cli.md)**
* **[Parser Internals](parser.md)**
* **[Usage Guide](usage.md)**
* **[Contribution Guide](contributing.md)**
