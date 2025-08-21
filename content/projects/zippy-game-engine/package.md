# `zippy-game-engine` - v1.0.6

A lightweight game engine for web games

## Package Details
- **Name:** `zippy-game-engine`
- **Version:** `1.0.6`
- **Description:** A lightweight game engine for web games
- **License:** MIT
- **Type:** `module`

## Distribution
- **Entry Point (CommonJS):** `./dist/index.js`
- **Type Definitions:** `./dist/index.d.ts`
- **Included Files:** The `[files]` array specifies which directories are published to npm. This package includes: `dist`.

## Exports (Module API)
The package exposes its public API through the following entry points:
```json
{
  ".": {
    "types": "./dist/index.d.ts",
    "import": "./dist/index.js"
  }
}
```

## Scripts
| Script | Purpose |
| :--- | :--- |
| `build` | Compiles TypeScript source code to JavaScript |
| `dev` | Compiles TypeScript in watch mode for development |
| `prepublishOnly` | Automatically builds the package before publishing to npm |

## Dependencies
### Runtime Dependencies
These packages are required for this library to run:
- `zippy-shared-lib@^0.1.7`

### Development Dependencies
These packages are only needed for development and building:
- `typescript@~5.8.3`
- `vite@^7.0.4`

## Keywords
game, engine, web

This package is a TypeScript library configured for distribution as an npm package.