# Utility File Conventions

- Common utility file naming:
  ```python
  utils.py  # Generic utilities (Python)
  utils.js  # Generic utilities (JavaScript)
  ```

- Recommended specialized utility files:
  ```python
  string_utils.py  # String manipulation helpers
  date_utils.py    # Date/time operations
  file_utils.py    # File system operations
  ```

- Key considerations:
  - Start with generic `utils` for early-stage projects
  - Refactor into specialized files as codebase grows
  - Group related functions by domain (strings, dates, files)