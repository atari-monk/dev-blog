# Last Element

To get the last element of a list in Python, including a list of objects like `List[Task]`, you can use negative indexing:

```python
last_task = tasks[-1]
```

This will return the last `Task` object in the `tasks` list.

> ⚠️ Make sure the list is not empty, or you'll get an `IndexError`.

To be safe, you can do:

```python
if tasks:
    last_task = tasks[-1]
else:
    last_task = None  # or handle it however appropriate
```
