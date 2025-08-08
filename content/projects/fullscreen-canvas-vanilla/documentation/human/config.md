# Config Documentation

## Functionality

- This is config for library with ui component intended to use as npm package in other projects.  
Project was set with vite cli with pnpm.  
Build switched to tsc.

## Config for Refferance

### package.json

```json
{
    "name": "fullscreen-canvas-vanilla",
    "version": "0.0.4",
    "type": "module",
    "main": "./dist/index.js",
    "types": "./dist/index.d.ts",
    "files": [
        "dist"
    ],
    "exports": {
        ".": {
            "types": "./dist/index.d.ts",
            "import": "./dist/index.js"
        }
    },
    "scripts": {
        "build": "tsc",
        "dev": "tsc --watch",
        "prepublishOnly": "npm run build"
    },
    "devDependencies": {
        "typescript": "~5.8.3",
        "vite": "^7.0.4"
    },
    "dependencies": {
        "zippy-shared-lib": "^0.1.8"
    }
}
```

### tsconfig.json

```json
{
    "compilerOptions": {
        "target": "ES2022",
        "useDefineForClassFields": true,
        "lib": ["ES2022", "DOM", "DOM.Iterable"],
        "skipLibCheck": true,

        /* Module settings */
        "module": "NodeNext", // Changed from ESNext
        "moduleResolution": "NodeNext", // Changed from bundler
        "verbatimModuleSyntax": true,

        /* Output */
        "declaration": true,
        "declarationMap": true,
        "sourceMap": true,
        "outDir": "./dist",
        "rootDir": "./src",

        /* Linting */
        "strict": true,
        "noUnusedLocals": true,
        "noUnusedParameters": true,
        "erasableSyntaxOnly": false,
        "noFallthroughCasesInSwitch": true,
        "noUncheckedSideEffectImports": true
    },
    "include": ["src"],
    "exclude": ["node_modules", "dist"]
}
```