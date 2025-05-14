# Virtual Environments

## Create and Activate a Virtual Environment

- Create a virtual environment:
  ```bash
  python -m venv venv
  ```

- Activate on Windows (PowerShell/CMD):
  ```bash
  .\venv\Scripts\activate
  ```

- Activate on macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

## Manage Dependencies

- Install a package (e.g., `pytest`):
  ```bash
  pip install pytest
  ```

- Export dependencies to `requirements.txt`:
  ```bash
  pip freeze > requirements.txt
  ```

- Restore dependencies later:
  ```bash
  pip install -r requirements.txt
  ```

- Deactivate the environment:
  ```bash
  deactivate
  ```

## VS Code Configuration

- Select the virtual environment as the Python interpreter:
  1. Open Command Palette (`Ctrl+Shift+P` / `Cmd+Shift+P`)
  2. Search for **"Python: Select Interpreter"**
  3. Choose the path to `venv/Scripts/python` (Windows) or `venv/bin/python` (macOS/Linux)

- Manually select interpreter if missed:
  1. Click Python version in VS Code status bar
  2. Pick the `venv` interpreter

## Dependency Version Control

- Specify a package version in `requirements.txt`:
  ```text
  pytest==7.4.0
  ```

## Best Practices

- Exclude `venv/` from Git (add to `.gitignore`)
- Always activate the environment before development
- Use `requirements.txt` for reproducible setups