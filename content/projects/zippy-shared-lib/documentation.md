# zippy-shared-lib

Vite lib project established to communicate two component projects with common code.

## Notes

- The project uses Vite as a build tool to handle bundling, minification, and tree-shaking, which helps create an optimized, lightweight library. While a simple TypeScript project would work, Vite provides a more production-ready build process.

## version: "0.1.8":

### FrameContext

```typescript
export type FrameContext = {
    readonly ctx: CanvasRenderingContext2D;
    readonly width: number;
    readonly height: number;
    readonly deltaTime: number;
    readonly totalTime: number;
};
```

Type merging information for calculating frame in simple engine.  
CanvasRenderingContext2D is passed to render.  
Width and height may be used in render or game updates.  
deltaTime and totalTime might also be used in render and update methods.
It is shared by canvas and engine components.  
It's calculated in canvas and passed to engine.  

---

### EngineHook

```typescript
export interface EngineHook {
    frameTick(context: FrameContext): void;
}
```

Connector between canvas and engine components.
Canvas uses this interface to inject engine frameTick calculation into its render method also called frameTick.

---

### Exports

```ts
export type { FrameContext, EngineHook } from "./interfaces";
```

---

### Cli

Offen used commands

```bash
pnpm build --mode production
pnpm login
pnpm publish --access public
```

---

### Configs

Reference for configs used in this library project  

- vite.config.ts

```ts
import { defineConfig } from "vite";
import dts from "vite-plugin-dts";

export default defineConfig({
    build: {
        lib: {
            entry: "src/index.ts",
            name: "ZippySharedLib",
            fileName: (format) => `zippy-shared-lib.${format}.js`,
            formats: ["es", "umd"],
        },
        rollupOptions: {
            external: [],
            output: {
                globals: {},
            },
        },
    },
    plugins: [
        dts({
            insertTypesEntry: true,
        }),
    ],
});
```

- tsconfig.json

```json
{
    "compilerOptions": {
        "target": "ES2022",
        "module": "ESNext",
        "lib": ["ES2022", "DOM"],
        "moduleResolution": "bundler",
        "declaration": true,
        "declarationMap": true,
        "outDir": "./dist",
        "strict": true,
        "skipLibCheck": true,
        "esModuleInterop": true
    },
    "include": ["src"]
}
```

- package.json

```json
{
    "name": "zippy-shared-lib",
    "version": "0.1.8",
    "type": "module",
    "main": "./dist/zippy-shared-lib.umd.js",
    "module": "./dist/zippy-shared-lib.es.js",
    "types": "./dist/index.d.ts",
    "files": [
        "dist/"
    ],
    "exports": {
        ".": {
            "types": "./dist/index.d.ts",
            "import": "./dist/zippy-shared-lib.es.js",
            "require": "./dist/zippy-shared-lib.umd.js"
        }
    },
    "scripts": {
        "dev": "vite",
        "build": "tsc && vite build",
        "preview": "vite preview"
    },
    "devDependencies": {
        "typescript": "~5.8.3",
        "vite": "^7.0.4",
        "vite-plugin-dts": "^3.7.1"
    }
}
```

---