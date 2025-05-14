# Optional Parameters

- Optional parameters (with default values) should use keyword arguments for clarity:
  ```python
  def save_chatgpt_code_block(driver, output_file_path: str, delay_seconds: int, json: bool = False):
  ```

- Positional arguments can cause confusion with optional parameters:
  ```python
  # Avoid - ambiguous which parameter True applies to
  save_chatgpt_code_block(driver, "file.json", 1, True)
  ```

- Correct keyword argument usage:
  ```python
  save_chatgpt_code_block(driver, "file.json", 1, json=True)
  ```

- Required parameters without defaults must be passed positionally:
  ```python
  def save_chatgpt_code_block(driver, output_file_path: str, delay_seconds: int, json: bool):
  ```
  ```python
  save_chatgpt_code_block(driver, "file.json", 1, True)
  ```