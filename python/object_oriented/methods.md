# Methods

- Basic class with instance methods:

  ```python
  class Dog:
      species = "Canis familiaris"

      def __init__(self, name, age):
          self.name = name
          self.age = age

      def bark(self):
          return f"{self.name} says woof!"

      def describe(self):
          return f"{self.name} is {self.age} years old"
  ```

## Method Types

- Instance method:
  ```python
  def instance_method(self, arg1, arg2):
      # method body
  ```

- Class method:
  ```python
  @classmethod
  def class_method(cls, arg1, arg2):
      # method body
  ```

- Static method:
  ```python
  @staticmethod
  def static_method(arg1, arg2):
      # method body
  ```

## Complete Implementation

```python
class MyClass:
    class_attribute = "I'm a class attribute"

    def __init__(self, value):
        self.instance_attribute = value

    def instance_method(self):
        return f"Instance method called, instance attribute: {self.instance_attribute}"

    @classmethod
    def class_method(cls):
        return f"Class method called, class attribute: {cls.class_attribute}"

    @staticmethod
    def static_method():
        return "Static method called"

    def __str__(self):
        return f"MyClass with value: {self.instance_attribute}"
```