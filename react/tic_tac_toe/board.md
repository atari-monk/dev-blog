# Board Component

## Core Concepts

1. **Component Structure**:
   - `Board` is a parent component managing game state
   - `Square` is a child component (imported) representing individual cells

2. **Props**:
   - `xIsNext`: Boolean tracking whose turn it is
   - `squares`: Array representing current board state (9 elements)
   - `onPlay`: Callback function to update game state

## Key Functions

### `handleClick(i)`
- **Purpose**: Handles player moves
- **Logic**:
  - Prevents moves if game is won or square is occupied
  - Creates copy of current board state (immutability principle)
  - Updates the copied array with "X" or "O"
  - Calls `onPlay` with new state

### `calculateWinner(squares)`
- **Purpose**: Determines if game is won
- **Logic**:
  - Checks all 8 possible winning lines
  - Returns winning player ("X"/"O") or `null` if no winner

## Rendering

1. **Status Display**:
   - Shows current winner or next player

2. **Board Layout**:
   - 3x3 grid of `Square` components
   - Each `Square` receives:
     - `value`: Current mark ("X", "O", or empty)
     - `onSquareClick`: Click handler with specific index

## React Patterns Demonstrated

1. **Lifting State Up**: Parent component manages state, passes down to children
2. **Immutability**: Using `slice()` to create new array instead of mutating
3. **Conditional Rendering**: Status message changes based on game state
4. **Component Composition**: Building complex UI from simple components

## Key Takeaways

1. React components receive data via props and communicate via callbacks
2. State should be managed by the lowest common parent component
3. Always treat state as immutable in React
4. UI is a function of state - re-renders happen when state changes