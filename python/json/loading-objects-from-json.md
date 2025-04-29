# Loading Objects from JSON

- Define a class with fields matching JSON keys:
  ```python
  from dataclasses import dataclass
  from pathlib import Path
  from typing import Type, TypeVar, List
  import json

  T = TypeVar('T')

  @dataclass
  class Person:
      name: str
      age: int
  ```

- Implementation of `load_from_json`:
  ```python
  def load_from_json(cls: Type[T], file_path: Path) -> List[T]:
      if not file_path.exists():
          raise FileNotFoundError(f"File not found: {file_path}")

      with open(file_path, "r", encoding="utf-8") as f:
          data = json.load(f)

      if not isinstance(data, list):
          raise ValueError("JSON data should be a list of items")

      return [cls(**item) for item in data]
  ```

- Example JSON file (`people.json`):
  ```json
  [
      { "name": "Alice", "age": 30 },
      { "name": "Bob", "age": 25 }
  ]
  ```

- Usage:
  ```python
  file_path = Path("people.json")
  people = load_from_json(Person, file_path)

  for person in people:
      print(person)
  ```