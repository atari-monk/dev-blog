# Clear repo

Clear local and github origin  
Removes all files and history !  

```sh
m .git -r -fo
git init
git remote add origin https://github.com/atari-monk/tic-tac-toe-react-tutorial-page.git
git add .
git commit -m "Page Build"
git push -f origin master
```

If local repo dosent get sync with origin  

```sh
git branch --set-upstream-to=origin/master master
```