# ProductTable

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQSZBOOSl-jFQ4Ch2AaDTOibAY9n_mnu3b58zrmvtS41EN0" width="98" height="120" frameborder="0" scrolling="no"></iframe>

## Core Purpose
This component displays a filtered list of products in a table, grouped by category.

## Key React Concepts Illustrated:

1. **Component Composition**:
   - Uses two child components (`ProductCategoryRow` and `ProductRow`)
   - Shows how to build complex UIs from smaller pieces

2. **Props**:
   - Receives `products`, `filterText`, and `inStockOnly` as props
   - Passes data down to child components via props

3. **Conditional Rendering**:
   - Filters products based on `filterText` and `inStockOnly`
   - Only shows products matching search text and stock status

4. **List Rendering**:
   - Builds a `rows` array dynamically
   - Uses `key` prop for efficient React reconciliation

5. **State Management**:
   - Tracks `lastCategory` to determine when to render category headers

## Execution Flow:

1. Initializes empty `rows` array and `lastCategory` tracker
2. Iterates through each product:
   - Skips products not matching `filterText`
   - Skips out-of-stock products if `inStockOnly` is true
   - Adds category header when category changes
   - Always adds product row
3. Renders table with accumulated rows

## Important Details:

- `key` props are crucial for React's diffing algorithm
- `filterText` matching is case-insensitive
- Category headers only appear when category changes
- Pure rendering based on props (no internal state)