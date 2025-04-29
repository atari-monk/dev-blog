# Formatting Tools

## Black Installation

```bash
pip install black
```

- Format single file:
  ```bash
  black your_file.py
  ```
- Format entire directory:
  ```bash
  black .
  ```

## autopep8 Installation

```bash
pip install autopep8
```

- Fix PEP 8 violations:
  ```bash
  autopep8 --in-place --aggressive your_file.py
  ```

## yapf Installation

```bash
pip install yapf
```

- Format in-place:
  ```bash
  yapf -i your_file.py
  ```

## Ruff Installation

```bash
pip install ruff
```

- Format all files:
  ```bash
  ruff format .
  ```

## Configuration Files

- Prettier config (non-Python files):
  ```json
  {
  	"semi": false,
  	"singleQuote": true,
  	"tabWidth": 2
  }
  ```
- Black config:
  ```toml
  [tool.black]
  line-length = 88
  target-version = ["py310"]
  ```

## Pre-commit Setup

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
  - repo: https://github.com/prettier/prettier
    rev: "3.0.0"
    hooks:
      - id: prettier
        exclude: \.py$
```