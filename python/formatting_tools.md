# Formatting Tools

## Options

Prettier doesn’t support Python well because Python relies on significant whitespace (indentation matters!), and Prettier is primarily designed for JavaScript, TypeScript, HTML, CSS, and similar languages.

### **Best Alternatives to Prettier for Python Formatting**

Here are the top tools for formatting Python code:

#### **1. Black** (Most Popular)

✅ **Opinionated, no configuration needed** – Just run it and your code is formatted.  
✅ **PEP 8 compliant** – Follows Python’s style guide.  
✅ **Fast & Reliable** – Used by major projects like Django, Pandas, and FastAPI.

**Install:**

```bash
pip install black
```

**Usage:**

```bash
black your_file.py  # Format a single file
black .             # Format all Python files in the current directory
```

#### **2. autopep8** (Good for Fixing PEP 8 Violations)

✅ **Fixes PEP 8 issues** – Helps make code compliant with Python’s style guide.  
✅ **Configurable** – More flexible than Black.

**Install:**

```bash
pip install autopep8
```

**Usage:**

```bash
autopep8 --in-place --aggressive your_file.py
```

#### **3. yapf** (Google’s Formatter)

✅ **Highly Configurable** – Like Prettier, but for Python.  
✅ **Supports Different Styles** (PEP 8, Google style, custom).

**Install:**

```bash
pip install yapf
```

**Usage:**

```bash
yapf -i your_file.py  # Format in-place
```

#### **4. Ruff (Fast & Modern)**

✅ **Extremely fast** (written in Rust).  
✅ **Combines formatting + linting**.  
✅ **Drop-in replacement for Black + Flake8 + isort**.

**Install:**

```bash
pip install ruff
```

**Usage:**

```bash
ruff format .  # Format all files
```

---

### **Which One Should You Use?**

| Tool         | Opinionated           | Speed          | Best For                      |
| ------------ | --------------------- | -------------- | ----------------------------- |
| **Black**    | ✅ Yes                | ⚡ Fast        | Simple, consistent formatting |
| **autopep8** | ❌ No                 | � Slow         | Fixing PEP 8 issues           |
| **yapf**     | ❌ Configurable       | ⚡ Fast        | Customizable formatting       |
| **Ruff**     | ✅ (Black-compatible) | ⚡⚡⚡ Fastest | Formatting + Linting in one   |

**Recommendation:**

- **Use `Black`** if you want a zero-config, consistent formatter.
- **Use `Ruff`** if you want speed + formatting + linting together.

Would you like help setting up a pre-commit hook for auto-formatting? 🚀

## Prettier, Black/Ruff

If you're using **Prettier for HTML, CSS, or JavaScript/TypeScript files** (e.g., in documentation like `docs/`, `*.html`, `*.md`), **keep the Prettier config**—it’s still useful for those!

But if you were trying to use Prettier for **Python** (which doesn’t work well), just **exclude Python files** from Prettier.

### **Recommended Setup**

#### 1. **Keep Prettier for non-Python files**

- Works great for:
  - `*.html`, `*.css`, `*.md`, `*.js`, `*.json`, etc.
- Add this to `.prettierignore` (or modify it):
  ```gitignore
  # .prettierignore
  *.py  # Ignore Python files
  ```

#### 2. **Use Black/Ruff for Python**

- Run Black/Ruff only on Python files.

#### 3. **Example Config (`prettierrc.json` + `pyproject.toml`)**

- **For Prettier (non-Python):**
  ```json
  // .prettierrc.json
  {
  	"semi": false,
  	"singleQuote": true,
  	"tabWidth": 2
  }
  ```
- **For Python (Black/Ruff):**
  ```toml
  # pyproject.toml
  [tool.black]
  line-length = 88
  target-version = ["py310"]
  ```

#### 4. **Pre-commit Hook (Optional but Recommended)**

If you use `pre-commit`, you can run both:

```yaml
# .pre-commit-config.yaml
repos:
  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
  - repo: https://github.com/prettier/prettier
    rev: "3.0.0"
    hooks:
      - id: prettier
        exclude: \.py$ # Skip Python files
```

### **Final Decision**

✅ **Keep Prettier** for HTML/JS/CSS/Markdown.  
❌ **Ignore Python files** in Prettier (use Black/Ruff instead).

This way, you get the best of both worlds! 🚀
