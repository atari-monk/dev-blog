# Scene Interface

## Functionality

- Defines the structure for game/application scenes.  
- Provides lifecycle hooks for scene management.  
- Allows optional implementation of scene behaviors.

## Implementation

### Public methods

#### name (optional property)

- Identifier for the scene.

#### displayName (optional property)

- Human-readable name for the scene.

#### init (optional method)

- Called once when the scene is first loaded.  
- Used for initial setup and resource loading.

#### update (optional method)

- Called every frame before rendering.  
- Receives deltaTime (time since last frame) for frame-independent updates.  
- Used for game logic and state updates.

#### render (optional method)

- Called every frame after update.  
- Receives FrameContext for drawing operations.  
- Used for visual rendering.

#### onEnter (optional method)

- Called when the scene becomes active.  
- Used for activation setup.

#### onExit (optional method)

- Called when the scene becomes inactive.  
- Used for cleanup before switching scenes.

#### resize (optional method)

- Called when the viewport resizes.  
- Used for responsive layout adjustments.