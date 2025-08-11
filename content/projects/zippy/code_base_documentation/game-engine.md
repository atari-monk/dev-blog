# GameEngine Documentation (High level overview)

## Functionality

- Core engine class that manages game loop, scenes, and input systems.
- Coordinates frame updates between systems.
- Provides scene management capabilities.
- Handles debug mode toggling.

## Implementation

### Public methods

#### Constructor

- Initializes with required systems (InputSystem and SceneSystem).
- Sets up initial debug mode state.

#### handleDebugToggle

- Toggles debug mode state.
- Logs current debug mode status to console.

#### frameTick

- Main game loop handler called each frame.
- Updates input system state.
- Updates and renders current scene if methods exist.

#### availableScenes (getter)

- Returns list of all registered scenes from SceneSystem.

#### activeScene (getter)

- Returns currently active scene from SceneSystem.

#### input (getter)

- Returns reference to InputSystem.

#### onSceneChange

- Registers callback for scene change events.
- Returns unsubscribe function.

#### transitionToScene

- Attempts to transition to specified scene by name.
- Returns boolean indicating success.

#### registerScene

- Registers new scene with SceneSystem.

### Private methods

- No private methods (all dependencies injected via constructor).