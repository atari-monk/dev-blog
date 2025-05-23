# Template

If you want to **use `element_type` inside the `description`** as a **template**, so that the description can automatically incorporate the `element_type`, you can achieve this using Python’s string formatting capabilities, such as **f-strings** or the **`str.format()`** method.

Here’s how you can do it in practice:

---

## ✅ Option 1: Use `__post_init__`-like logic (if using Pydantic BaseModel) with a method

```python
from pydantic import BaseModel
from pathlib import Path
from typing import List

class Task(BaseModel):
    assumptions: List[str]
    description_template: str
    file_path: Path
    element_type: str

    @property
    def description(self) -> str:
        return self.description_template.format(element_type=self.element_type)
```

### Example usage:

```python
task = Task(
    assumptions=["All inputs are validated."],
    description_template="This task processes the {element_type} from the file.",
    file_path=Path("/some/path/file.csv"),
    element_type="CSV data"
)

print(task.description)
# Output: This task processes the CSV data from the file.
```

---

## ✅ Option 2: Use `description` as an f-string and render it dynamically

If you want to support f-string-like behavior (i.e., `{self.element_type}` inside the string), you'd need to **evaluate the string dynamically**:

```python
class Task(BaseModel):
    assumptions: List[str]
    description_template: str
    file_path: Path
    element_type: str

    @property
    def description(self) -> str:
        return eval(f'f"""{self.description_template}"""')
```

### Example:

```python
task = Task(
    assumptions=["Something..."],
    description_template="This task handles {self.element_type} carefully.",
    file_path=Path("/tmp/file.json"),
    element_type="JSON data"
)

print(task.description)
# Output: This task handles JSON data carefully.
```

⚠️ **Warning**: Using `eval` is **not safe** if the source of the template string is untrusted. Stick to `.format()` or string interpolation when security is a concern.

---

## Summary

| Approach           | Template Format                  | Safe?                              |
| ------------------ | -------------------------------- | ---------------------------------- |
| `.format()`        | `"Handles {element_type} well."` | ✅ Yes                              |
| `eval(f"""...""")` | `"Handles {self.element_type}."` | ❌ No (unsafe with untrusted input) |

Let me know if you want to support more complex templating (like Jinja2).
