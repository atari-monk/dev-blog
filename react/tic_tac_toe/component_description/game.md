# Game Component

## State Management
- `history`: Array storing all board states (using `useState`)
- `currentMove`: Integer tracking current move index
- Derived state:
  - `xIsNext`: Boolean calculated from `currentMove`
  - `currentSquares`: Current board state from history

## Core Functions

### `handlePlay(nextSquares)`
1. Creates new history by:
   - Taking all moves up to current position
   - Appending new board state
2. Updates history and sets current move to latest position

### `jumpTo(nextMove)`
- Allows time travel by setting `currentMove` to specific index

### Move List Generation
- Maps history to JSX list items:
  - First move shows "Go to game start"
  - Subsequent moves show "Go to move #X"
  - Each has button to trigger `jumpTo`

## Component Structure
1. **Game Board**:
   - Renders `Board` component
   - Passes current game state and handlers

2. **Move History**:
   - Ordered list of buttons for time travel
   - Each button maintains its own move index

## Key React Patterns
1. **State Lifting**: Game manages all state, Board is controlled component
2. **Immutability**: Creates new history array instead of modifying
3. **Time Travel**: Full game history enables undo/redo functionality
4. **Derived State**: `xIsNext` and `currentSquares` computed from core state

## Data Flow
1. Board → Game: Sends updated squares via `onPlay`
2. Game → Board: Provides current state via props
3. User → Game: Time travel via move history buttons