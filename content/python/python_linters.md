# Python Linters

## ✅ RECOMMENDED MINIMAL SETUP (for most developers):

* **Pylance + Mypy**

This gives you:

* Fast in-editor type checking (Pylance)
* Static type checking across your codebase (Mypy)

📦 Install:

```bash
pip install mypy
```

Then in `.vscode/settings.json`:

```json
{
  "python.analysis.typeCheckingMode": "strict",
  "python.linting.enabled": true,
  "python.linting.mypyEnabled": true
}
```

---

### 🔍 OPTIONAL LINTERS (only pick one of these):

| Linter     | What It Does                             | Good For                        | Notes                     |
| ---------- | ---------------------------------------- | ------------------------------- | ------------------------- |
| **Flake8** | Code style, unused variables, formatting | Clean code                      | Lightweight, customizable |
| **Pylint** | Style + some logic issues                | Large projects, deep inspection | Slower, can be noisy      |
| **Mypy**   | Type checking only                       | Projects using type hints       | Pairs well with Pylance   |

📌 You generally pick **one** from Flake8 or Pylint. If you're already using type hints, **Mypy is a great addition**.

---

### 🧠 TL;DR Recommendation

**Start with:**

* ✅ `Pylance` (`python.analysis.typeCheckingMode: "strict"`)
* ✅ `Mypy`

If you want extra code quality/style enforcement:

* Add either 🔹 `Flake8` *or* 🔹 `Pylint` — not both.

Let me know your project type (e.g. data science, web, CLI app), and I can suggest the best combo.
