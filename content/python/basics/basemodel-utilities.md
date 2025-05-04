# BaseModel Utilities

- Delegation to utility functions in `BaseModel`:
  ```python
  @classmethod
  def load_from_json(cls: Type[T], file_path: Path) -> List[T]:
      return load_from_json(cls, file_path)
  ```
  - Uses `Type[T]` for correct subclass typing
  - Returns `List[T]` for type safety

- Utility function characteristics:
  - Pure functions (stateless)
  - Easy to test independently
  - Swappable implementations via base class

- Type consistency:
  - `T` bounded to `BaseModel`
  - `Path` for file operations
  - Full type hint coverage

- Optional advanced testing approach:
  ```python
  class BaseModel:
      json_loader = staticmethod(load_from_json)  # Injectable utility
  ```