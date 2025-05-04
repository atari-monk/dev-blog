# Folder Listing

## Command Prompt

```cmd
dir "subfolder_name"
```

List only files:

```cmd
dir "scripts\*" /A-D
```

List only directories:

```cmd
dir "scripts\" /AD
```

## PowerShell

```powershell
Get-ChildItem -Path .\subfolder_name
```

List only files:

```powershell
Get-ChildItem -Path .\scripts -File
```

List only directories:

```powershell
Get-ChildItem -Path .\scripts -Directory
```

Get clean name output:

```powershell
(Get-ChildItem -Path .\scripts).Name
```

## Quick Reference

CMD:

```cmd
dir scripts
```

PowerShell:

```powershell
ls scripts
```