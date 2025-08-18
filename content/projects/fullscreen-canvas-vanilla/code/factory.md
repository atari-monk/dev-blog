# Create Game Canvas Factory Documentation

## Functionality

- Generates Game Canvas component with fullscreen capabilities
- Creates and manages all related subcomponents and services

## Implementation

### Export methods

#### createGameCanvas

- params:
    - containerId: string - ID of HTML container element
    - canvasId: string - ID of canvas element
    - engineHook: EngineHook - Rendering callback function
    - options: FullscreenCanvasOptions - Configuration options (optional)
- returns: instance of FullscreenCanvas
- throws:
    - Error if container or canvas elements not found
    - Error if canvas element is not HTMLCanvasElement

### Internal Methods

#### getAndValidateElements
- Validates and retrieves DOM elements
- params:
    - containerId: string
    - canvasId: string
- returns: { container: HTMLElement, canvas: HTMLCanvasElement }
- throws errors if elements are invalid/missing

#### createComponents
- Creates all component instances
- params:
    - container: HTMLElement
    - services: { canvasResizer: CanvasResizer, renderer: Renderer }
- returns: FullscreenCanvas instance

#### createMergedOptions
- Merges user options with defaults
- params: options: FullscreenCanvasOptions
- returns: Merged options object (defaults: { isAnimLoop: true })

#### createServices
- Creates service instances
- params:
    - canvas: HTMLCanvasElement
    - options: FullscreenCanvasOptions
    - engineHook: EngineHook
- returns: Object containing:
    - canvasResizer: CanvasResizer instance
    - renderer: Renderer instance (with TimeCalculator)