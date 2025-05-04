# Vite for fast, minimal setup

## New Project

```sh
cd C:\atari-monk\code
```
```sh
npm create vite@latest tic-tac-toe-react-tutorial --template react
```
Example options: React, Javascript.

```sh
cd tic-tac-toe-react-tutorial
```
```sh
npm i
```
```sh
npm run dev
```

## Publish on github pages

- add to package.json

```json
"scripts": {
  "build": "vite build",
  "build:gh": "vite build --base=/your-repo-name/"
}
```

- [copy build](./../../powershell/basics/commands.md) to new page repo root, commit
- with github web page, enable github pages on root