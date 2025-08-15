## Building zippy-test

zippy-test is composed out of 3 library projects.
Powershell script to automate building of projects.
For debug:  

```powershell
# Build zippy-shared-lib
cd C:\Atari-Monk-Art\zippy-shared-lib
Remove-Item -Recurse -Force .\dist
pnpm run build --mode development

# Build fullscreen-canvas-vanilla
cd C:\Atari-Monk-Art\fullscreen-canvas-vanilla
Remove-Item -Recurse -Force .\dist
pnpm run build

# Build zippy
cd C:\Atari-Monk-Art\zippy
Remove-Item -Recurse -Force .\dist
pnpm run build

# Build zippy-test
cd C:\Atari-Monk-Art\zippy-test
Remove-Item -Recurse -Force .\dist
pnpm run build --mode development
```
