# Vite CLI

## New Project

Just write and run script

```powershell
param([string]$name)

npx create-vite@latest $name --template react-ts
cd $name
code .
npm install
npm run dev
```

or

```sh
npx create-vite@latest repo-name --template react-ts && cd repo-name && code . && npm i && npm run dev
```

or 

```sh
npx create-vite@latest repo-name --template react-ts
```
Shows selection menu

```sh
cd repo-name
```
```sh
code .
```
```sh
npm i
```
```sh
npm run dev
```

## Build

```sh
vite build
```

## Tip for publishing on github pages

```sh
vite build --base=/your-repo-name/
```

## package.json scripts

```json
"scripts": {
  "build": "vite build",
  "build:gh": "vite build --base=/your-repo-name/"
}
```