# Python Requirements

To install the requirements for a Python project, you typically use a `requirements.txt` file and the `pip` package manager.

## ✅ Steps to install requirements in Python:

1. **Ensure you're in the correct environment (optional but recommended):**
   If you're using a virtual environment:

   ```bash
   python -m venv venv
   # source venv/bin/activate   
   # On Windows: 
   venv\Scripts\activate
   ```

2. **Use pip to install from `requirements.txt`:**

   ```bash
   pip install -r requirements.txt
   ```

---

## 📝 Notes:

* Make sure you are in the same directory as the `requirements.txt` file, or provide the full path.
* If you don’t have `requirements.txt`, you can create one by running:

  ```bash
  pip freeze > requirements.txt
  ```

Let me know if you’re using a specific environment (like conda, Docker, or Jupyter), and I can tailor the steps.

## ✅ Why you should ignore `venv`:

1. **It's system-specific** – Virtual environments contain binaries and paths that vary across systems.
2. **It can be large** – The `venv` folder can take up a lot of space and doesn't need to be tracked.
3. **It's not necessary** – Instead of tracking it, just use `requirements.txt` so others can recreate the environment.

---

### 📄 What to add to `.gitignore`:

If your virtual environment folder is named `venv`, add this line:

```
venv/
```

If your environment has a different name (like `.env`, `env`, etc.), add that name instead.

---

Let me know if you're using a different setup like **Poetry**, **Pipenv**, or **Conda**, and I’ll adjust the advice accordingly.
