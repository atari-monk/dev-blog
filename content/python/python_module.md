# Python Local/Dev Module

## setup.py

```py
from setuptools import setup, find_packages

setup(
    name="task-log-sqlite",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "project_cli=project.project_cli:main"
        ],
    },
    python_requires=">=3.7",
)
```

## reload

in proj root

```bash
pip install -e .
```

```bash
pip uninstall task-log-sqlite
```

```bash
pip list
```

```bash
pip show task-log-sqlite
```