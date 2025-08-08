# Fullscreen Component Documentation (Detailed API reference)

## Functionality

- Creates a fullscreen toggle button that automatically:
  - Only appears on mobile/touch devices
  - Hides when entering fullscreen mode
  - Shows "Enter Fullscreen"/"Exit Fullscreen" text based on current state

## Implementation

### Public Methods

#### `constructor(container: HTMLElement)`
Initializes the fullscreen component.

**Parameters:**
- `container` - The parent HTML element where the button will be placed

**Behavior:**
1. Stores the container reference
2. Detects if running on a mobile/touch device
3. Creates the fullscreen button
4. Sets up event handlers
5. Initializes button visibility state

#### `destroy()`
Cleans up the component by:
1. Removing all event listeners
2. Removing the button from DOM

### Private Methods

#### `createFullscreenButton()`
- Generates and returns a styled button element
- Adds the button to the container
- Button text defaults to "Enter Fullscreen"

#### `handleFullscreenToggle()`
- Toggles between fullscreen and normal mode
- Handles both entering and exiting fullscreen
- Catches and logs any fullscreen API errors

#### `setupEventListeners()`
Sets up necessary event listeners for:
- Fullscreen state changes (updates button)
- Button clicks (triggers toggle)

#### `updateButtonVisibility()`
- Updates button text based on current fullscreen state
- Manages visibility (shown only on mobile when not in fullscreen)
- Applies/removes 'visible' CSS class

#### `isTouchDeviceCheck()`
- Detects mobile/touch devices using multiple methods:
  - Touch events support
  - Max touch points
  - CSS pointer media query
- Returns boolean (true for touch devices)