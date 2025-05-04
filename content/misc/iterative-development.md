# Iterative Development

## Process Breakdown

1. **Specification/Plan**
   - Define:
     - What is being built
     - Why it's needed
     - How it will work
   - Document:
     - Requirements
     - Goals
     - Constraints
     - Implementation steps

2. **Test**
   - Validate key assumptions before full implementation
   - Methods:
     - Prototypes
     - Mockups
     - Small-scale experiments

3. **Implementation**
   - Develop with validated plan
   - Reduced unknowns from prior stages

4. **AI Enhancement**
   - Apply AI tools for:
     ```python
     # Code optimization
     def optimize_code(base_implementation):
         return ai_suggest_improvements(base_implementation)

     # Documentation generation
     generate_docs(code, format='markdown')
     ```
     - Efficiency automation
     - Logic refinement
     - Documentation assistance

## Workflow Variations

- **Agile Hybrid**
  ```
  while project_incomplete:
      plan → test → implement → ai_refine
  ```

- **AI-Assisted Planning**
  ```python
  initial_spec = generate_spec(prompt="Web auth service requirements")
  test_cases = suggest_test_scenarios(initial_spec)
  ```

- **Automated Testing Integration**
  ```bash
  pytest --ai-generate-tests --coverage
  ```