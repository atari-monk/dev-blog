# Package Configuration Documentation (`package.json`)

## Project Overview
This is an npm package providing a fullscreen canvas component built with vanilla JavaScript/TypeScript. The package is designed to be imported as an ES module (`"type": "module"`).

## Key Configuration
- **Entry Points**:
  - Main: `./dist/index.js` (compiled JavaScript)
  - Types: `./dist/index.d.ts` (TypeScript declarations)
- **Exports**:
  - Provides both type definitions and JavaScript implementation through the package exports:
    ```json
    "exports": {
        ".": {
            "types": "./dist/index.d.ts",
            "import": "./dist/index.js"
        }
    }
    ```
  - This enables type-aware imports in TypeScript projects
- **Build System**:
  - Uses TypeScript compiler (`tsc`) for building
  - Includes CSS files in the distribution
- **Dependencies**:
  - Requires `zippy-shared-lib` as a runtime dependency
  - Uses `typescript` and `vite` for development

## Build Commands
- `npm run build`: Compiles TypeScript and copies CSS to dist
- `npm run dev`: Development watch mode
- `prepublishOnly`: Automatic build before publishing

## Distribution
Only the `dist` folder is included in the published package (as specified in `files` array).

## Version
Current package version: 0.0.9