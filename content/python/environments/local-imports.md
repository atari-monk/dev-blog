# Local Imports

## Imports Problem

- Repo imports fail unless treated as a Python module
- Solution: Convert repo into an installable local package

## Editable Package Setup

```sh
pip install setuptools
```

Required files:
- `__init__.py` in root
- `setup.py` in root

```py
from setuptools import setup, find_packages

setup(
    name="py_scripting",
    version="0.1",
    packages=find_packages(),
)
```

```sh
pip install -e .
```

## Verification

Check installation:

```sh
pip list | grep py_scripting
```

Verify Python environment:

```sh
python -c "import sys; print(sys.executable)"
```

## Clean Reinstallation

```sh
pip uninstall py_scripting -y
rm -rf py_scripting.egg-info
pip install -e .
```

## Usage Example

```py
from py_scripting.selenium_scripts.chatgpt import initialize_chatgpt_session
```

## Reinstall Triggers

- Adding new subpackages
- Changing `setup.py` dependencies
- Renaming/moving major directories