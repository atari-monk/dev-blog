# Guide to `pip install -e .`

## What It Does

The command `pip install -e .` installs a Python package in "editable" or "development" mode from the current directory (`.`).

## Key Features

- Creates a link to your package instead of copying files
- Changes to your code are immediately available without reinstallation
- Maintains package metadata and dependencies

## When to Use It

- During package development
- When you need to test changes frequently
- When working on a project that's both a library and an application

## Requirements

- Must have a `setup.py` or `pyproject.toml` file in the current directory
- `-e` stands for `--editable`

## Common Alternatives

- `pip install .` (regular installation)
- `python setup.py develop` (older equivalent)

This mode is perfect for development but not suitable for production deployments.
