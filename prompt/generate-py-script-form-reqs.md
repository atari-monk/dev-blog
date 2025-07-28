### 🐍 Prompt: Generate a Modern Python CLI Script with Console Entry Point

Generate a complete, idiomatic Python 3.12+ script that fulfills the following requirements and is designed to be used as a **CLI tool** with a console entry point mapped in `pyproject.toml`.

Your code **must**:

* Be structured as **modular, single-responsibility units**
* Use **strict type hints** everywhere (no implicit `Any`)
* Read like a **well-written narrative** — clean, self-documenting, and expressive
* **Avoid all inline comments** — clarity must come from code structure, naming, and design
* Include a clear `main()` function and a `__name__ == "__main__"` block
* Be compatible with `pyproject.toml` using `[project.scripts] tool-name = "main:main"`
* Prefer `typer` or `argparse` for CLI parsing (based on requirement complexity)
* Be testable and maintainable, with clear separation of logic, IO, and orchestration
* Handle errors gracefully and explicitly

---

### 🧾 Format

```python
# requirements.txt
# TODO: Add required dependencies, e.g., typer

# main.py
# Your Python script starts here
```

`main.py` must include a callable `main()` function, ready for use like this:

```toml
[project]
name = "your-cli-tool"
version = "0.1.0"
requires-python = ">=3.12"

[project.scripts]
your-cli = "main:main"
```

---

### ✅ Output

Return a full `.py` file ready for CLI execution and packaging.

> ✅ Code should be expressive and self-explanatory
> ✅ Avoid comments; code should speak for itself
> ✅ Maintain strict typing and single responsibility

---

### 📋 Requirements

Provide your requirements below:

```txt
# Example:
- Accept a file path to a Markdown file
- Extract all URLs
- Optionally validate URLs with HTTP requests
- Output the result as JSON
```
