## Refactoring Prompt (concise)

* Analyze the given code for usefulness.
* Evaluate if the code follows **KISS** (Keep It Simple, Stupid) and **DRY** (Don’t Repeat Yourself) principles.
* Propose changes that **improve code quality significantly** without breaking existing functionality.
* If no improvements are possible, **do not modify the code**.
* Ensure that **testing remains possible** after changes.
* Provide a **one-line commit message** summarizing the changes.

**Input:** Code base to analyze and refactor.

**Goal:** Maintain functionality, improve quality, readability, and maintainability.

## Refactoring Prompt (verbose)

**Objective**: Analyze and improve code quality while maintaining functionality

### Analysis Phase:
1. **Usefulness Assessment**: 
   - Does the code solve a meaningful problem?
   - Is the implementation appropriate for the stated purpose?

2. **Code Quality Evaluation**:
   - **KISS Principle**: Identify over-engineering, unnecessary complexity
   - **DRY Principle**: Detect code duplication and repetitive patterns
   - **Readability**: Check naming, structure, and clarity
   - **Maintainability**: Assess ease of modification and extension

3. **Testing Considerations**:
   - Preserve existing test interfaces
   - Ensure changes don't break testability
   - Consider if new tests would be beneficial

### Refactoring Rules:
- **Only refactor if** there are clear quality improvements
- **Preserve** all existing functionality and public APIs
- **Maintain or improve** test coverage and testability
- **Avoid** breaking changes unless critical for quality
- **Document** non-obvious design decisions in comments

### Output Format:
```
## Analysis Summary
[Brief assessment of current code quality]

## Proposed Changes
[Specific, actionable improvements]

## Commit Message
[One-line descriptive commit message]

## Refactored Code
[Complete implementation]
```

**Code base**: [paste code here]
