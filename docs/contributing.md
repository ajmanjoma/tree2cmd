# 🤝 Contributing Guide – tree2cmd

Thank you for your interest in contributing to **tree2cmd**!
This project welcomes:

* Bug fixes
* New features
* Documentation updates
* Test improvements
* Feedback or suggestions

This guide explains how to set up the project, run tests, and submit changes.

---

# 📦 1. Project Setup

Clone the repository:

```bash
git clone https://github.com/ajmanjoma/tree2cmd.git
cd tree2cmd
```

Install in editable mode:

```bash
pip install -e .
```

Install development requirements (if any):

```bash
pip install -r requirements.txt
```

---

# 🧪 2. Running Tests

The test suite uses Python’s built-in `unittest`.

Run all tests:

```bash
python -m unittest discover -v
```

You should see output like:

```
Ran 8 tests in 0.01s

OK
```

---

# 🛠 3. Project Structure

```
tree2cmd/
│
├── tree2cmd/          # Library code
│   ├── cli.py
│   ├── parser.py
│   └── utils.py
│
├── tests/             # Unit tests
│   ├── test_cli.py
│   ├── test_parser.py
│   └── test_integration.py
│
├── docs/              # Documentation
│
├── examples/          # Example struct files
│
├── scripts/           # Build & automation
│
└── pyproject.toml
```

---

# 🧩 4. Coding Style

Please follow these guidelines:

* Use clear, descriptive variable names
* Keep functions small and focused
* Avoid unnecessary complexity
* Add comments where needed
* Preserve existing formatting
* Do not break API compatibility without discussion

---

# 🔍 5. Adding New Features

Before adding a new feature:

1. Open an **Issue** on GitHub
2. Describe your idea
3. Wait for approval or discussion
4. Submit a Pull Request once approved

---

# 🧪 6. Writing Tests

Every new feature **must** include tests.

Add tests in:

```
tests/
```

Example test template:

```python
import unittest
from tree2cmd.parser import parse_tree

class TestParser(unittest.TestCase):
    def test_simple_tree(self):
        text = "App/\n  main.py"
        result = parse_tree(text)
        self.assertEqual(result[0], ("App", True))
```

---

# 📘 7. Updating Documentation

All documentation lives in:

```
docs/
```

If you add a new CLI option or parser behavior:

* Update `docs/cli.md`
* Update `docs/parser.md`
* Update `README.md`

---

# 📤 8. Submitting a Pull Request

Once you make your changes:

```bash
git checkout -b feature/my-feature
git add .
git commit -m "Add new feature"
git push origin feature/my-feature
```

Then submit a Pull Request on GitHub.

**Your PR should include:**

* A clear description
* Why the change is needed
* Before/after examples (if applicable)
* Passing tests

---

# 📄 9. Code of Conduct

* Be respectful
* No rude language
* Assume positive intent
* Help other contributors
* Keep discussions technical

---

# 🛡️ 10. License

By contributing, you agree that your contributions are licensed under the project’s MIT License.

---

# 🌟 Thank You

Your contributions make **tree2cmd** better for everyone!
Feel free to reach out or open a discussion.
