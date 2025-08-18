# Time Calculator Documentation

## Functionality

The TimeCalculator class provides time tracking utilities for animation/game loops. It calculates:

- `deltaTime`: Time elapsed since last frame (in seconds)
- `totalTime`: Total accumulated time since last reset (in seconds)
- `lastTime`: Timestamp of the last frame (in milliseconds)

## Implementation Details

### Public Methods

#### `calculate(time: number): TimeData`

Calculates and returns time metrics for the current frame:

1. On first call, initializes `lastTime` with the current timestamp
2. Computes `deltaTime` as the difference between current and last timestamp (converted to seconds)
3. Updates `lastTime` with current timestamp
4. Accumulates `deltaTime` into `totalTime`
5. Returns an object containing all time metrics

**Parameters:**
- `time`: Current timestamp in milliseconds (typically from performance.now() or Date.now())

**Returns:**
- `TimeData` object with:
  - `deltaTime`: number - Time since last frame in seconds
  - `totalTime`: number - Total elapsed time since reset in seconds
  - `lastTime`: number - Last frame timestamp in milliseconds

#### `reset(): void`

Resets all internal time tracking:
- Sets `lastTime` to 0
- Sets `totalTime` to 0

### Internal State

- `lastTime`: Stores timestamp of the previous frame (milliseconds)
- `totalTime`: Accumulates total elapsed time (seconds)

### Usage Notes

- Designed to be called once per animation/game frame
- Typically used with `requestAnimationFrame` or similar loop mechanisms
- First call will return a `deltaTime` of 0 (since there's no previous frame)