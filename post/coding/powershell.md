# Powershell

## Copy File to Clipboard

```powershell
gc .\some.ts | Set-Clipboard
```

```powershell
gc "C:\Full\Path\To\some.ts" | Set-Clipboard
```

where gc is alias for Get-Content