Perfect — here’s a clear **ESLint + Prettier setup** that works well for a **Vite + TypeScript** project and helps enforce consistent naming, formatting, and best practices.

I’ll break it down into:
✅ **1. Dependencies**
✅ **2. `eslint` config**
✅ **3. `prettier` config**
✅ **4. How to enforce naming conventions with ESLint**

---

## ✅ 1️⃣ Install dependencies

```bash
npm install -D eslint prettier eslint-config-prettier eslint-plugin-prettier @typescript-eslint/eslint-plugin @typescript-eslint/parser
```

---

## ✅ 2️⃣ Example **`.eslintrc.json`**

```json
{
  "env": {
    "browser": true,
    "es2021": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:prettier/recommended"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaVersion": "latest",
    "sourceType": "module"
  },
  "plugins": ["@typescript-eslint", "prettier"],
  "rules": {
    "prettier/prettier": "error",
    "@typescript-eslint/naming-convention": [
      "error",
      {
        "selector": "variableLike",
        "format": ["camelCase"],
        "leadingUnderscore": "allow"
      },
      {
        "selector": "typeLike",
        "format": ["PascalCase"]
      },
      {
        "selector": "enumMember",
        "format": ["UPPER_CASE"]
      }
    ]
  }
}
```

**What this does:**
✔️ Uses TypeScript rules
✔️ Runs Prettier as an ESLint rule
✔️ Enforces:

* `camelCase` for variables, functions, hooks
* `PascalCase` for types, interfaces, classes, components
* `UPPER_CASE` for enum members

---

## ✅ 3️⃣ Example **`.prettierrc`**

```json
{
  "semi": true,
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2,
  "trailingComma": "es5",
  "bracketSpacing": true
}
```

---

## ✅ 4️⃣ Add lint & format scripts in `package.json`

```json
{
  "scripts": {
    "lint": "eslint . --ext .ts,.tsx",
    "format": "prettier --write ."
  }
}
```

---

## ✅ **Bonus: Format on save**

If you’re using **VS Code**, add this to `.vscode/settings.json`:

```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

---

## ⚡️ Final tip

👉 ESLint doesn’t enforce file/folder **names** directly — but you can keep that consistent with clear conventions + a simple code review or commit hook. For stricter control, you’d use a custom lint rule or an extra tool like [`eslint-plugin-unicorn`](https://github.com/sindresorhus/eslint-plugin-unicorn) (which has some file naming rules).

---

If you want, I can generate a **full starter config folder** for you. Want a ready-to-copy zip? 🚀
