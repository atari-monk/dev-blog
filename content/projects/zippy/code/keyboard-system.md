# KeyboardSystem

## Functionality

- Stores and updates keyboard key states (pressed/released)
- Prevents default browser behavior for arrow keys and spacebar to avoid scrolling
- Provides query methods to check key states

## Implementation

### Public methods

#### Constructor

- Initializes keys state object
- Binds event handlers to class instance
- Registers event listeners

#### isKeyDown

- Takes key symbol as parameter
- Returns boolean indicating if key is currently pressed
- Returns false for unregistered keys

#### destroy

- Removes all keyboard event listeners
- Cleans up event handler references

### Private methods

#### #setupEventListeners

- Registers keydown and keyup event listeners on window

#### #handleKeyDown

- Sets key state to true when pressed
- Prevents default behavior for arrow keys and spacebar

#### #handleKeyUp

- Sets key state to false when released
