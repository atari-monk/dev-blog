# repr

The `__repr__` method in Python is a special method used to define the **official string representation** of an object. It's mainly used for:

---

## 🧪 1. **Debugging and Logging**

When you print an object or inspect it in a debugger, `__repr__` is what gets shown.

Example:

```python
db = DbPath("/my/repo", "subdir")
print(db)
# Without __repr__: <__main__.DbPath object at 0x109b5>
# With __repr__:    DbPath(path=PosixPath('/my/repo/subdir'))
```

Much easier to understand what's going on at a glance!

---

## 🧑‍💻 2. **Interactive Sessions and REPLs**

When working in a Python shell or Jupyter Notebook, the REPL shows the `__repr__` output:

```python
>>> db = DbPath("/tmp", "data")
>>> db
DbPath(path=PosixPath('/tmp/data'))
```

This gives you immediate, useful feedback about the object.

---

## 📖 3. **Best Practice for Custom Classes**

Python’s data model recommends defining `__repr__` for classes where object inspection is useful.

From the [official docs](https://docs.python.org/3/reference/datamodel.html#object.__repr__):

> If at all possible, this should look like a valid Python expression that could be used to recreate the object.

---

## ✅ Example for Your Class

```python
class DbPath:
    def __init__(self, db_repository_path: Union[str, Path], subdir: str):
        self.repo_path = Path(db_repository_path)
        self.path = self.repo_path / subdir
        self.path.mkdir(parents=True, exist_ok=True)

    def __repr__(self):
        return f"DbPath(path={self.path!r})"
```

This way, if anything goes wrong or you're trying to understand an object in logs, you'll see something useful.

---

## TL;DR

`__repr__` is **mainly for developers**. It makes your object easier to inspect, debug, and understand during development or testing. Highly recommended for any class you’ll work with directly.
