### **Name: Project Structure Refactor Advisor**  
**Purpose:** Transform a chaotic project tree into a well-organized, domain-driven structure for better maintainability.  

### **Input:**  
1. **Current Project Tree** (e.g., from `tree` command or IDE):  
   ```plaintext
   /project  
   ├── /src  
   │   ├── utils.js  
   │   ├── auth.js  
   │   ├── api.js  
   │   ├── /components  
   │   │   ├── Button.js  
   │   │   ├── Navbar.js  
   │   │   └── PaymentForm.js  
   │   └── /styles  
   │       └── main.css  
   ├── /scripts  
   │   └── deploy.sh  
   └── /docs  
       └── README.md  
   ```  

2. **File Descriptions** (optional but helpful):  
   - `auth.js`: "Handles user login, JWT tokens, and session management."  
   - `PaymentForm.js`: "Stripe integration for checkout flows."  

### **Output Format:**  
```plaintext
[Project Name]  
│  
├── /core/                  # Domain-independent fundamentals  
│   ├── /utils/             # Reusable helpers (e.g., date formatters)  
│   └── /logging/           # Centralized logging  
│  
├── /domains/               # Business logic by feature  
│   ├── /auth/              # Auth-related files  
│   │   ├── auth.js         # Session/JWT logic  
│   │   └── /components/    # Auth-specific UI (e.g., LoginForm)  
│   │  
│   ├── /payments/          # Payment processing  
│   │   ├── PaymentService.js  
│   │   └── /components/    # e.g., PaymentForm.js  
│   │  
│   └── /api/               # API communication layer  
│       ├── api.js          # Base client  
│       └── /endpoints/     # Organized by resource (e.g., users.js)  
│  
├── /infrastructure/        # DevOps/glue code  
│   ├── /scripts/           # Deployment/build scripts  
│   └── /config/            # Env files, CI/CD templates  
│  
└── /interface/             # User-facing layers  
    ├── /components/        # Shared UI (e.g., Button.js)  
    └── /styles/            # Global CSS/theming  
```  

### **Rules Applied:**  
1. **Domain-Driven**: Group by business capability (e.g., `auth/`, `payments/`).  
2. **Layer Separation**: Isolate core logic (`/core`), UI (`/interface`), and infra.  
3. **Flat > Nested**: Avoid deep nesting (max 3-4 levels).  
4. **No Generic Folders**: Replace `utils/` with purposeful names (e.g., `/core/date-utils`).  

---

### **Example Transformation:**  
**Before (Chaotic):**  
```plaintext
/src  
├── helpers.js  
├── userAuth.js  
├── cart.js  
├── /components  
│   ├── Modal.js  
│   └── Checkout.js  
└── /api  
    └── fetchData.js  
```  

**After (Organized):**  
```plaintext
domains/  
├── /ecommerce/  
│   ├── cart.js            # Business logic  
│   └── /components/       # Feature-specific UI  
│       └── Checkout.js  
│  
├── /auth/  
│   └── userAuth.js        # Auth logic  
│  
interface/  
└── /components/  
    └── Modal.js           # Shared UI  

core/  
└── /network/  
    └── fetchData.js       # Reusable API client  
```  

### **Key Features:**  
- **Framework-Agnostic**: Works for React, Django, etc.  
- **Scalability**: Prepares for growth (e.g., microservices).  
- **Justification**: Explains *why* files move (e.g., "`cart.js` → `/domains/ecommerce` for cohesion").  

**Bonus:** Add a `migration.md` with commands to reorganize files automatically!