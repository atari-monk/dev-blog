# Prettier Formatter

## Configuration File

Create `.prettierrc` in your project root:

```json
{
  "tabWidth": 2,
  "semi": false,
  "singleQuote": true,
  "arrowParens": "avoid",
  "trailingComma": "es5",
  "printWidth": 80,
  "endOfLine": "crlf",
  "bracketSpacing": false
}
```

## Key Options

- `tabWidth`: 2-space indentation
- `semi`: Disables semicolons
- `singleQuote`: Enforces single quotes
- `arrowParens`: "avoid" omits parens for single parameters
- `trailingComma`: Adds ES5-valid trailing commas
- `printWidth`: 80-character line limit
- `endOfLine`: Windows CRLF line endings
- `bracketSpacing`: Removes space inside object braces

## Format entire code base

```sh
npx prettier --write .
```

To format your entire codebase with Prettier, use the following command in your terminal:

```bash
npx prettier --write .
```

### Explanation:

* `npx` runs Prettier without installing it globally.
* `prettier` is the formatter.
* `--write` tells Prettier to overwrite the files with the formatted code.
* `.` tells it to process the current directory and all subdirectories.

### Optional: Exclude specific files or directories

If you want to ignore certain files, use a `.prettierignore` file (similar to `.gitignore`).

Would you like a sample `.prettierrc` or `.prettierignore` file setup?
