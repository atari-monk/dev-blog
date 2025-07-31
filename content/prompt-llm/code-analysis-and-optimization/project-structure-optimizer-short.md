### **Prompt: Project Structure Optimizer**  
**Input:**  
1. Current project tree (text).  
2. (Optional) File descriptions.  

**Output:** A reorganized tree adhering to:  
1. **Domain-Driven Folders** (`/auth`, `/payments`).  
2. **Layer Separation** (`/core`, `/interface`, `/infra`).  
3. **Flat Hierarchy** (max 3-4 levels deep).  

**Example (Short):**  
```plaintext
# Before  
/src  
├── utils.js  
├── auth.js  
└── PaymentForm.js  

# After  
/domains/auth/auth.js  
/domains/payments/PaymentForm.js  
/core/utils.js  
```  

**Key Rules:**  
- No "utils" or "misc" folders—use purposeful names.  
- Isolate shared code (`/core`), business logic (`/domains`), and UI (`/interface`).  

---  
