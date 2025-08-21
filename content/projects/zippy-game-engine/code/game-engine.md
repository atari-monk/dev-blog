# Game Engine

## Functionality

- Core engine class that manages game loop, scenes, and input systems.
- Coordinates frame updates between systems.
- Provides scene management capabilities.
- Handles debug mode toggling.

## Implementation

### Public properties

#### debugMode
- Boolean flag indicating whether debug mode is active.
- Can be toggled via `handleDebugToggle()` method.

### Public methods

#### Constructor
- Initializes with required systems (InputSystem and SceneSystem).
- Sets up initial debug mode state.

#### handleDebugToggle
- Toggles debug mode state.
- Logs current debug mode status to console.

#### frameTick
- Main game loop handler called each frame.
- **Parameter:** `context` - FrameContext object containing frame timing data
- Updates input system state.
- Updates and renders current scene if methods exist.

#### availableScenes (getter)
- Returns list of all registered scenes from SceneSystem.
- **Return type:** Array of scene names

#### activeScene (getter)
- Returns currently active scene from SceneSystem.
- **Return type:** Scene object or null

#### input (getter)
- Returns reference to InputSystem.
- **Return type:** InputSystem instance

#### onSceneChange
- Registers callback for scene change events.
- **Parameter:** `callback` - Function to call when scene changes
- Returns unsubscribe function.

#### transitionToScene
- Attempts to transition to specified scene by name.
- **Parameter:** `name` - Name of the scene to transition to
- Returns boolean indicating success.

#### registerScene
- Registers new scene with SceneSystem.
- **Parameters:**
  - `name` - Unique identifier for the scene
  - `sceneModule` - Scene implementation object

### Private methods
- No private methods (all dependencies injected via constructor).