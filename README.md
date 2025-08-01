# tree2cmd

Convert tree-style directory text into shell commands (`mkdir` and `touch`).

---

## Installation

```bash
pip install tree2cmd
```

---

## Features

- Parse tree-like folder structures from text files or standard input
- Support emojis and common tree characters (`├──`, `│`, `└──`, etc.)
- Heuristically detect folders vs. files (folder if ends with `/` or indentation implies children)
- Generate safe shell commands: `mkdir -p` for directories, `touch` for files
- Optionally execute commands or save them into a shell script
- Handle indentation-based nesting with configurable indent width (default: 2 spaces)
- Properly escape special shell characters inside quotes
- Lightweight and dependency-free, compatible with Python 3.7+

---

## Usage

Run `tree2cmd` from the command line:

- **Dry-run (print commands)**:

  ```bash
  tree2cmd <input_file>
  ```

- **Execute commands to create files and folders**:

  ```bash
  tree2cmd <input_file> --run
  ```

- **Save generated commands to a shell script**:

  ```bash
  tree2cmd <input_file> --save <script.sh>
  ```

- **Read input from standard input**:

  ```bash
  cat structure.txt | tree2cmd --stdin
  ```

Adjust indentation width with `--indent-width` if your input uses non-standard spacing.

---

## FAQ & Troubleshooting

- **Does this work on Windows CMD or PowerShell?**  
  Generated commands target bash shells (Linux/macOS/WSL). Windows native shells are not supported.

- **Special characters cause errors?**  
  Input paths are quoted and escaped, but ensure input format is clean and consistent.

- **Indentation detection issues?**  
  Verify your input uses consistent indentation and set `--indent-width` accordingly.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Clone it locally
3. Run tests:

   ```bash
   python -m unittest discover tests
   ```
4. Implement your changes and commit
5. Push and open a Pull Request

Ideas for future enhancements: Windows shell support, custom file templates, GUI frontend.

---

## Disclaimer

Experimental project — use at your own risk. Always review generated commands before execution. No liability for data loss.

---

## Author

AnJoMa — [antonyjosephmathew1@gmail.com](mailto:antonyjosephmathew1@gmail.com)  
GitHub: [https://github.com/ajmanjoma/tree2cmd](https://github.com/ajmanjoma/tree2cmd)

---