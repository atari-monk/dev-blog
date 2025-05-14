# Testing

## Prerequisites

- Python 3.6+
- `pytest` package

## Setup

- Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
- Project structure:
  ```
  scripts/
  ├── ...
  └── tests/
      ├── __init__.py
      ├── test_directory_tree.py
      └── test_treemd.py
  ```

## Writing Tests

- File naming: `test_*.py`
- Function naming: `test_*`
- Example test:
  ```python
  from core.directory_tree import DirectoryTree

  def test_empty_tree():
      tree = DirectoryTree()
      assert tree.root is None
  ```

## Running Tests

- Run all tests:
  ```bash
  pytest
  ```
- Specific test file:
  ```bash
  pytest tests/test_directory_tree.py
  ```
- Verbose output:
  ```bash
  pytest -v
  ```

## Test Coverage

- Install coverage:
  ```bash
  pip install pytest-cov
  ```
- Run coverage:
  ```bash
  pytest --cov=core --cov=scripts
  ```

## Frameworks Comparison

### unittest

- Built-in Python
- Requires test classes
- Basic assertions:
  ```python
  self.assertEqual(a, b)
  ```

### pytest

- Requires installation:
  ```bash
  pip install pytest
  ```
- Function-based tests:
  ```python
  assert a == b
  ```
- Advanced features:
  ```python
  @pytest.mark.parametrize("input,expected", [(1,2), (3,4)])
  def test_func(input, expected):
      assert input+1 == expected
  ```