# Commands

## Print paths

Prints paths in folder with /

```sh
Get-ChildItem -Recurse | ForEach-Object { $_.FullName -replace '\\','/' }
```