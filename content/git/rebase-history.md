# Rebase History

## Rewriting Entire Git History

Use:
```bash
git rebase -i --root
```

This rebases from the very first commit in the repository — useful when rewriting the entire commit history.

## Editing Commit Messages

You’ll see something like:
```
pick 1e97abf Initialize project using Create React App  
pick 6aef733 remove template content  
pick 0a1b463 game
```

Change all `pick` entries to `reword`:
```
reword 1e97abf Initialize project using Create React App  
reword 6aef733 remove template content  
reword 0a1b463 game
```

Git will then prompt you to edit each message one-by-one.

## Saving in GNU Nano

When you're in the editor:

1. Press `Ctrl + O` to save  
2. Press `Enter` to confirm  
3. Press `Ctrl + X` to exit

For each commit message prompt:

- Edit as needed  
- Press `Ctrl + O`, `Enter`, `Ctrl + X` to save and proceed

## Force Pushing Updated History

After completing the rebase, force-push the changes:

```bash
git push --force
```

Or with explicit branch:

```bash
git push origin master --force
```

### ⚠ Caution

- This overwrites the remote history  
- Safe only when working solo or with team agreement

Once pushed, VS Code should stop prompting to sync changes.