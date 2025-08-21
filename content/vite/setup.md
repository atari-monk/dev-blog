# Vite

## Vite Cli

### Vite + TypeScript + React + pnpm

```bash
pnpm create vite@latest project-name --template react-ts
cd project-name
pnpm install
pnpm dev
```

### Vite + TypeScript + pnpm

```bash
pnpm create vite@latest project-name --template vanilla-ts
cd project-name
pnpm install
pnpm dev
```

## 🧹 Cleanup

### 🧹 React Template

* Cleared `App.css` and `index.css`.
* Updated `App.tsx`:

  ```tsx
  import "./App.css";

  function App() {
      return <></>;
  }

  export default App;
  ```

### 🧹 Css

* Updated `index.css` to [Empty Style](../css/style.md)
