* Name: Generate a Modern Python CLI Script with Console Entry Point
* Purpose / Goal: Create a modular, type-hinted Python CLI script compatible with `pyproject.toml` and modern Python 3.12+ standards.
* Input Data: Requirements for the script's functionality (e.g., file path to a Markdown file, URL extraction, JSON output).
* Constraints / Requirements:
  - Modular, single-responsibility units
  - Strict type hints
  - No inline comments; self-documenting code
  - Clear `main()` function and `__name__ == "__main__"` block
  - Compatible with `pyproject.toml`
  - Use `typer` or `argparse` for CLI parsing
  - Testable and maintainable with clear separation of logic, IO, and orchestration
  - Graceful and explicit error handling
* Task / Action: Generate a complete Python script adhering to the specified requirements and format.
* Expected Output / Format: A full `.py` file ready for CLI execution and packaging, with expressive and self-explanatory code.