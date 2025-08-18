# TypeScript Configuration Documentation (`tsconfig.json`)

This configuration file sets up TypeScript compilation for an npm package project featuring a fullscreen canvas component. Below is the breakdown:

## Core Compiler Options
- **Target:** `ES2022` - Outputs modern JavaScript syntax
- **Class Fields:** Uses standard `define` semantics (`useDefineForClassFields: true`)
- **Libraries:** Includes ES2022 features, DOM types, and iterable DOM APIs

## Module System
- **Module Format:** `NodeNext` (Node.js native ES modules)
- **Resolution:** `NodeNext` (Node.js module resolution algorithm)
- **Syntax:** Strict module syntax (`verbatimModuleSyntax: true`)

## Output Configuration
- **Declaration Files:** Generates `.d.ts` files (`declaration: true`) with source maps
- **Source Maps:** Enabled for debugging
- **Directory Structure:**
  - Source: `./src`
  - Output: `./dist`

## Strict Type Checking
- All strict type checks enabled
- Additional safety features:
  - No unused locals/parameters
  - No fallthrough in switch cases
  - Strict side effect checks for imports

## File Inclusion
- Includes: All files in `src/`
- Excludes: `node_modules/` and `dist/`

This configuration optimizes for:
1. Modern JavaScript output
2. Strict type safety
3. Node.js/npm package compatibility
4. Maintainable declaration files for consumers