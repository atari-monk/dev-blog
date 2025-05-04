# Commands

## Delete folder 

```sh
Remove-Item -Path "C:\path\to\folder" -Recurse -Force
```

```sh
(Get-Item "C:\path\to\folder").Delete($true)
```

```sh
rm "C:\path\to\folder" -r -fo
```

## Copy folder to other

```powershell
Copy-Item -Path "C:\Source\*" -Destination "C:\Target" -Recurse
```

```powershell
cp C:\Source\* C:\Target -Recurse
```

* `cp` is an alias for `Copy-Item`.
* `*` ensures only the contents are copied, not the folder itself.
* `-Recurse` ensures all subfolders and files are included.
Would you like to include hidden/system files too?
