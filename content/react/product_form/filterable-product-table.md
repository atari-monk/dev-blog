# FilterableProductTable

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQQh8ofgisP6S6_o7DO0aec3AdJ-uxkTV84gx2WUZwIWLHo" width="98" height="120" frameborder="0" scrolling="no"></iframe>

## Core Concepts

1. **Component Composition**: This is a parent component combining `SearchBar` and `ProductTable`.

2. **State Management**: Uses React's `useState` hook to manage two pieces of state:
   - `filterText` (string): Tracks search input
   - `inStockOnly` (boolean): Tracks checkbox status

3. **Props Flow**:
   - Receives `products` data from parent component
   - Passes state and handlers down to child components

## Key Patterns

1. **Controlled Components**:
   - `SearchBar` is controlled via props (`filterText`, `inStockOnly`)
   - Changes are handled via `onFilterTextChange` and `onInStockOnlyChange`

2. **Lifting State Up**:
   - State is managed in this parent component
   - Changes propagate down through props

## How It Works

1. **Initialization**:
   - State variables are created with empty string and false as default values

2. **Render Cycle**:
   - Renders `SearchBar` and `ProductTable` with current state values
   - When user interacts with `SearchBar`, it calls the handlers:
   - `setFilterText` updates `filterText`
   - `setInStockOnly` toggles `inStockOnly`

3. **Data Flow**:
   - Updated state triggers re-render
   - New values propagate to `ProductTable` for filtering

## What You Should Learn From This

1. **Basic React Component Structure**
2. **State Management with Hooks**
3. **Parent-Child Communication**
4. **Controlled Component Pattern**

This is a classic example of React's unidirectional data flow and component composition.
