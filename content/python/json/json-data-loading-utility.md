# JSON Data Loading Utility

- Generic JSON loader function (`utils/json_loader.py`):
  ```python
  from typing import Type, TypeVar, List
  from pathlib import Path
  import json

  T = TypeVar("T")

  def load_from_json(cls: Type[T], file_path: Path) -> List[T]:
      if not file_path.exists():
          raise FileNotFoundError(f"File not found: {file_path}")

      with open(file_path, "r", encoding="utf-8") as f:
          data = json.load(f)

      if not isinstance(data, list):
          raise ValueError("JSON data should be a list of items")

      return [cls(**item) for item in data]
  ```

- Example model (`models/person.py`):
  ```python
  from dataclasses import dataclass

  @dataclass
  class Person:
      name: str
      age: int
  ```

- Implementation usage (`main.py`):
  ```python
  from pathlib import Path
  from models.person import Person
  from utils.json_loader import load_from_json

  people = load_from_json(Person, Path("people.json"))

  for p in people:
      print(p)
  ```

- Optional classmethod convenience method:
  ```python
  @classmethod
  def from_json(cls, file_path: Path):
      from utils.json_loader import load_from_json
      return load_from_json(cls, file_path)
  ```