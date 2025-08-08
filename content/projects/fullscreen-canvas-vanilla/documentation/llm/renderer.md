# Renderer Documentation

## Functionality

The `Renderer` class manages the rendering loop for a canvas-based application. It handles:
- Starting and stopping the animation loop
- Calculating frame timing (delta time and total time)
- Clearing the canvas and delegating rendering to an engine hook
- Supporting both looping and non-looping rendering modes

## Implementation

### Public methods

#### Constructor

- Initializes the renderer with a canvas, engine hook, options, and time calculator
- Parameters:
  - `canvas`: HTMLCanvasElement - The canvas element to render to
  - `engineHook`: EngineHook - The engine implementation that handles actual rendering
  - `options`: FullscreenCanvasOptions - Configuration options for the renderer
  - `timeCalculator`: TimeCalculator - Utility for calculating frame timing
- Throws an error if 2D context cannot be obtained from the canvas

#### start()

- Starts the rendering loop if not already running
- Resets the time calculator
- Begins the animation frame request cycle

#### stop()

- Stops the rendering loop if currently running
- Cancels any pending animation frame requests

### Private methods

#### frameTick(time: number)

- The core rendering callback called each animation frame
- Parameters:
  - `time`: number - The timestamp provided by requestAnimationFrame
- Calculates deltaTime and totalTime using the time calculator
- Creates a FrameContext with rendering information
- Clears the canvas and delegates rendering to the engine hook
- Continues the loop if options.loop is true and renderer is still running