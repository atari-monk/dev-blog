# `zippy-shared-lib` - v0.1.9

A shared library package built with TypeScript and Vite.

## Package Details
- **Name:** `zippy-shared-lib`
- **Version:** `0.1.9`
- **Description:** A shared library package built with TypeScript and Vite.
- **Type:** `module` (ES Modules)

## Distribution
- **Entry Point (CommonJS):** `./dist/zippy-shared-lib.umd.js`
- **Module Entry Point:** `./dist/zippy-shared-lib.es.js`
- **Type Definitions:** `./dist/index.d.ts` (indicates a TypeScript library)
- **Included Files:** The `files` array specifies which directories are published to npm. This package includes: `dist/`.

## Exports (Module API)
The package exposes its public API through the following entry points:
```json
{
  ".": {
    "types": "./dist/index.d.ts",
    "import": "./dist/zippy-shared-lib.es.js",
    "require": "./dist/zippy-shared-lib.umd.js"
  }
}
```

## Scripts
| Script | Purpose |
| :--- | :--- |
| `dev` | Starts the Vite development server for testing and development |
| `build` | Compiles TypeScript code and builds the production bundle using Vite |
| `preview` | Previews the production build locally using Vite's preview server |

## Dependencies
### Development Dependencies
These packages are only needed for development and building:
- `typescript@~5.8.3`
- `vite@^7.0.4`
- `vite-plugin-dts@^3.7.1`

## Package Overview
This is a TypeScript library package configured for npm distribution with dual module format support (ES Modules and UMD/CommonJS). The package uses Vite as its build system with TypeScript compilation and includes `vite-plugin-dts` for automatic generation of TypeScript declaration files. The build process produces optimized bundles for both modern ES modules and legacy CommonJS environments, making it suitable for consumption in various JavaScript environments.