# Editable Installations

- Install package in development mode:
  ```bash
  pip install -e .
  ```
- Key features:
  - Creates symlink to package instead of copying files
  - Code changes reflect immediately without reinstall
  - Preserves package metadata and dependencies

## Usage Scenarios

- Active package development
- Frequent change testing
- Projects serving as both library and application

## Prerequisites

- Requires `setup.py` or `pyproject.toml` in current directory
- `-e` flag denotes `--editable` mode

## Alternative Methods

- Standard installation:
  ```bash
  pip install .
  ```
- Legacy equivalent:
  ```bash
  python setup.py develop
  ```