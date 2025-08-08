# Canvas Resizer Documentation (High level overview)

## Functionality

- This class resizes canvas in reaction to window resizes

## Implementation

### Public methods

#### Constructor

- Sets up handler of resize event
- Resize initially

#### Resize

- Smart resize logic with delay and pixelRatio
- Emitts resize event

#### Destroy

- Remove timer
- Remove event handlers

### Private methods

- Gets canvas container dimensions
- Setup event handlers
- Handles resize logic
- Sends custom event canvas-resized
