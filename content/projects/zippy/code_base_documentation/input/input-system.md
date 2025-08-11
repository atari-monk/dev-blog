# InputSystem Documentation (High level overview)

## Functionality

- Acts as a central hub for all input systems (keyboard, mouse, gamepads, and touch).
- Manages initialization and updates of all input subsystems.
- Provides canvas event setup for mouse and touch inputs.

## Implementation

### Public methods

#### Constructor

- Initializes all input subsystems:
  - `KeyboardSystem`
  - `MouseSystem`
  - `GamepadInputProcessor`
  - `TouchSystem`

#### setupCanvasEvents

- Takes an HTML canvas element.
- Delegates canvas event setup to mouse and touch systems.

#### update

- Updates state of gamepad and mouse systems.
- Should be called every frame for accurate input tracking.

### Private methods

- (No private methods in this class)