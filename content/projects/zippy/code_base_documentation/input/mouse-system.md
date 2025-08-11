# Mouse System Documentation (High level overview)

## Functionality

- Tracks and updates mouse state including:
  - Current cursor position (x,y)
  - Button states (pressed/released)
  - Wheel scroll delta

## Implementation

### Public methods

#### Constructor

- Initializes default mouse state:
  - Sets position to (0,0)
  - Creates empty buttons map
  - Sets wheel delta to 0

#### setupCanvasEvents

- Takes canvas element and registers mouse event handlers:
  - `mousemove` - tracks cursor position relative to canvas
  - `mousedown` - sets button state to true
  - `mouseup` - sets button state to false
  - `wheel` - tracks vertical scroll delta

#### update

- Resets wheel delta to 0 (should be called every frame)

#### isButtonDown

- Takes mouse button number
- Returns current pressed state of button (false if never pressed)

#### getPosition

- Returns current mouse coordinates as {x, y} object

#### getWheel

- Returns current wheel scroll delta

### Private methods

- None (all event handlers are defined inline as arrow functions)