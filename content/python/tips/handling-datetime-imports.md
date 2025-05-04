# Handling Datetime Imports

- Correct implementation using class import:
  ```python
  from datetime import datetime
  import pyperclip

  def get_formatted_timestamp(now):
      return now.strftime("%Y-%m-%d %H:%M")

  def copy_timestamp_to_clipboard():
      pyperclip.copy(get_formatted_timestamp(datetime.now()))
  ```

- Alternative using module import:
  ```python
  import datetime
  import pyperclip

  def get_formatted_timestamp(now):
      return now.strftime("%Y-%m-%d %H:%M")

  def copy_timestamp_to_clipboard():
      pyperclip.copy(get_formatted_timestamp(datetime.datetime.now()))
  ```

Key differences:
- First approach imports only `datetime` class (direct method access)
- Second approach requires full qualification (`datetime.datetime.now()`)