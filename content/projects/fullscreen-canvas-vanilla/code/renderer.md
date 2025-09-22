# Renderer

## Functionality

- Manages the animation loop for a fullscreen canvas application
- Handles frame timing calculations (deltaTime and totalTime)
- Provides rendering context to the engine hook each frame
- Automatically clears the canvas between frames
- Supports both single-frame and continuous animation modes

## Implementation

### Public methods

#### Constructor

- Initializes the 2D rendering context (throws error if unavailable)
- Stores dependencies for later use
- Validates canvas support

#### Start

- Resets time calculations
- Sets running state to true
- Initiates the animation loop using requestAnimationFrame
- Safe to call when already running (no-op)

#### Stop

- Cancels any active animation frame request
- Sets running state to false
- Safe to call when not running (no-op)

### Private methods

#### frameTick

- Core animation loop handler
- Calculates frame timing (deltaTime and totalTime)
- Creates FrameContext containing:
  - Canvas rendering context (ctx)
  - Canvas dimensions (width, height)
  - Timing information (deltaTime, totalTime)
- Clears the canvas
- Invokes the engine hook with current context
- Continues animation loop if `options.isAnimLoop` is true
