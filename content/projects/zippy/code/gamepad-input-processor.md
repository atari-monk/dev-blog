# Gamepad Input Processor

## Functionality
- Handles gamepad input processing including buttons, axes, vibration, and dead zones
- Manages gamepad connections and state tracking
- Provides button state detection (down, pressed, released)
- Applies dead zones to analog stick inputs
- Supports custom button and axis mapping

## Implementation

### Public methods

#### Constructor
- Initializes gamepad tracking, button/axis mappings, and dead zones
- Sets up default button mappings (A, B, X, Y, LB, RB, LT, RT, Back, Start, LStick, RStick, D-pad)
- Sets up default axis mappings (LeftStickX, LeftStickY, RightStickX, RightStickY)
- Configures default dead zones for all axes (0.2 threshold)

#### update
- Updates previous gamepad states and checks for new connections
- Captures current gamepad states for frame comparison

#### isButtonDown
- Checks if a button is currently pressed
- Accepts either button name string or numeric index
- Returns boolean indicating current pressed state

#### isButtonPressed 
- Checks if a button was just pressed this frame
- Compares current frame state with previous frame
- Returns true only on the frame when button is first pressed

#### isButtonReleased
- Checks if a button was just released this frame
- Compares current frame state with previous frame
- Returns true only on the frame when button is released

#### getAxis
- Gets axis value with dead zone applied
- Accepts either axis name string or numeric index
- Returns normalized value (0 if within dead zone, otherwise original value)

#### setButtonMapping
- Maps a button action name to a button index
- Allows custom button configuration

#### setAxisMapping
- Maps an axis action name to an axis index
- Allows custom axis configuration

#### setDeadZone
- Sets dead zone threshold for an axis
- Values below threshold are treated as zero

#### vibrate
- Triggers gamepad vibration/rumble effect
- Supports dual-magnitude vibration (weak/strong)
- Returns boolean indicating success/failure

### Private methods
- (No private methods beyond property declarations)
