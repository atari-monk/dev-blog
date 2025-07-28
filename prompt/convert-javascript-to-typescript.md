# Prompt: Convert JavaScript to Modern TypeScript

Convert the following JavaScript code into **modern, idiomatic TypeScript** using best practices.

Where appropriate:
- Use ES6+ **classes**
- Add proper **type annotations**
- Use **access modifiers**: `public`, `private`, `protected`
- Apply **interfaces**, **union types**, **generics**, and other modern TypeScript features

## Rules:
- Target the latest TypeScript version (TS 5.x+)
- Assume `strictNullChecks: true` and `noImplicitAny: true`
- If a type is unclear, leave a comment like:  
  `// TODO: define type`
- Remove unused code or variables
- Small refactors are allowed if they improve clarity
- Use self documenting code from srp units that reads like a novel

## Output

Return a full, working `.ts` file, ready for integration into a TypeScript project.

> ✅ Prefer readability and maintainability over exact 1:1 transpilation
> ✅ Preserve functionality, this is a part of existing project we dont want to break

## Input

Paste your JavaScript code inside this block:
