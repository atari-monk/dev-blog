# ProductCategoryRow 

<iframe src="https://1drv.ms/u/c/37f44e52f80d7972/IQTzUb8TzwAiQKm7l_5K8zMwAV_J4E9fx6aWB7Gn29rRvA4" width="98" height="120" frameborder="0" scrolling="no"></iframe>

## What this is:
- A React functional component that renders a table row (`<tr>`) with a header cell (`<th>`)
- Used to display product categories in a table layout

## Key React concepts demonstrated:
1. **Component Props**: Takes a single prop `category` (destructured directly in parameters)
2. **JSX Syntax**: Returns HTML-like syntax that gets compiled to React elements
3. **Table Elements**: Uses standard HTML table elements (`tr`, `th`) with React
4. **colSpan Attribute**: HTML attribute passed directly in JSX to span 2 columns

## How it works:
- When rendered, creates a table row with a header cell
- The header cell spans 2 columns (colSpan="2")
- Displays the `category` prop value as the cell content
- Example usage: `<ProductCategoryRow category="Electronics" />`

## Why this matters:
- Shows how to create simple, reusable components in React
- Demonstrates proper use of HTML table semantics in React
- Illustrates basic prop passing pattern (destructuring in parameters)

This is a pure presentational component - it only displays data without any logic.
