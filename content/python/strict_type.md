# Programmatic Strict Type Validation in Python (VSCode + Mypy/Pyright)

## Context:

* You have **strict type checking enabled in VSCode** via **Pyright (Pylance)** or **Mypy**.
* You want to **run type checks on code programmatically** and **get the feedback as a string or structured data** for further use.

---

## 1. Using **Mypy** Programmatically (Recommended)

* Mypy provides a **Python API** for running type checks and capturing output.

### Example:

```python
from mypy import api
from pathlib import Path
from typing import List, Dict, TypedDict, Union

class IssueDict(TypedDict):
    type: str
    message: str
    detail: str
    line: str
    code: str

Issue = IssueDict
ValidationResults = Dict[str, List[Issue]]

def validate_types(path: Union[str, Path], recursive: bool = False) -> ValidationResults:
    path = Path(path)
    results: ValidationResults = {}

    files = [path] if path.is_file() else list(path.rglob("*.py") if recursive else path.glob("*.py"))
    if not files:
        return {"error": [{"type": "Error", "message": "No Python files found", "detail": "", "line": "", "code": ""}]}

    for file in files:
        stdout, _, exit_code = api.run([str(file), "--strict"])
        if exit_code != 0:
            results[str(file)] = _parse_mypy_output(stdout)
    return results

def _parse_mypy_output(output: str) -> List[Issue]:
    issues = []
    for line in output.splitlines():
        parts = line.split(":", 3)
        if len(parts) < 4:
            continue
        file, line_no, _, message = parts
        issues.append({"type": "TypeError", "message": message.strip(), "detail": "", "line": line_no.strip(), "code": file.strip()})
    return issues
```

---

## 2. Using **Pyright** via subprocess

* Pyright has no official Python API but supports JSON output.
* Run Pyright from Python subprocess and parse JSON output.

### Example:

```python
import subprocess, json
from pathlib import Path
from typing import List, Dict, TypedDict, Union

class IssueDict(TypedDict):
    type: str
    message: str
    detail: str
    line: str
    code: str

ValidationResults = Dict[str, List[IssueDict]]

def validate_types_with_pyright(path: Union[str, Path]) -> ValidationResults:
    path = Path(path)
    cmd = ["pyright", "--outputjson", str(path)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode not in (0, 1):
        return {"error": [{"type": "Error", "message": proc.stderr, "detail": "", "line": "", "code": ""}]}

    output = json.loads(proc.stdout)
    results = {}
    for diag in output.get("generalDiagnostics", []):
        file = diag.get("file", "unknown")
        results.setdefault(file, []).append({
            "type": diag.get("severity", "error").capitalize(),
            "message": diag.get("message", ""),
            "detail": diag.get("rule", ""),
            "line": str(diag.get("range", {}).get("start", {}).get("line", "")),
            "code": file
        })
    return results
```

---

## 3. Integration

* Use your existing `print_results(results)` or `validation_results_to_str(results)` functions to format/display issues.
* You get structured, detailed feedback like:

```
File: example.py
  1. TypeError:
     Line: 10
     error: Incompatible types in assignment (expression has type "int", variable has type "str")
```

---

## Summary:

| Feature                      | Mypy (via API)               | Pyright (via subprocess)                      |
| ---------------------------- | ---------------------------- | --------------------------------------------- |
| Integration in Python script | ✅ Official Python API        | ✅ CLI JSON output, no API                     |
| Performance                  | Moderate                     | Very fast                                     |
| Setup                        | `pip install mypy`           | Install Pyright globally (`npm i -g pyright`) |
| VSCode built-in usage        | Mypy extension/plugin needed | Built-in with Pylance extension               |
| Best for CLI/automation      | ✅                            | ✅                                             |

---