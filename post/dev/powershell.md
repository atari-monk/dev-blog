# Powershell

## Copy File to Clipboard

```powershell
gc .\some.ts | Set-Clipboard
```

```powershell
gc "C:\Full\Path\To\some.ts" | Set-Clipboard
```

where gc is alias for Get-Content

## Override last commit

Optionally with same message

```
git add . && git commit --amend -m "commit msg" && git push --force origin main  
```