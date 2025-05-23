# Black

The **Black** formatter, often referred to as **"Black, the uncompromising Python code formatter"**, is a popular opinionated code formatter for Python. It reformats entire files to follow a consistent style, promoting readability and reducing stylistic debates in code reviews.

## 🔧 Key Features

* **Opinionated**: Black enforces a specific coding style with minimal configuration. This reduces bikeshedding about code formatting.
* **Consistent Output**: It reformats your code to look the same every time, no matter who wrote it.
* **Speed**: It’s fast and designed to work well in automated tools and pre-commit hooks.
* **Safe**: Black only reformats code that is syntactically correct. It parses the code into an abstract syntax tree (AST) and then reprints it—so it won’t change the behavior of your code.
* **Supports Python 3.6+**: Including modern features like f-strings, type annotations, and assignment expressions.

## 🛠 How to Use

### Installation

```bash
pip install black
```

### Formatting a File

```bash
black your_script.py
```

### Formatting All Files in a Directory

```bash
black .
```

## ⚙️ Options

* `--check`: Checks if the file would be reformatted, without changing it.
* `--diff`: Shows the diff of what would change.
* `--line-length`: Sets the maximum line length (default is 88 characters).
* `--skip-string-normalization`: Prevents Black from changing string quotes (e.g., single to double).
* `--target-version`: Set the Python versions Black should target for syntax (e.g., `py38`, `py310`).

## 🧪 Example

Before:

```python
def add(a,b): return a+b
```

After running `black`:

```python
def add(a, b):
    return a + b
```

## 💡 Common Uses

* IDE integration (e.g., with VS Code, PyCharm)
* Pre-commit hooks in Git
* CI pipelines to ensure codebase consistency

Would you like help setting it up in a project or using it with a specific tool?
