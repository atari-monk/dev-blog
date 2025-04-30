# Python Execution Methods

## Running Python Code

### Direct Script Execution
```bash
python script.py
```

### One-Line Code Execution
```bash
python -c "print('Hello World')"
```

### Module Execution (`-m` flag)
```bash
python -m module_name
```

### Interactive Interpreter
```bash
python  # Launches REPL
```

## Path Separators

### Import Paths
- Dot notation for packages:
```python
from package.subpackage import module
```

### Filesystem Paths
- Cross-platform forward slashes:
```python
open('path/to/file.txt')
```
- Windows raw strings:
```python
open(r'path\to\file.txt')
```
- Platform-independent:
```python
from pathlib import Path
Path('path') / 'to' / 'file.txt'
```

## Best Practices

1. Use `-m` for:
   - Package modules
   - Virtual environments
   - Reliable imports

2. Path handling:
   - Never mix filesystem separators in imports
   - Prefer `pathlib` for filesystem operations
   - Forward slashes work everywhere

3. Execution methods:
   - Scripts: `python script.py`
   - Quick tests: `python -c`
   - Modules: `python -m module`
   - Development: REPL