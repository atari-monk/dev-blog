Good question — using a clear, consistent naming convention makes a big difference, especially in a TypeScript + Vite project. Here’s what’s generally recommended in modern frontend projects:

---

### ✅ **1. Files & Folders**

* **Components:** `PascalCase` — `Header.tsx`, `UserProfile.tsx`
* **Hooks:** `camelCase` — `useAuth.ts`
* **Utilities/helpers:** `camelCase` — `formatDate.ts`
* **Styles:**

  * If using CSS Modules: `ComponentName.module.css`
  * If using plain CSS/SCSS: `snake-case` or `kebab-case` — `main.scss`, `reset.css`
* **Assets:** `kebab-case` — `logo.svg`, `hero-image.png`

---

### ✅ **2. Variables & Functions**

* `camelCase` — `userName`, `getUserProfile()`

---

### ✅ **3. Types & Interfaces**

* `PascalCase` — `User`, `AuthContextProps`
* Prefix `I` is optional — `User` vs `IUser` (modern TS projects often skip `I`)

---

### ✅ **4. Constants**

* `UPPER_SNAKE_CASE` — `API_URL`, `DEFAULT_THEME`

---

### ✅ **5. Project Structure Example**

```
src/
 ├─ components/
 │   ├─ Header.tsx
 │   ├─ UserProfile.tsx
 ├─ hooks/
 │   ├─ useAuth.ts
 │   ├─ useFetch.ts
 ├─ utils/
 │   ├─ formatDate.ts
 │   ├─ validateEmail.ts
 ├─ styles/
 │   ├─ variables.scss
 │   ├─ reset.css
 ├─ assets/
 │   ├─ logo.svg
 ├─ types/
 │   ├─ user.ts
 ├─ App.tsx
 ├─ main.tsx
```

---

### ✅ **6. Vite Config & Env**

* Config files: `vite.config.ts`
* Env files: `.env`, `.env.local`
* Use `VITE_` prefix for env vars: `VITE_API_URL`

---

**In short:**
✔️ PascalCase → Components, Classes, Types
✔️ camelCase → Functions, Variables, Hooks
✔️ UPPER\_SNAKE\_CASE → Constants
✔️ kebab-case → Assets, non-module CSS filenames

---

If you want, I can help you make an ESLint/Prettier config to enforce this too. Want that?

## Folders naming

Great follow-up — folder naming style is worth being consistent about too!

In **modern Vite + TypeScript projects**, there are two common conventions for **folders**:

---

### ✅ **1️⃣ kebab-case (most common)**

* `components/`
* `hooks/`
* `utils/`
* `pages/`
* `styles/`
* `assets/`

**Why?**

* Easy to read in URLs and file paths.
* Works well across operating systems.
* Matches how folders are named in many open-source projects.

---

### ✅ **2️⃣ PascalCase (also acceptable for components folders)**

Some teams prefer `PascalCase` only for folders that hold a single component:

```
components/
 ├─ Header/
 │   ├─ Header.tsx
 │   ├─ Header.module.css
```

This is nice if you co-locate files (component, styles, tests) inside a folder.
In that case:

* Use `PascalCase` for the component folder — `UserProfile/`
* Keep everything related inside: `UserProfile.tsx`, `UserProfile.test.tsx`, `UserProfile.module.scss`

---

### ⚡️ **Rule of thumb**

* **Top-level folders:** `kebab-case`
* **Feature/Component folders:** `PascalCase` if co-locating files

---

### ✅ **Example**

```
src/
 ├─ components/
 │   ├─ Header/
 │   │   ├─ Header.tsx
 │   │   ├─ Header.module.css
 │   ├─ UserProfile/
 │   │   ├─ UserProfile.tsx
 ├─ hooks/
 ├─ utils/
 ├─ pages/
 ├─ assets/
 ├─ styles/
```

---

**Summary:**
✔️ `kebab-case` for general folders
✔️ `PascalCase` for co-located component folders
✔️ Be consistent across the whole project

If you’d like, I can generate a folder structure template for you too — want one?
