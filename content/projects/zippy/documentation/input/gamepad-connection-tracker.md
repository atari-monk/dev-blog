# Gamepad Connection Tracker Documentation

## Functionality
- Tracks connected/disconnected gamepads and maintains their current state.
- Provides access to gamepad data.

## Implementation

### Public Methods

#### `constructor()`
- Binds event handlers for gamepad connections/disconnections.
- Sets up event listeners.
- Initializes gamepad state.

#### `getGamepad(index: number = 0): Gamepad | null`
- Returns the gamepad at the specified index.
- Returns `null` if index is invalid or no gamepad exists.

#### `getConnectedGamepads(): Gamepad[]`
- Returns an array of all currently connected gamepads.

#### `destroy(): void`
- Removes event listeners.
- Clears stored gamepad data.

### Private Methods

#### `setupEventListeners(): void`
- Adds event listeners for 'gamepadconnected' and 'gamepaddisconnected' events.

#### `removeEventListeners(): void`
- Removes the gamepad connection event listeners.

#### `handleGamepadConnected(e: GamepadEvent): void`
- Handles gamepad connection events, logs the event, and updates gamepad state.

#### `handleGamepadDisconnected(e: GamepadEvent): void`
- Handles gamepad disconnection events, logs the event, and updates gamepad state.

#### `update(): void`
- Refreshes the stored gamepad data from the browser's current state.

--- 

This class provides a clean interface for managing gamepad connections and accessing their data while handling the underlying event management.