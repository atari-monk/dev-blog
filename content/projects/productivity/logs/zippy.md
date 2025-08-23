## 2025-08-21

**Time:** 1h

- Prepare documentation for zippy-shared-lib


## 2025-08-20

**Time:** 2h15m

- Documentation for config files
- Its quite hard to document configs and in a consistent way
- Merge zippy-test doc to this doc, no need for separete doc
- Also zippy-shared-lib dosent need to have separete doc, merging


## 2025-08-19

**Time:** 2h30m

- Documentation
- Refactored script of producting documentation, its simple now
- Updated code documentation files
- Add usage doc


## 2025-08-12

**Time:** 4h

- Zippy-test
- Made it run after component have been changed
- There is some bug manifesting as weird behavior and crash
- Turned out canvas resizer was looping on itself
- This was imposible to debug in original project, becouse of minified libs that scramble code and make it unreadable
- Monorepo with clone of code of each component was created and build for development, this is better for debuging


## 2025-08-11

**Time:** 1h

- Documentation with refactoring


## 2025-08-10

**Time:** 2h

- Documentation with refactoring


## 2025-08-09

**Time:** 3h10m

- Documentation with refactoring


## 2025-08-08

**Time:** 1h 10m

- Documentation with refactoring


## 2025-08-07

**Time:** 30m

- Fix this file to comply with new format


## 2025-08-06

**Time:** 1h50m

- zippy-shared-lib
- Rewiewing, i see, i pretty much wasted 16 hours. I am not sure why this happened. After 3 project with simple game engine, i wanted to optimize them with prompts, document what it is. I had 2 components, canvas and engine. I comunicated them with interface in shared lib. Extracted two shared classes. I was optimizing them with prompts. Events are handled in components, so no need for centralizing it. Wrappers over browser api is just pointless and insane. Classes were removed. I guess i was procrastinating and wanted prompt automation to much. Only thing out of this is scripts for prompting, but it may turn out to be not that usefull. This gives me thouth that a lot of time, best code is removed one. Need clear, measured goals.
- Prepare stable version
- Documentation,
- Fix git history (reset history, 'Initial commit')
- Publish npm package


## 2025-08-05

**Time:** 4h

- zippy-shared-lib
- Made code compile
- Script tool for prompting
- Refactoring with 9 prompts
- Removed 95 % of lib after realizing it was pointless wrappers on browser utils
- zippy
- Update after removed 95% of shared lib


## 2025-08-04

**Time:** 7h20m

- zippy-shared-lib
- Cli commands with args for prompt generation
- Refactored prompt script to use file for text data
- Refactoring with maintenance prompt, to point where code is not getting better
- Refactoring with SOLID checker prompt, went from 2 files to 20
- Script with 9 maintanace prompts


## 2025-08-03

**Time:** 1h40m

- zippy-shared-lib
- Fix bugs form AI
- Scripts to support prompts generation


## 2025-08-02

**Time:** 2h50m

- Optimizing zippy-shared-lib with maintanace prompts
- Zippy-test is a page to test component integration
- zippy-shared-lib, fullscreen-canvas-vanilla, zippy-game-engine
- This is needed to run any project with zippy-game-engine


## 2025-08-01

**Time:** 4h

- zippy-shared-lib
- Lib project with shared types
- Initialized project
- config - types in exports prop required
- Published to npm
- Installed 'zippy-shared-lib' to 'zippy'


## 2025-07-22

**Time:** 3h20m

- Project structure
- Initial setup, vite ts with pnpm
- Converted day-game\dev-tool game-engine code to typescript
- Tested on cross lines scene
- Published npm package
- Cloned Scenelet project and named it as zippy-test
- Linked local pnpm package, with file:../zippy