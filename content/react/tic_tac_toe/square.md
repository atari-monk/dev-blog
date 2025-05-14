# Square Component

## Core Functionality
- **Purpose**: Renders a single tic-tac-toe square
- **Type**: Presentational/dumb component (no internal state)

## Props
1. `value`: String ("X", "O", or empty) to display in the square
2. `onSquareClick`: Callback function for click events

## Implementation Details
- Renders a `<button>` element with:
  - `className="square"` for styling
  - `onClick` handler connected to the passed prop
  - Displays the `value` prop as button content

## Key React Concepts Demonstrated
1. **Props**: Receives data and behavior from parent component
2. **Event Handling**: Delegates click handling to parent via callback
3. **Component Reusability**: Stateless design allows multiple instances
4. **Simple Rendering**: Pure function that returns JSX based on props

## Why This Matters
- Shows how to create basic interactive UI elements in React
- Demonstrates parent-child component communication pattern
- Illustrates separation of concerns (display vs logic)