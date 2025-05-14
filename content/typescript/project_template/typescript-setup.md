# TypeScript Setup

## Initialize Project

```sh
mkdir my-ts-project && cd my-ts-project
npm init -y
```

## Install Dependencies

```sh
npm install -D typescript ts-node jest ts-jest @types/jest vite
```

## Configure TypeScript

Generate config:
```sh
npx tsc --init
```

Modified `tsconfig.json`:
```json
{
  "compilerOptions": {
    "target": "ESNext",
    "module": "ESNext",
    "moduleResolution": "Node",
    "outDir": "dist",
    "rootDir": "libs",
    "strict": true,
    "esModuleInterop": true
  },
  "include": ["libs/**/*"]
}
```

## Create Structure

```sh
mkdir libs tests client docs docs_pl
New-Item libs/battleship/index.ts -ItemType File
New-Item tests/index.test.ts -ItemType File
New-Item client/index.html -ItemType File
New-Item client/main.ts -ItemType File
```

```
my-ts-project
│── libs/
│   └── battleship/
│       └── index.ts
│── tests/
│   └── index.test.ts
│── client/
│   ├── index.html
│   └── main.ts
│── docs/
│── tsconfig.json
│── package.json
│── jest.config.js
```

## Library Code

`libs/battleship/index.ts`:
```ts
export function greet(name: string): string {
  return `Hello, ${name}!`;
}
```

## Tests

`tests/index.test.ts`:
```ts
import { greet } from "../libs/battleship/index";

test("greet function", () => {
  expect(greet("Alice")).toBe("Hello, Alice!");
});
```

Run tests:
```sh
npx jest
```

## Client Setup

`client/index.html`:
```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Test TypeScript</title>
</head>
<body>
  <script type="module" src="./main.ts"></script>
</body>
</html>
```

`client/main.ts`:
```ts
import { greet } from "../libs/battleship/index";
console.log(greet("World"));
```

## Run Scripts

`package.json` scripts:
```json
"scripts": {
  "build": "tsc",
  "test": "jest",
  "dev": "vite client"
}
```

Start client:
```sh
npm run dev
```

## Jest Config

`jest.config.js`:
```js
module.exports = {
  preset: "ts-jest",
  testEnvironment: "node",
  transform: {
    "^.+\\.ts$": "ts-jest",
  },
  extensionsToTreatAsEsm: [".ts"],
};
```