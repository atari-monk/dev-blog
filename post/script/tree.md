# Directory Tree CLI Tool

A small Python CLI utility to print a directory tree, with support for:

- Ignoring files and folders via `config.json`
- Limiting tree depth
- Copying output to the clipboard
- Displaying the active ignore configuration

---

## Features

- 📁 Pretty tree output using `├──` / `└──` connectors
- 🚫 Ignore specific folders and files
- 📏 Optional maximum depth
- 📋 Copy tree output directly to clipboard
- ⚙️ Configurable via `config.json`

---

## Requirements

- Python 3.8+
- `pyperclip`

Install dependencies:

```bash
pip install pyperclip
````

---

## Installation

Save the script as, for example:

```bash
tree.py
```

(Optional) Make it executable on Unix systems:

```bash
chmod +x tree.py
```

---

## Usage

```bash
python tree.py [path] [options]
```

If no path is provided, the current directory (`.`) is used.

---

## Options

| Flag                  | Description                                  |
| --------------------- | -------------------------------------------- |
| `-l`, `--level <n>`   | Maximum directory depth                      |
| `-c`, `--clipboard`   | Copy output to clipboard instead of printing |
| `-s`, `--show-ignore` | Print loaded ignore configuration and exit   |

---

## Examples

### Print full tree of current directory

```bash
python tree.py
```

### Print tree for a specific path

```bash
python tree.py /path/to/project
```

### Limit tree depth to 2 levels

```bash
python tree.py -l 2
```

### Copy tree output to clipboard

```bash
python tree.py -c
```

### Show ignore configuration

```bash
python tree.py --show-ignore
```

---

## Output Example

```text
project/
├── README.md
├── src/
│   ├── main.py
│   └── utils.py
└── tests/
    └── test_main.py
```

---

## Configuration (`config.json`)

The tool looks for a `config.json` file in the current working directory.

If the file does not exist, defaults are used.

### Default Configuration

```json
{
  "ignore": {
    "folders": [],
    "files": []
  }
}
```

### Example Configuration

```json
{
  "ignore": {
    "folders": ["__pycache__", ".git", "node_modules"],
    "files": [".DS_Store", "*.log"]
  }
}
```

> **Note:**
> Ignore matching is based on exact names only (no glob or wildcard support).

---

## How Ignore Logic Works

* If a path is a **directory**, its name is checked against `ignore.folders`
* If a path is a **file**, its name is checked against `ignore.files`
* Ignored paths are completely excluded from the tree

---

## Error Handling

* Missing `config.json` → silently ignored
* Invalid `config.json` → prints error message
* Permission errors → shown as `[Permission denied]`
* Non-existent path → prints an error message

---

## Internals Overview

* `load_config()`
  Loads ignore settings from `config.json`

* `should_ignore(path)`
  Determines whether a file or folder should be skipped

* `build_tree()`
  Recursively constructs the tree structure

* `generate_tree()`
  Entry point for producing the final tree output

* `main()`
  CLI argument parsing and execution logic

---

## License

MIT (or specify your preferred license)

---

## Notes

* Sorting places directories before files
* Tree connectors adapt correctly for last/inner nodes
* Clipboard support works across platforms via `pyperclip`

---

Happy hacking 🌲

```
