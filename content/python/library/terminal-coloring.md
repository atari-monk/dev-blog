# Terminal Coloring

- Install Colorama:
  ```bash
  pip install colorama
  ```

## Basic Usage

```python
from colorama import Fore, Back, Style, init

init()

print(Fore.RED + "Red text" + Style.RESET_ALL)
print(Fore.GREEN + "Green text" + Style.RESET_ALL)
print(Back.YELLOW + "Yellow background" + Style.RESET_ALL)
print(Fore.BLUE + Back.WHITE + "Blue on white" + Style.RESET_ALL)
print(Style.BRIGHT + "Bright text" + Style.RESET_ALL)
```

## Color Options

- Foreground (`Fore`):
  `BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE`
- Background (`Back`):
  Same colors as `Fore`
- Styles (`Style`):
  `DIM, NORMAL, BRIGHT, RESET_ALL`

## Utility Function

```python
def color_print(text, color=Fore.WHITE, bg=Back.BLACK, style=Style.NORMAL):
    print(style + color + bg + text + Style.RESET_ALL)

color_print("Warning!", Fore.RED, style=Style.BRIGHT)
```

## Requirements

- Always include `Style.RESET_ALL`
- Mandatory `init()` call (Windows/PowerShell)
- Supported terminals: CMD, PowerShell, bash