# Reset repo history

```sh
cd C:\atari-monk\code\dev-blog
```
```sh
Remove-Item -Recurse -Force ".git" -ErrorAction SilentlyContinue
```
```sh
git init
```
```sh
git add .
```
```sh
git commit -m "Update $(Get-Date -Format 'yyyy-MM-dd HH:mm zzz')"
```
```sh
git remote add origin "https://github.com/atari-monk/dev-blog.git"
```
```sh
git push -u --force origin master
```
