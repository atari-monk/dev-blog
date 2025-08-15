# PowerShell Command Reference

## 1. **Copying Files**

Copy a file from one folder to another:

```powershell
Copy-Item -Path "C:\Source\file.txt" -Destination "C:\Destination\"
```

## 2. **Opening a File**

* To display contents in PowerShell:

```powershell
Get-Content .\project.json
```

* To open in Notepad:

```powershell
notepad .\project.json
```

## 3. **Incrementing Patch Version in `package.json`**

```powershell
$json = Get-Content package.json -Raw | ConvertFrom-Json
$versionParts = $json.version -split '\.'
$versionParts[2] = [int]$versionParts[2] + 1
$json.version = "$($versionParts[0]).$($versionParts[1]).$($versionParts[2])"
$json | ConvertTo-Json -Compress | Set-Content package.json -Force
```

**Explanation:**

* Reads the `package.json`.
* Splits the version into major.minor.patch.
* Increments the patch number.
* Writes the updated JSON back to the file.

## 4. **Checking Version**

```powershell
(Get-Content package.json -Raw | ConvertFrom-Json).version
```

## 5. **Creating an Alias for a Script**

* Open PowerShell profile:

```powershell
notepad $PROFILE
```

* Add an alias to run a script easily:

```powershell
Set-Alias incrementVersion "C:\Path\To\Your\Script\Increment-Version.ps1"
```

* Restart PowerShell for changes to take effect.

## 6. **Creating a PowerShell Profile if Missing**

```powershell
if (!(Test-Path $PROFILE)) { New-Item -Type File -Path $PROFILE -Force }
```

---

If you want, I can also make a **fully formatted `.ps1` script** that includes all these snippets as ready-to-use commands with comments for learning/reference. That way, you could just open it and copy commands whenever needed.

Do you want me to do that?
