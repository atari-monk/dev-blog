
## Override last commit

Optionally with same message

```
git add . && git commit --amend -m "commit msg" && git push --force origin main  
```

## Remove last commit

```sh
git reset --hard HEAD~1
git push origin main --force
```
