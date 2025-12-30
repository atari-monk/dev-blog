# Powershell

## Copy File to Clipboard

```powershell
gc .\some.ts | Set-Clipboard
```

```powershell
gc "C:\Full\Path\To\some.ts" | Set-Clipboard
```

where gc is alias for Get-Content

## Lowercase

```powershell
"Some String".ToLower()
```

```powershell
"Some String".ToLower().Replace(" ", "-");
```

```powershell
(Read-Host "Enter a string").ToLower()
```

## Open files

projects logs

- today-current
- today-log
- log
- plan

```powershell
code "C:/Atari-Monk/project/dev-blog/post/projects/logs/2025/11/today-current.json"
```

```sh
Get-Content "C:/Atari-Monk/project/dev-blog/post/projects/logs/2025/11/today-current.json"
```
