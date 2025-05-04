# Pathlib Path Construction

- Partial path construction with `pathlib.Path` allows mixing strings and Path objects:
  ```python
  from pathlib import Path
  Path('a') / 'b' / 'c'  # Valid
  'a' / Path('b') / 'c'  # Valid
  ```

## Gradual Construction

- Build paths incrementally:
  ```python
  base = Path('my_project')
  config_path = base / 'config' / 'settings.ini'
  ```

## Technical Behavior

- `/` operator rules:
  ```python
  Path('a') / 'b'  # Works
  'a' / Path('b')  # Works
  'a' / 'b'        # TypeError
  ```

## Best Practices

- Start with `Path()` for path building:
  ```python
  base = Path('project')
  ```

- Avoid unnecessary Path conversions:
  ```python
  Path('config') / 'settings.ini'  # Preferred
  Path('config') / Path('settings.ini')  # Redundant
  ```

- Use Path methods when needed:
  ```python
  parent_dir = Path(__file__).parent / 'assets'
  ```

## Practical Example

- Combine dynamic and static path components:
  ```python
  def get_data_path(config):
      base = Path(config['base_dir'])
      return base / config['data_folder'] / 'dataset.csv'
  ```