### **Name: Codebase Capability Summary**  
**Purpose:** Provide a rapid overview of what the codebase *does* as a system, organized by functional domains.  

### **Output Format:**  
```markdown 
# [Codebase Name] Functional Overview  

## Core Capabilities  
1. **[Domain/System 1]**: Brief description of its purpose and outcomes.  
   - Key abilities:  
     - Does [X] (e.g., "Processes payments via Stripe/PayPal")  
     - Enables [Y] (e.g., "User role-based access control")  

2. **[Domain/System 2]**: [...]  

## Critical Integrations  
- **External**: [Service/API names] → [Usage] (e.g., "AWS S3 for file storage")  
- **Internal**: [Major module dependencies] → [Purpose] (e.g., "Auth service → Used by all APIs")  

## Key Data/Outputs  
- Generates: [Reports/APIs/UI components] (e.g., "REST API for mobile apps")  
- Manages: [Core data entities] (e.g., "User profiles, transaction logs")  
```  

### **Key Differences:**  
- **Aggregates by domain** (e.g., "Payment System" instead of individual files).  
- **Omits file paths** unless critical (focus on *what*, not *where*).  
- **Prioritizes outcomes** (e.g., "Enables PDF exports" vs. "Uses libXYZ").  

### **Example Output:**  
```markdown  
# "ShopFast" E-Commerce Overview  

## Core Capabilities  
1. **Order Processing**: Handles checkout, payments, and inventory updates.  
   - Key abilities:  
     - Processes credit card/PayPal transactions  
     - Syncs inventory levels in real-time  

2. **User Management**: Manages authentication and profiles.  
   - Key abilities:  
     - OAuth2 login via Google/Facebook  
     - Role-based permissions (admin/customer)  

## Critical Integrations  
- **External**: Stripe (payments), SendGrid (emails), UPS API (shipping)  
- **Internal**: Auth service → Required by orders, analytics, and admin UI  

## Key Data/Outputs  
- Generates: Order confirmations, sales dashboards  
- Manages: Product catalog, customer reviews  
```  

---  
