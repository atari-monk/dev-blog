# Bounded TypeVar

- `TypeVar`s are scoped to their defining module:
  ```python
  # base.py
  T = TypeVar("T", bound="BaseModel")

  # utils.py
  T = TypeVar("T")  # Separate scope, no conflict
  ```

- Bounding to `BaseModel` ensures correct typing for class methods:
  ```python
  class BaseModel:
      @classmethod
      def deserialize(cls: Type[T]) -> T:
          ...
  ```

- Unbounded `TypeVar` in utilities still works when passed bounded types:
  ```python
  # json_utils.py
  T = TypeVar("T")

  def load_from_json(cls: Type[T], path: Path) -> List[T]:
      # cls satisfies type constraints when bounded to BaseModel
      ...
  ```

- Key behavior:
  - Bounded `T` enforces subclass relationships
  - Unbounded `T` accepts any type
  - No cross-module `TypeVar` collisions
```