# Canvas Resizer Documentation (Detailed API reference)

## Functionality

- Manages canvas element resizing to match its container dimensions
- Handles both window resizing and direct container resizing (using ResizeObserver when available)
- Maintains proper pixel ratio for high-DPI displays
- Throttles resize events for performance
- Dispatches custom "canvas-resized" event when dimensions change

## Implementation

### Public methods

#### Constructor

- Initializes the resizer with a target canvas element
- Binds event handlers and sets up initial resize listeners
- Performs initial resize of the canvas

#### resize()

- Checks current container dimensions
- Updates canvas size if dimensions have changed
- Maintains aspect ratio and handles high-DPI scaling
- Dispatches resize event if changes occurred

#### destroy()

- Cleans up all event listeners and observers
- Cancels any pending resize operations
- Prepares the instance for garbage collection

### Private methods

#### getDimensions()

- Calculates current container dimensions
- Applies device pixel ratio scaling
- Returns width and height as integers

#### setupEventListeners()

- Sets up appropriate resize detection mechanism
- Uses ResizeObserver when available, falls back to window resize events
- Observes either canvas parent or document body

#### handleResize()

- Throttles resize events using a timer
- Ensures resize operations don't happen too frequently
- Clears pending resize if new resize occurs

#### dispatchResizeEvent()

- Creates and dispatches custom "canvas-resized" event
- Includes width, height and pixel ratio in event details
- Event is dispatched from the canvas element itself