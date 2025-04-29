# Static Methods Explained

## Static Method Basics

- `@staticmethod` does not take `self` or `cls` as first parameter:
  ```python
  class MyClass:
      @staticmethod
      def say_hello(name):
          print(f"Hello, {name}!")
  ```
- Valid calling methods:
  ```python
  MyClass.say_hello("Alice")   # Class call
  obj = MyClass()
  obj.say_hello("Bob")         # Instance call
  ```

## Instance Call Behavior

- Static methods can be called via `self` despite not using it:
  ```python
  class Demo:
      @staticmethod
      def show():
          print("Static method called")

      def call_static(self):
          self.show()  # Works but doesn't use self
  ```

## Utility Organization

- For standalone functions, consider `utils.py`:
  ```python
  # utils.py
  def normalize_string(s):
      return s.strip().lower()
  ```
- Usage in classes:
  ```python
  from utils import normalize_string

  class User:
      def __init__(self, name):
          self.name = normalize_string(name)
  ```

## Wrapper Pattern

- Combine utility functions with class static methods:
  ```python
  # utils.py
  def normalize_string(s):
      return s.strip().lower()

  # user.py
  class User:
      @staticmethod
      def normalize_name(name):
          return normalize_string(name)
  ```
- Enhanced wrapper example:
  ```python
  @staticmethod
  def normalize_name(name):
      if not name:
          return ''
      return normalize_string(name)
  ```