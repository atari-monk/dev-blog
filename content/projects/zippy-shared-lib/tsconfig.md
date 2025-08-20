# TypeScript Configuration Overview

This project uses TypeScript with a modern, strict configuration designed for library development with optimal compatibility and tooling support.

## Key Configuration Highlights

**Target Environment**: ES2022
- Generates JavaScript using the latest ECMAScript 2022 standards
- Ensures compatibility with modern browsers and Node.js versions

**Module System**: ESNext
- Uses the most recent ECMAScript module format
- Enables tree-shaking and optimal bundling

**Output**: Library Distribution
- Declaration files (`.d.ts`) are generated for type safety in consuming projects
- Source maps provided for debugging convenience
- Output directory: `./dist/`

**Strict Type Checking**: Enabled
- Full strict mode ensures maximum type safety
- Helps catch errors during development rather than runtime

**Compatibility Features**:
- ES module interoperability for mixed module environments
- DOM library included for web development support
- Library checking skipped for faster compilation

## Development Workflow

The configuration includes all files in the `src/` directory and produces optimized output ready for distribution as a shared library. The setup is ideal for projects requiring both type safety and modern JavaScript features.

This configuration balances development experience with production readiness, providing excellent tooling support while maintaining strict type checking standards.