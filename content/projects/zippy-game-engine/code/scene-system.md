# Scene System

## Functionality

- Manages game scenes (levels/menus) and transitions between them.
- Tracks currently active scene.
- Provides scene registration and querying capabilities.
- Notifies subscribers when scene changes occur.

## Implementation

### Public methods

#### Constructor

- Initializes empty scene map and callback set

#### registerScene

- Registers a new scene with the system.
- Initializes the scene if it has an `init` method.
- Stores scene in internal map keyed by name.
- Parameters: `name: string`, `sceneModule: Scene`
- Return: `void`

#### transitionToScene

- Transitions to specified scene if it exists.
- Calls `onExit` on current scene (if exists).
- Calls `onEnter` on new scene (if exists).
- Notifies all scene change subscribers.
- Parameters: `name: string`
- Returns: `boolean` indicating success/failure

#### availableScenes (getter)

- Returns array of registered scenes with their names and display names.
- Return: `Array<{ name: string; displayName: string }>`

#### activeScene (getter)

- Returns name of currently active scene.
- Return: `string | undefined`

#### currentScene (getter)

- Returns reference to current scene object.
- Return: `Scene | undefined`

#### onSceneChange

- Registers callback to be notified when scene changes.
- Parameters: `callback: () => void`
- Returns: `() => void` unsubscribe function

### Private methods

#### #notifySceneChange

- Internal method to notify all registered callbacks when scene changes.
- Return: `void`