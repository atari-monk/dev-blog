# Script Execution

- Correct usage of `if __name__ == '__main__':`:
  ```python
  def main():
      print("This is the main function")

  if __name__ == '__main__':
      main()
  ```

- Key requirements:
  - Use double underscores: `'__main__'`
  - Proper comparison operator: `==`

- Behavior:
  - Executes when run directly (`python script.py`)
  - Skips when imported as module

- Incorrect implementation to avoid:
  ```python
  if __name__ = 'main':  # Assignment operator and wrong string
      main()
  ```

- Best practices:
  - Place main program logic in `main()` function
  - Keep imports and function definitions outside the block