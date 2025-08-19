# Fullscreen Button Component

## Functionality

- Button that shows only if it's a touch-enabled device
- Toggles between fullscreen modes
- Dynamically changes text between "Enter Fullscreen" and "Exit Fullscreen"
- Automatically hides when in fullscreen mode (for touch devices)

## Implementation

### Public methods

#### Constructor

- Requires container argument (UI parent for button)
- Checks for touch device capability
- Creates button with initial "Enter Fullscreen" text
- Sets up event handlers
- Initializes button visibility state

#### Destroy

- Cleans up event listeners:
  - fullscreenchange
  - button click
- Removes button element from DOM

### Private methods

#### createFullscreenButton
- Creates button element with CSS class 'fullscreen-button'
- Appends button to container
- Returns created button element

#### handleFullscreenToggle
- Toggles between:
  - Requesting fullscreen on container
  - Exiting fullscreen
- Handles and logs any fullscreen API errors

#### setupEventListeners
- Sets up listeners for:
  - fullscreenchange (updates button state)
  - button clicks (triggers fullscreen toggle)

#### updateButtonVisibility
- Updates button text based on fullscreen state
- Toggles 'visible' CSS class based on:
  - Touch device capability
  - Current fullscreen state

#### isTouchDeviceCheck
- Detects touch capability using multiple methods:
  - ontouchstart in window
  - navigator.maxTouchPoints
  - CSS pointer:coarse media query
- Returns boolean result