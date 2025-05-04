### **PowerShell Variable Lifetime (Short Answer)**  
Variables like `$in` and `$out` persist **only for the current session** (until you close the terminal).  

---

### **Key Details (Developer Focus)**
1. **Scope**:  
   - Variables declared in the **console** live in the **global scope**.  
   - They remain available until you:  
     - Close the terminal  
     - Run `Remove-Variable -Name in, out`  
     - Start a new session.  

2. **Scripts vs. Console**:  
   - If you define `$in` inside a **script**, it dies when the script ends (unless explicitly scoped with `$global:in`).  
   - Your example (`$in = "..."`) runs in the **console**, so it persists.  

3. **Verify**:  
   ```powershell
   $in = "C:\docs\input.md"  # Set variable
   $in                       # Outputs "C:\docs\input.md" (proves it's stored)
   Get-Variable -Name in     # Confirms existence
   ```  

4. **Clear Manually**:  
   ```powershell
   Remove-Variable -Name in, out  # Deletes them
   ```  

---

### **When You Close PowerShell**  
All variables are wiped. No memory persists unless you:  
- Save them to disk (e.g., `Export-Clixml`).  
- Use a profile script (`$PROFILE`).  

*(No fluff—just facts.)*