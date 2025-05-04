# Npm Serve Folder

To serve a folder using an npm package, the most common and lightweight way is to use the [`serve`](https://www.npmjs.com/package/serve) package.

### Steps:

1. **Install `serve` globally (or locally):**

```bash
npm install -g serve
```

Or if you prefer to use it locally in a project:

```bash
npm install --save-dev serve
```

2. **Run the command to serve a folder:**

```bash
serve path/to/your-folder
```

Example:

```bash
serve dist
```

This will serve the contents of the `dist` folder at `http://localhost:3000` by default.

---

### Optional: Add a script to `package.json`

```json
"scripts": {
  "start": "serve dist"
}
```

Then run:

```bash
npm run start
```

Would you like it to serve with custom port, headers, or support for SPA routing (e.g., for React or Vue)?
