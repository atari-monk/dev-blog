# Prettier Configuration

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