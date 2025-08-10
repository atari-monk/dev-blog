# Gamepad Input Processor Documentation

## Functionality
- Handles gamepad input processing including buttons, axes, vibration, and dead zones

## Implementation

### Public methods

#### Constructor
- Initializes gamepad tracking, button/axis mappings, and dead zones

#### update
- Updates previous gamepad states and checks for new connections

#### isButtonDown
- Checks if a button is currently pressed

#### isButtonPressed 
- Checks if a button was just pressed this frame

#### isButtonReleased
- Checks if a button was just released this frame

#### getAxis
- Gets axis value with dead zone applied

#### setButtonMapping
- Maps a button action name to a button index

#### setAxisMapping
- Maps an axis action name to an axis index  

#### setDeadZone
- Sets dead zone threshold for an axis

#### vibrate
- Triggers gamepad vibration/rumble effect

### Private methods
- (No private methods beyond property declarations)