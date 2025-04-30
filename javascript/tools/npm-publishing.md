# NPM Publishing

## Build and Publish
- Run `npm install` to install dependencies
- Run `npm run build` to generate `dist/`
- Run `npm login` to authenticate
- Run `npm publish` to deploy

Install published package:
```
npm install event-emitter
```

## Common Errors

### Package Name Conflict
- Check name availability:
  ```
  npm info event-emitter
  ```
- For taken names, use scoped naming in `package.json`:
  ```json
  {
    "name": "@your-username/event-emitter"
  }
  ```

### Scoped Package Access
Publish with public access flag:
```
npm publish --access public
```