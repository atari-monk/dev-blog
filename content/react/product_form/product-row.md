# ProductRow

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQTnWE-alC_bTLNEpGCeYb0GAZBDr5DJo7WFWTEGvSI95Rc" width="98" height="120" frameborder="0" scrolling="no"></iframe>

## What This Code Does
- Displays a single product row in a table
- Shows product name and price
- Highlights out-of-stock products in red

## Key React Concepts

1. **Component Props**:
   - `{product}` is passed as a prop containing product data
   - Props are React's way of passing data from parent to child components

2. **Conditional Rendering**:
   - Checks `product.stocked` boolean
   - If true: renders plain product name
   - If false: wraps name in `<span>` with red color styling

3. **JSX Syntax**:
   - Mixes HTML-like tags with JavaScript expressions (`{ }`)
   - Returns table row (`<tr>`) with two cells (`<td>`)

4. **Inline Styles**:
   - Uses React's style object syntax: `{{color: 'red'}}`
   - Outer curly braces = JS expression
   - Inner curly braces = JS object

5. **Component Structure**:
   - Functional component (modern React standard)
   - Pure function that takes props and returns JSX

## Data Flow
1. Parent component passes a `product` object containing:
   - `name` (string)
   - `price` (string/number)
   - `stocked` (boolean)
2. Component renders this data in table format
3. UI changes based on stock status

This is a simple, focused component that demonstrates core React patterns in minimal code.