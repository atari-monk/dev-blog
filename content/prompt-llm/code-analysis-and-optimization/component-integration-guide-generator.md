### **Name: Component Integration Guide Generator**  
**Purpose:** Create clear, actionable instructions for using a specific code component in a real project.  

### **Input:**  
- A single component file (e.g., `useAuth.ts`, `PaymentService.js`, `api_client.py`).  
- (Optional) Example usage context (e.g., "We use this in a React app with Redux").  

### **Output Format:**  
```markdown
# [Component Name] Usage Guide  

## **1. Purpose**  
- In 1 sentence: "This [component] handles [X] so you can [Y]."  
- Example: "`useAuth` manages user login/logout state and tokens for React apps."  

## **2. Installation**  
- **Dependencies**: List libraries/packages required (e.g., "Requires `axios@^1.0.0`").  
- **Install command**: `npm install [deps]` / `pip install [deps]`.  

## **3. Basic Usage**  
```[language]  
// Minimal working example:  
[Code snippet showing the simplest way to invoke/import the component]  
```  

## **4. Configuration (if needed)**  
- **Key options**: Bullet list of params/flags that matter (e.g., `apiKey: string`).  
- **Defaults**: "Uses `timeout: 5000ms` if unspecified."  

## **5. Common Use Cases**  
- **Scenario 1**: "[Action]" → "[How to achieve it with the component]".  
  ```[language]  
  [Example code]  
  ```  
- **Scenario 2**: [...]  

## **6. Troubleshooting**  
- **Error X**: "Fix: [Solution] (e.g., 'Ensure the parent component provides context')."  
- **Limitations**: "Does not support [Z] (use [alternative] instead)."  

---  

### **Example Output:**  
```markdown
# `useFetch` Usage Guide  

## **1. Purpose**  
- "This React hook simplifies data fetching with caching and error handling."  

## **2. Installation**  
- **Dependencies**: `react@^18`, `axios@^1.0.0`.  
- **Install command**: `npm install axios`.  

## **3. Basic Usage**  
```jsx  
import useFetch from './hooks/useFetch';  

function UserProfile() {  
  const { data, loading } = useFetch('/api/user/123');  
  return loading ? <Spinner /> : <div>{data.name}</div>;  
}  
```  

## **4. Configuration**  
- **Key options**:  
  - `url`: Required endpoint (string).  
  - `cacheTTL`: Cache duration in seconds (default: `60`).  

## **5. Common Use Cases**  
- **Fetch with auth headers**:  
  ```jsx  
  useFetch('/api/protected', { headers: { Authorization: token } });  
  ```  
- **POST request**:  
  ```jsx  
  const { post } = useFetch();  
  post('/api/submit', { payload });  
  ```  

## **6. Troubleshooting**  
- **Error 401**: "Fix: Pass a valid `Authorization` header."  
- **Limitations**: "No retry logic; use `useFetchRetry` for unstable networks."  
```  
