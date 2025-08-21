Perfect! Here’s a fully commented PowerShell script that consolidates all the commands we discussed. You can save this as something like `PowerShell-Commands.ps1` and run or reference it anytime.

```powershell
<#
    PowerShell Commands Reference Script
    ====================================
    This script consolidates common PowerShell commands for:
    - Copying files
    - Opening files
    - Incrementing package.json version
    - Setting aliases/functions
    - Profile management
#>

# --------------------------------------------------
# 1. Copying Files
# Copy a file from one folder to another
# Example: Copy C:\Source\file.txt to C:\Destination\
# --------------------------------------------------
Copy-Item -Path "C:\Source\file.txt" -Destination "C:\Destination\"


# --------------------------------------------------
# 2. Opening a File
# --------------------------------------------------
# Display contents in PowerShell
Get-Content .\project.json

# Open file in Notepad
notepad .\project.json


# --------------------------------------------------
# 3. Increment Patch Version in package.json
# --------------------------------------------------
$json = Get-Content package.json -Raw | ConvertFrom-Json
$versionParts = $json.version -split '\.'
$versionParts[2] = [int]$versionParts[2] + 1
$json.version = "$($versionParts[0]).$($versionParts[1]).$($versionParts[2])"
$json | ConvertTo-Json -Compress | Set-Content package.json -Force

# Check the new version
(Get-Content package.json -Raw | ConvertFrom-Json).version


# --------------------------------------------------
# 4. PowerShell Profile Management
# --------------------------------------------------
# Open your PowerShell profile to edit
notepad $PROFILE

# Create profile if it doesn't exist
if (!(Test-Path $PROFILE)) { New-Item -Type File -Path $PROFILE -Force }


# --------------------------------------------------
# 5. Creating an Alias for a Script
# Example: create alias to run Increment-Version.ps1 easily
# --------------------------------------------------
# Add this to your profile:
# Set-Alias incrementVersion "C:\Path\To\Your\Script\Increment-Version.ps1"
# Then restart PowerShell to use the alias


# --------------------------------------------------
# 6. Extra Tips
# --------------------------------------------------
# - Make sure paths are correct for Copy-Item and aliases
# - Use -Force if needed to overwrite files
# - Use -Raw with Get-Content when reading JSON or multiline files
```

---

If you like, I can also make a **version with ready-to-run functions** so that you can just call `Increment-Version` and `Copy-File` like custom commands, without manually editing paths each time.

Do you want me to do that next?
