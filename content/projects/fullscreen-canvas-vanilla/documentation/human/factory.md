# Create Game Canvas Factory Documentation (High level overview)

## Functionality

- Generates Game Canvas component.

## Implementation

### Export methods

#### createGameCanvas

- params:
    - containerId
    - canvasId
    - engineHook
    - options
- returns instance of FullscreenCanvas

### Methods

- gets container and canvas elements and validates them
- generates FullscreenCanvas and its composite components
- merges options with default
- generates services for components