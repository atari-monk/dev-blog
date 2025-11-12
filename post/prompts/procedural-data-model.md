## **Procedural Data Model Prompt**

> Analyze the provided module file and construct a **procedural-style data model** for it.
>
> **Instructions:**
>
> 1. Identify the **core entities** or “things” represented in the module.
> 2. For each entity, define a **struct** containing **only the necessary data fields**. Avoid including functions or hidden state.
> 3. Identify the **operations/functions** that act on each struct:
>
>    * Each function should be **single-purpose, deterministic, and testable**.
>    * Input and output must be **explicit**; no hidden side effects.
> 4. Suggest **function signatures** for these operations (no implementation required).
> 5. Ensure the design adheres to **KISS** (keep it simple, readable, flat) and **DRY** (avoid redundant data or repeated patterns).
>
> **Output format (C-style example):**
>
> ```c
> typedef struct {
>     // data fields here
> } EntityName;
>
> // Function prototypes
> EntityName Operation1(EntityName entity, ...);
> EntityName Operation2(EntityName entity, ...);
> ```
>
> Only include the **data model and function signatures**, not full implementation.

---

> Analyze the given module file and generate a **procedural-style data model**. Identify the core entities and define a **struct** for each containing only the necessary data. List the **function signatures** for operations on these structs, ensuring each is single-purpose, deterministic, and explicitly inputs/outputs data. Follow **KISS** (simple, flat, readable) and **DRY** (no redundant data or repeated patterns) principles. Output only the **struct definitions and function prototypes**, no implementation.
