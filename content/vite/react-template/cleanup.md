## 🧹 Cleanup Vite React Template

```sh
/
├── public/
│   └── vite.svg (delete)
├── src/
│   ├── assets/
│   │   └── react.svg (delete)
│   ├── App.css (empty)
│   ├── App.tsx (replace)
│   ├── index.css (replace)
│   ├── main.tsx
│   └── vite-env.d.ts
├── .gitignore
├── eslint.config.js
├── index.html
├── package.json
├── pnpm-lock.yaml
├── README.md (replace)
├── tsconfig.app.json
├── tsconfig.json
├── tsconfig.node.json
└── vite.config.ts
```

* `App.tsx`:

```tsx
import "./App.css";

function App() {
    return <></>;
}

export default App;
```

* `index.css`:
    - [Empty Style](../../css/empty-style.md)
