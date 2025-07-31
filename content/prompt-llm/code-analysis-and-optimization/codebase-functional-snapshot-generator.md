### **Name: Codebase Functional Snapshot Generator**  
**Purpose:** Create instant orientation documents that explain what each file/module contributes to the codebase.  

### **Input:**  
- Entire codebase directory (or selected files)  
- Optional: Custom focus areas (e.g., "Highlight integration points")  

### **Output Format:**  
```markdown
# [Codebase Name] Functional Snapshot  

## [File/Module 1 Path]  
**Role:** [1-2 sentences about the file’s purpose]  
**Key Capabilities:**  
- Provides [X] to [Y system]  
- Handles [specific responsibility]  
- Exposes [key functions/data] for [use case]  

**Integration Points:**  
- Depends on: [external/internal dependencies]  
- Used by: [downstream dependents if detectable]  

---  

## [File/Module 2 Path]  
**Role:** [...]  
[...]  
```  

### **Key Differences from Original:**  
1. **Focus on "what it does"** over technical minutiae (no parameter lists).  
2. **Aggregate by functional role** (e.g., "Authentication Handler" vs. "auth_utils.py").  
3. **Highlight relationships** between modules.  
4. **Omit examples/APIs** unless critical to understanding functionality.  

### **Implementation Logic:**  
1. **File Role Detection:**  
   - Heuristic: Scan for dominant class/function names, docstrings, or exports.  
   - Example: A file with `process_payment()` → "Payment Processor".  

2. **Capability Extraction:**  
   - Summarize top-level functions/classes in plain English.  
   - Ignore helper/private methods unless they’re the file’s primary content.  

3. **Dependency Mapping:**  
   - Track imports to infer "Depends on".  
   - (Advanced) Use call graphs to infer "Used by".  

4. **Output Simplification:**  
   - Merge similar files (e.g., `utils/` → "Shared helper utilities").  
   - Group by domain (e.g., "All payment-related modules").  

---  

**Example Output:**  
```markdown
# Project "Alpha" Snapshot  

## backend/auth/jwt_manager.py  
**Role:** Handles JWT token generation and validation for API security.  
**Key Capabilities:**  
- Issues signed tokens for authenticated users  
- Validates tokens in incoming API requests  
- Integrates with user database for credential checks  

**Integration Points:**  
- Depends on: `pyjwt` library, `db/user_models.py`  
- Used by: `api/routers/login.py`, `middleware/security.py`  
```  
