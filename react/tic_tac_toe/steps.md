# Steps

## Resources

- [Tutorial](https://react.dev/learn/tutorial-tic-tac-toe)

## Initialize project 

`create-react-app` tool is obsolete  

### Vite for fast, minimal setup

```sh
cd C:\atari-monk\code
```
```sh
npm create vite@latest tic-tac-toe-react-tutorial --template react
```
Options chosen: React, Javascript  

```sh
cd tic-tac-toe-react-tutorial
```
```sh
npm i
```
```sh
npm run dev
```

## Initial commit

- Remove default content
- Prettier config
- Init Repo, initial commit

## Copy Game files 

- copy files, test, style

## Publish

To test locally  

```
npm run build
```

and [serve](./../../javascript/tools/npm_serve_folder.md)  

To publish on github pages  

- add to package.json

```json
"scripts": {
  "build": "vite build",
  "build:gh": "vite build --base=/your-repo-name/"
}
```

- build and include it in commit, best in separate repo!
- [copy folder](./../../powershell/basics/commands.md)
- enable github pages on root