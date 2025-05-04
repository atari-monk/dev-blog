# JSON and Pydantic

## Define a Pydantic Model

```python
from pydantic import BaseModel

class Person(BaseModel):
    name: str
    age: int
```

## Load a List of Items from JSON

```python
from typing import Type, TypeVar, List
from pathlib import Path
import json

T = TypeVar("T", bound=BaseModel)

def load_from_json(cls: Type[T], file_path: Path) -> List[T]:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Expected a list of objects in JSON")

    return [cls(**item) for item in data]
```

## Usage Example

```python
people = load_from_json(Person, Path("people.json"))

for person in people:
    print(person)
```

## Built-in Pydantic Methods for Single Objects

```python
# From JSON string
person = Person.parse_raw('{"name": "Alice", "age": 30}')

# From file
person = Person.parse_file("person.json")
```

## Handling Lists with Built-in Methods

```python
with open("people.json") as f:
    raw_list = json.load(f)

people = [Person(**item) for item in raw_list]
```

## Complete Implementation

```python
from pathlib import Path
from typing import Type, TypeVar, List
from pydantic import BaseModel
import json

T = TypeVar("T", bound=BaseModel)

class Person(BaseModel):
    name: str
    age: int

def load_from_json(cls: Type[T], file_path: Path) -> List[T]:
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Expected a list of objects in JSON")

    return [cls(**item) for item in data]
```