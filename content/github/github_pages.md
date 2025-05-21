# Github Pages

## Dependencies Installed

```bash
npm install gh-pages --save-dev
```

## Configuration Changes

* Added `homepage` to `package.json`:

```json
"homepage": "https://atari-monk.github.io/pong-game"
```

* Added deployment script to `package.json`:

```json
"scripts": {
  "deploy": "gh-pages -d build"
}
```

## Commands Executed

```bash
npm run deploy
```

## Notes

* A custom script is needed to:

  * Copy contents of `dist` to a `docs/` directory
  * Rename `index.html` to `demo.html` within `docs`
