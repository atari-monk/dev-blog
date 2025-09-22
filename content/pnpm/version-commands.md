Here's a comprehensive guide to pnpm version commands and Git integrations:

## Basic Version Management Commands

```bash
# View current version
pnpm version

# Show version of a specific package
pnpm version <package-name>

# Check for outdated packages
pnpm outdated

# Update all packages to latest
pnpm update

# Update specific package
pnpm update <package-name>

# Update to specific version
pnpm update <package-name>@<version>
```

## Version Bumping Commands

```bash
# Patch version (1.0.0 → 1.0.1)
pnpm version patch

# Minor version (1.0.0 → 1.1.0)
pnpm version minor

# Major version (1.0.0 → 2.0.0)
pnpm version major

# Pre-release versions
pnpm version prerelease
pnpm version prepatch
pnpm version preminor
pnpm version premajor

# Specific version
pnpm version 2.1.0

# Version with pre-release tag
pnpm version 2.1.0-beta.1
```

## Git Integration Commands

```bash
# Install packages and commit lockfile automatically
pnpm install --git-checks

# Add all changes and commit with message
pnpm exec git add . && pnpm exec git commit -m "chore: update dependencies"

# Create version tag after bumping
pnpm version patch --tag-version-prefix="v"

# Push version changes and tags
pnpm exec git push && pnpm exec git push --tags
```

## Advanced Version Management

```bash
# Interactive update
pnpm update -i

# Update only in specific scope
pnpm update --filter <package-pattern>

# Update dev dependencies only
pnpm update --dev

# Update production dependencies only
pnpm update --prod

# Dry run (see what would be updated)
pnpm update --dry-run
```

## Workspace Version Management (Monorepo)

```bash
# Update versions across all workspace packages
pnpm -r update

# Update specific package in all workspaces
pnpm -r update <package-name>

# Version all packages consistently
pnpm version major --recursive

# Update packages with interactive selection
pnpm update -r -i
```

## Git Hooks Integration

Add to your `package.json`:

```json
{
  "scripts": {
    "preversion": "npm test",
    "version": "npm run build && git add -A dist",
    "postversion": "git push && git push --tags"
  }
}
```

Or use with pnpm:

```bash
# Run tests before versioning
pnpm run test && pnpm version patch

# Build and commit built files
pnpm run build && pnpm exec git add dist/ && pnpm version minor
```

## Version Policy Configuration

Create `.npmrc` for version policies:

```ini
# Prefer exact versions
save-exact = true

# Use latest tag for updates
save-prefix = ^

# Or use caret for minor updates
# save-prefix = ^

# Or tilde for patch updates
# save-prefix = ~
```

## Common Git + pnpm Workflows

### 1. Dependency Update Workflow
```bash
# Update dependencies
pnpm update

# Review changes
pnpm exec git diff

# Add lockfile changes
pnpm exec git add pnpm-lock.yaml

# Commit with conventional message
pnpm exec git commit -m "chore(deps): update dependencies"
```

### 2. Version Release Workflow
```bash
# Bump version
pnpm version patch --message "chore(release): v%s"

# Build project
pnpm run build

# Add built files
pnpm exec git add dist/

# Commit build files
pnpm exec git commit -m "chore(build): update built assets"

# Push everything including tags
pnpm exec git push && pnpm exec git push --tags
```

### 3. Monorepo Release Workflow
```bash
# Update all packages
pnpm -r update

# Version all packages
pnpm version minor --recursive --message "chore(release): v%s"

# Build all packages
pnpm -r run build

# Commit and push
pnpm exec git add . && pnpm exec git commit -m "chore(release): version bump"
pnpm exec git push && pnpm exec git push --tags
```

## Useful Aliases

Add to your `.zshrc` or `.bashrc`:

```bash
# pnpm version with git integration
alias pv='pnpm version'
alias pvg='pnpm version && git add . && git commit -m "chore(release): version bump"'
alias pvpg='pnpm version patch && git add . && git commit -m "chore(release): patch version"'

# pnpm update with git
alias pu='pnpm update'
alias pug='pnpm update && git add pnpm-lock.yaml && git commit -m "chore(deps): update packages"'
```

These commands and workflows will help you manage versions effectively while maintaining good Git practices with pnpm!