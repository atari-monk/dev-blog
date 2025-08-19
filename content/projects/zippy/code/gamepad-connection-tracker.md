# Gamepad Connection Tracker

## Functionality
- Tracks connected/disconnected gamepads and maintains their current state.
- Provides access to gamepad data.
- Handles browser gamepad connection/disconnection events.

## Implementation

### Public Methods

#### `constructor`
- Binds event handlers for gamepad connections/disconnections.
- Sets up event listeners.
- Initializes gamepad state by calling initial update.

#### `getGamepad(index: number = 0)`
- Returns the gamepad at the specified index from internal storage.
- Returns `null` if index is invalid or no gamepad exists.

#### `getConnectedGamepads`
- Returns an array of all currently connected gamepads by querying `navigator.getGamepads()` directly.

#### `update`
- Refreshes the stored gamepad data from `navigator.getGamepads()`.

#### `destroy`
- Removes event listeners.
- Clears stored gamepad data.

### Private Properties/Methods

#### `boundHandleGamepadConnected`
- Pre-bound event handler for gamepad connected events.

#### `boundHandleGamepadDisconnected`
- Pre-bound event handler for gamepad disconnected events.

#### `setupEventListeners`
- Adds event listeners for 'gamepadconnected' and 'gamepaddisconnected' events.

#### `removeEventListeners`
- Removes the gamepad connection event listeners.

#### `handleGamepadConnected`
- Handles gamepad connection events, logs the event, and updates gamepad state.

#### `handleGamepadDisconnected`
- Handles gamepad disconnection events, logs the event, and updates gamepad state.

--- 

This class provides a clean interface for managing gamepad connections and accessing their data while handling the underlying event management. Note that `getGamepad()` uses internally stored data while `getConnectedGamepads()` queries live data directly from the browser.