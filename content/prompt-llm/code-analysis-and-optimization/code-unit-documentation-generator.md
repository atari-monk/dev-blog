**Name: Code Unit Documentation Generator**  
**Purpose/Goal:** Generate complete documentation for a given code unit including functionality, dependencies, parameters, and usage.  
**Input Data:**  
- Raw code file (any language)  
- Optional: Specific documentation requirements (e.g., focus on public APIs, include examples)  
**Constraints/Requirements:**  
- Must analyze code structure automatically  
- Identify and document all key components:  
  * Functions/methods  
  * Parameters/inputs  
  * Return values/outputs  
  * Dependencies (internal/external)  
  * Usage examples  
- Maintain consistent formatting  
**Task/Action:**  
1. Parse the input code file to identify:  
   - All functions/methods with their signatures  
   - Input parameters and types  
   - Return values and types  
   - Called dependencies (internal functions and external libraries)  
   - Any special constraints or exceptions  
2. For each function/method:  
   - Generate clear description of functionality  
   - List all parameters with types and purposes  
   - Specify return value with type and meaning  
   - Note any dependencies called  
   - Include usage example if possible  
3. Output in standardized markdown format  

**Expected Output/Format:**  
```markdown
# [File Name] Documentation

## Dependencies
- External: [list of imported libraries/packages]
- Internal: [list of internal dependencies]

## Functions

### [Function Name]
**Description:** [Concise functionality explanation]  
**Parameters:**  
- `param1` (type): [description]  
- `param2` (type): [description]  
**Returns:**  
(type): [return value description]  
**Dependencies:**  
- Calls: [list of called functions]  
- Uses: [list of used libraries]  
**Example:**  
```[language]
[example usage code]
```

[Repeat for each function]
```

**Output Requirements:**  
- Complete documentation covering all public functions/methods  
- Clear parameter and return value documentation  
- Explicit dependency tracking  
- No code analysis commentary - only final documentation  
- Consistent markdown formatting  
