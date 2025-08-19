# TouchSystem

## Functionality

- Tracks and manages touch inputs on a canvas element.
- Stores touch positions relative to the canvas.
- Provides access to touch count and individual touch positions.

## Implementation

### Public methods

#### Constructor

- Initializes an empty Map to store touch information.

#### setupCanvasEvents

- Takes a canvas HTMLElement as parameter.
- Registers touch event listeners (touchstart, touchmove, touchend) on the canvas.
- Prevents default behavior for touch events.
- Handles touch events through private methods.
- Uses passive: false and capture: false options for event listeners.

#### getCount

- Returns the current number of active touches.

#### getPositions

- Returns an array of all current touch positions.

#### getPosition

- Takes a touch identifier.
- Returns the position of the specified touch or null if not found.

### Private methods

#### #handleTouchEvent

- Takes a TouchEvent and canvas element.
- Updates touch positions relative to the canvas by calculating client coordinates minus canvas offset.
- Stores touch positions in the touches Map.
