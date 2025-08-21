# InputSystem

## Functionality

- Acts as a central hub for input systems (keyboard, mouse, gamepads, and touch).
- Manages initialization of all input subsystems.
- Provides canvas event setup for mouse and touch inputs.
- Handles frame updates for gamepad and mouse state tracking.

## Implementation

### Public methods

#### Constructor

- Initializes all input subsystems as readonly properties:
  - `keyboard`: KeyboardSystem instance
  - `mouse`: MouseSystem instance  
  - `gamepads`: GamepadInputProcessor instance
  - `touches`: TouchSystem instance

#### setupCanvasEvents

- Takes an HTML canvas element.
- Delegates canvas event setup to mouse and touch systems.

#### update

- Updates state of gamepad and mouse systems.
- Should be called every frame for accurate input tracking.

### Private methods

- (No private methods in this class)