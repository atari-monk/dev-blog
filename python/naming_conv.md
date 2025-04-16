In Python, the convention for naming files containing classes follows the general guidelines for module naming, which is different from the class naming convention. Here's the breakdown:

### Class Naming (PascalCase / UpperCamelCase)

- Class names should use `PascalCase`: `ClassName`
- This is defined in [PEP 8](https://www.python.org/dev/peps/pep-0008/#class-names)

### Module/Filename Naming (snake_case)

- Filenames (modules) should use `snake_case`: `class_name.py`
- This is defined in [PEP 8](https://www.python.org/dev/peps/pep-0008/#package-and-module-names)
- Rationale: Filesystem case sensitivity issues (especially important for cross-platform compatibility)
- Even if the file contains only one class, the filename should not use PascalCase

### Example:

- Class: `class MyClass:` in file `my_class.py`
- Usage: `from my_class import MyClass`

### Why not match the filename to the class name?

1. **Filesystems**: Some filesystems are case-insensitive (Windows), which could cause issues.
2. **Consistency**: Python's import system and ecosystem heavily use `snake_case` for modules.
3. **Readability**: `snake_case` filenames are instantly recognizable as modules (not classes).

### Special Case:

If your module is primarily a single class and you want to emphasize this, you can do:

```python
# my_class.py
class MyClass:
    pass

__all__ = ['MyClass']  # Explicitly exports the class
```

But the filename remains `snake_case`.

### Best Practice:

Use `snake_case` for filenames (`my_class.py`) and `PascalCase` for class names (`MyClass`). This follows Python's strong conventions and avoids potential issues.
