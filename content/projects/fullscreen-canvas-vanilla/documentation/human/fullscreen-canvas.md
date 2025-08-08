# Fullscreen Canvas Documentation (High level overview)

## Functionality

- Main component for canvas.  
  Handles fullscreen on mobile,  
  resizing canvas to window size,  
  rendering loop with hook to engine.

## Implementation

### Public methods

#### Constructor

- Sets dependencies on fullscreen button component, canvas resizer and renderer.
- Resizes canvas, starts rendering loop.

#### Destroy

- Stops loop.
- Clears button component and resizer.
