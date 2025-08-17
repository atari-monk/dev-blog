# Renderer Documentation (High level overview)

## Functionality

- This class is canvas renderer service
- Calculates time
- Clears the canvas
- Provides a hook for engine frame calculation
- Runs in a loop for animation or renders image

## Implementation

### Public methods

#### Constructor

- Sets dependencies: canvas, engine hook, options, time calculator 
- Sets 2d canvas context

#### Start

- Resets time, sets runing state flag, starts animation

#### Stop

- Resets runing state flag, cancels animation

### Private methods

- Calculates frame, time, clear image, engine hook calculations,
