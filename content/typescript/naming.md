# TypeScript Naming Conventions

## Table of Contents
- [Variables](#variables)
- [Functions](#functions)
- [Classes](#classes)
- [Interfaces](#interfaces)
- [Types](#types)
- [Enums](#enums)
- [Constants](#constants)
- [Files](#files)
- [Generics](#generics)
- [Boolean Variables](#boolean-variables)

## Variables

### camelCase for variables and function parameters
```typescript
// Good
let userName: string = "John";
const maxItems: number = 100;

function calculateTotal(price: number, quantity: number): number {
  return price * quantity;
}

// Bad
let UserName: string = "John"; // PascalCase
const MAX_ITEMS: number = 100; // Should be constant
let user_name: string = "John"; // snake_case
```

## Functions

### camelCase for function names
```typescript
// Good
function calculateTotal(): number {
  return 0;
}

function getUserById(id: string): User {
  // implementation
}

// Bad
function CalculateTotal(): number { // PascalCase
  return 0;
}

function get_user_by_id(id: string): User { // snake_case
  // implementation
}
```

### Verb-based function names
```typescript
// Good
function fetchData(): void {}
function validateInput(): boolean {}
function formatDate(): string {}

// Less clear
function data(): void {} // What does it do?
function input(): boolean {} // Not descriptive
```

## Classes

### PascalCase for class names
```typescript
// Good
class UserService {
  // class implementation
}

class HttpClient {
  // class implementation
}

// Bad
class userService { // camelCase
  // class implementation
}

class HTTP_CLIENT { // UPPER_CASE
  // class implementation
}
```

### PascalCase for class methods and properties
```typescript
class User {
  // Properties - camelCase
  private firstName: string;
  private lastName: string;
  
  // Constructor
  constructor(firstName: string, lastName: string) {
    this.firstName = firstName;
    this.lastName = lastName;
  }
  
  // Methods - camelCase
  public getFullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }
  
  // Static methods - camelCase
  public static createUser(): User {
    return new User("", "");
  }
}
```

## Interfaces

### PascalCase for interface names (often with 'I' prefix)
```typescript
// Common convention (I prefix)
interface IUser {
  id: string;
  name: string;
}

interface IApiResponse<T> {
  data: T;
  status: number;
}

// Alternative (without I prefix - also common)
interface User {
  id: string;
  name: string;
}

// Usage
class UserService implements IUser {
  // implementation
}
```

## Types

### PascalCase for type aliases
```typescript
// Good
type UserRole = "admin" | "user" | "guest";
type ApiResponse<T> = {
  data: T;
  status: number;
};

type Coordinate = {
  x: number;
  y: number;
};

// Bad
type user_role = "admin" | "user" | "guest"; // snake_case
type apiresponse<T> = { // camelCase
  data: T;
  status: number;
};
```

## Enums

### PascalCase for enum names and members
```typescript
// Good
enum UserRole {
  Admin = "admin",
  User = "user",
  Guest = "guest"
}

enum HttpStatusCode {
  OK = 200,
  NotFound = 404,
  ServerError = 500
}

// Usage
const role: UserRole = UserRole.Admin;

// Bad
enum user_role { // camelCase
  ADMIN = "admin",
  USER = "user"
}

enum HTTP_STATUS_CODE { // UPPER_CASE
  OK = 200
}
```

## Constants

### UPPER_CASE for true constants
```typescript
// Good - values that won't change
const MAX_USERS: number = 100;
const API_BASE_URL: string = "https://api.example.com";
const DEFAULT_TIMEOUT: number = 5000;

// Config values that might change but are treated as constants
const APP_CONFIG = {
  version: "1.0.0",
  environment: "production"
} as const;

// Bad - not truly constant values
const maxUsers = calculateMaxUsers(); // This isn't a constant
let API_URL = "https://api.example.com"; // let shouldn't be UPPER_CASE
```

## Files

### camelCase for file names (or kebab-case)
```typescript
// Good (camelCase)
userService.ts
apiClient.ts
utils.ts

// Good (kebab-case - also common)
user-service.ts
api-client.ts
date-utils.ts

// For component files (React/Vue)
UserComponent.tsx   // PascalCase for components
user-hook.ts        // kebab-case for hooks

// Bad
UserService.ts      // PascalCase for regular files
API_CLIENT.ts       // UPPER_CASE
user_service.ts     // snake_case
```

## Generics

### Single uppercase letters for generic types
```typescript
// Good
interface Response<T> {
  data: T;
  status: number;
}

function identity<T>(value: T): T {
  return value;
}

class Repository<TEntity, TId> {
  // implementation
}

// Common generic type names:
// T - Type
// K - Key
// V - Value
// E - Element
// R - Return type

// Bad
function identity<type>(value: type): type { // lowercase
  return value;
}

interface Response<Data> { // PascalCase - usually reserved for specific types
  data: Data;
}
```

## Boolean Variables

### Prefix with 'is', 'has', 'should', 'can', etc.
```typescript
// Good
const isActive: boolean = true;
const hasPermission: boolean = false;
const shouldUpdate: boolean = true;
const canEdit: boolean = false;
const isLoading: boolean = true;

// Bad
const active: boolean = true; // Not clear it's a boolean
const permission: boolean = false; // Sounds like a value, not a flag
const update: boolean = true; // Sounds like a function
```

## Best Practices Summary

1. **camelCase** for variables, functions, methods, and properties
2. **PascalCase** for classes, interfaces, types, and enums
3. **UPPER_CASE** for true constants
4. Use descriptive names that indicate purpose
5. Avoid abbreviations unless widely understood
6. Use verb-based names for functions
7. Prefix boolean variables with `is`, `has`, `should`, etc.
8. Be consistent within your project

```typescript
// Example of good naming conventions
const MAX_RETRY_ATTEMPTS = 3;

interface IUserProfile {
  id: string;
  firstName: string;
  lastName: string;
  isActive: boolean;
}

class UserService {
  private apiClient: ApiClient;
  
  constructor(apiClient: ApiClient) {
    this.apiClient = apiClient;
  }
  
  async getUserById(userId: string): Promise<IUserProfile> {
    const response = await this.apiClient.fetch<UserResponse>(`/users/${userId}`);
    return this.mapToUserProfile(response.data);
  }
  
  private mapToUserProfile(data: UserResponse): IUserProfile {
    return {
      id: data.id,
      firstName: data.first_name,
      lastName: data.last_name,
      isActive: data.status === "active"
    };
  }
}
```