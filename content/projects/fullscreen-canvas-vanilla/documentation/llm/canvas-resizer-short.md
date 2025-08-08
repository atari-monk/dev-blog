# Canvas Resizer Documentation (High level overview)

## Functionality

- Automatically resizes canvas to fit its container
- Handles both window resizes and direct container changes
- Maintains sharp visuals on high-DPI displays
- Throttles resize events for performance
- Notifies other components via events when resized

## Implementation

### Public methods

#### Constructor
- Sets up resize detection (using ResizeObserver when available)
- Performs initial canvas sizing

#### Resize
- Applies container dimensions with pixel ratio scaling
- Only updates if dimensions actually changed
- Emits 'canvas-resized' event when changes occur

#### Destroy
- Cleans up all resources (timers, observers, event listeners)
- Prepares instance for removal

### Private methods
- getDimensions: Measures container and applies pixel scaling
- setupEventListeners: Configures ResizeObserver or fallback
- handleResize: Throttles rapid resize events
- dispatchResizeEvent: Notifies listeners of size changes