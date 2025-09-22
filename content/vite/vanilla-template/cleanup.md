## 🧹 Cleanup Vite Vanilla Template

```sh
fullscreen-canvas-vanilla/
├── public/
│   └── vite.svg (delete)
├── src/
│   ├── counter.ts (delete)
│   ├── main.ts (clean)
│   ├── style.css (clean)
│   ├── typescript.svg (delete)
│   └── vite-env.d.ts
├── .gitignore
├── index.html
├── package.json
├── pnpm-lock.yaml
└── tsconfig.json
```

* `main.ts`:

```ts
import './style.css'

```

* `style.css`:
    - [Empty Style](../../css/empty-style.md)
