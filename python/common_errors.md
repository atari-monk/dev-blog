# Common Errors

## datetime import naming conflic

Ah, I see the issue! The error occurs because you're trying to use `datetime.now()` but you've imported `datetime` from the `datetime` module, which creates a naming conflict. Here's how to fix it:

### Corrected Implementation (time_utils.py)

```python
from datetime import datetime  # This imports the datetime class
import pyperclip

def get_formatted_timestamp(now):
    return now.strftime("%Y-%m-%d %H:%M")

def copy_timestamp_to_clipboard():
    pyperclip.copy(get_formatted_timestamp(datetime.now()))  # Now this works
```

### Alternative Fix (if you prefer the module import)

```python
import datetime  # This imports the whole module
import pyperclip

def get_formatted_timestamp(now):
    return now.strftime("%Y-%m-%d %H:%M")

def copy_timestamp_to_clipboard():
    pyperclip.copy(get_formatted_timestamp(datetime.datetime.now()))  # Need to use datetime.datetime
```

The key difference:

1. In the first solution, we import just the `datetime` class from the module
2. In the second solution, we import the whole module and need to qualify `datetime.datetime.now()`

The error occurred because when you do `import datetime`, you need to use `datetime.datetime.now()` (module.class.method), but if you do `from datetime import datetime`, then you can use just `datetime.now()`.

I recommend the first solution as it's cleaner for this use case. Would you like me to explain any part of this in more detail?
