# Direct vs Imported Script

Here's a short guide on the correct usage of `if __name__ == '__main__':` in Python:

```python
def main():
    print("This is the main function")

if __name__ == '__main__':
    main()
```

Key points:

1. Use `'__main__'` (with double underscores on both sides), not `'main'`
2. This check allows your code to:
   - Run when executed directly (`python script.py`)
   - Not run when imported as a module
3. The `main()` function contains your program's main logic
4. This is Python's way of determining if the script is being run directly

Common mistake to avoid:

```python
if __name__ = 'main':  # Wrong (single = and wrong string)
    main()
```
