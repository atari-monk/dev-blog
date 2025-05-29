In Python, use `__str__` **without parentheses** when you're referring to the method itself — for example, when defining or overriding it in a class. Use `__str__()` **with parentheses** when you're calling or invoking the method.

### ✅ Use `__str__` when:

You're referring to the method object — like defining or accessing it:

```python
class Person:
    def __str__(self):  # <-- defining the method
        return "This is a Person"

p = Person()
print(p.__str__)  # <-- referring to the method object itself (not calling it)
```

### ✅ Use `__str__()` when:

You're explicitly **calling** the method to get its return value:

```python
p = Person()
print(p.__str__())  # <-- calling the method
```

### But usually:

You don't call `__str__()` directly. Instead, Python calls it automatically when you use `str(obj)` or `print(obj)`:

```python
print(p)           # Automatically uses p.__str__()
print(str(p))      # Also uses p.__str__()
```

### Summary:

* `__str__` → refers to the method itself
* `__str__()` → calls the method
* Prefer `str(obj)` or `print(obj)` rather than calling `__str__()` directly
