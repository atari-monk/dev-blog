# Naming Conventions

## Class Naming (PascalCase)
- Use `PascalCase` for class names:
  ```python
  class MyClass:
      pass
  ```
- Defined in [PEP 8](https://www.python.org/dev/peps/pep-0008/#class-names)

## Module Naming (snake_case)
- Use `snake_case` for filenames: `my_class.py`
- Defined in [PEP 8](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)

## Example Implementation
```python
# my_class.py
class MyClass:
    pass

__all__ = ['MyClass']
```
- Usage:
  ```python
  from my_class import MyClass
  ```

## Key Reasons
- Filesystem case sensitivity issues (Windows compatibility)
- Consistency with Python's import system
- Readability distinction between modules and classes

## Best Practice
- Always use `snake_case` for filenames
- Always use `PascalCase` for class names