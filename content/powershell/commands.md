# Commands

## Print paths

Prints paths in folder with /

```sh
Get-ChildItem -Recurse | ForEach-Object { $_.FullName -replace '\\','/' }
```

## Print file

```sh
Get-Content .\project.json
```

## Open file

```sh
notepad .\project.json
```

```sh
code .\project.json
```

## Open poweshell profile

```sh
notepad $PROFILE
```

```sh
code $PROFILE
```

## Create poweshell profile

```sh
if (!(Test-Path $PROFILE)) { New-Item -Type File -Path $PROFILE -Force }
```

## Copy file

```sh
Copy-Item -Path "C:\Source\file.txt" -Destination "C:\Destination\"
```

## Check web proj version

```sh
(Get-Content package.json -Raw | ConvertFrom-Json).version
```

## Alias for script

Put in profile

```powershell
Set-Alias alias-name "C:\Path\To\Your\Script\script.ps1"
```