To publish your scoped package (`@atari-monk/fullscreen-canvas`) to the npm registry using **pnpm**, follow these steps:

---

### ✅ **1. Ensure Your `package.json` is Correct**

Make sure you have at least the following fields in your `package.json`:

```json
{
  "name": "@atari-monk/fullscreen-canvas",
  "version": "1.0.0",
  "main": "dist/index.js",        // or whatever your entry file is
  "types": "dist/index.d.ts",     // if you're using TypeScript
  "files": ["dist"],              // only publish the necessary files
  "publishConfig": {
    "access": "public"
  }
}
```

> ⚠️ By default, scoped packages are private. The `"publishConfig": { "access": "public" }` is **required** to publish publicly.

---

### ✅ **2. Build Your Package (if needed)**

```sh
pnpm build
```

> This depends on your setup. Skip if you're not using a build step.

---

### ✅ **3. Login to npm (if not already)**

```sh
pnpm login
```

---

### ✅ **4. Publish the Package**

```sh
pnpm publish --access public
```

> You can omit `--access public` if it's already in your `publishConfig`.

---

### 🔁 Example Full Flow

```sh
pnpm login
pnpm build
pnpm publish
```

---

Let me know if your package is private or using a monorepo—those require different handling.
