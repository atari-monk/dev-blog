# Naming Conventions

## Basic Guidelines

- File extension: `.ps1`
- Verb-Noun structure using PascalCase:
  ```powershell
  Get-SystemInfo.ps1
  ```

## Recommended Practices

- Descriptive names:
  ```powershell
  Deploy-WebApplication.ps1
  ```

- Approved PowerShell verbs (Get, Set, New, Remove)

- Scope prefixes:
  ```powershell
  Contoso-DeployApp.ps1
  PROD-BackupDatabase.ps1
  ```

- Versioning formats:
  ```powershell
  MigrateUserData-v2.ps1
  GenerateReports-1.3.ps1
  ```

- ISO 8601 date format:
  ```powershell
  DailyReport-2023-11-15.ps1
  ```

## Example Scripts

```powershell
Install-CompanySoftware.ps1
Backup-SqlDatabase.ps1
AD-UserProvisioning.ps1
Azure-DeployResources.ps1
Cleanup-TempFiles.ps1
```