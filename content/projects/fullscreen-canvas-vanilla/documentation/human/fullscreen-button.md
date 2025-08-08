# Fullscreen Button Component Documentation (High level overview)

## Functionality

- Button that shows only if it is a mobile device
- Allows to switch to fullscreen and then is hidden

## Implementation

### Public methods

#### Constructor

- Requires container argument (ui parent for button)
- Sets is mobile flag
- Creates button
- Creates event handlers
- Add handlers to events
- Update button visibility

#### Destroy

- Remove event handlers
- Remove button

### Private methods

- Generating button
- Toggle fullscreen
- Setup events
- Update button visibility
- Check if mobile device
