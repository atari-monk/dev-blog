**Instructions:**  
Convert the given markdown into a clean developer-focused blog post with this structure:

# Title - 2 words based on content

Concise body preserving all technical details:  
- Code snippets  
- Commands  
- Configuration  
- Key explanations

No non-technical fluff or commentary

---

**Rules:**  
1. **Audience:** Developers (assume technical knowledge)  
2. **Style:**  
   - Minimalist markdown (no comments in code blocks)  
   - No "welcome"/conclusion paragraphs  
   - Preserve all actionable technical content  
3. **Formatting:**  
   - Use ` ``` ` fences for ALL code  
   - Headers only for major sections (H2+)  
   - Bullet points for steps/lists  

**Example Output:**  

# Setting Up Next.js with TypeScript

- Install dependencies:  
  ```bash
  npm install next react react-dom typescript @types/react @types/node
  ```
- Required `tsconfig.json`:  
  ```json
  {
    "compilerOptions": {
      "strict": true
    }
  }
  ```

**Content to work on:**  
$files$