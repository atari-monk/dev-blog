## 🔄 Reset Repo (Full History Wipe)

Use this **once** to reset everything and push a fresh commit history:

- Remove .git folder

```bash
# Reinitialize git and add everything
git init
git add .
git commit -m "Initial commit"

# Add remote and force push to master (or main)
git remote add origin https://github.com/atari-monk/repository-name.git
git push -f origin master  
# or 'main' if your default branch is main
````

Or as a one-liner:

```bash
git init && git add . && git commit -m "Initial commit" && git remote add origin https://github.com/atari-monk/repository-name.git && git push -f origin master
```

---

### ⚠️ A few notes:

1. **Branch Name**: Double-check if your remote repo uses `master` or `main` (GitHub defaults to `main` now).
2. **Repository Already Exists**: This assumes the GitHub repo already exists. If not, create it first via the GitHub UI or CLI.
3. **Force Push Warning**: This will overwrite all history in the remote repo—make sure that's what you want.
4. **Quirk**: Click "Publish Branch" in VSCode—this should re-sync everything properly.
 
---
