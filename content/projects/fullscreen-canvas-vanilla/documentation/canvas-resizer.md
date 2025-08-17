# Canvas Resizer Documentation

## Functionality

The `CanvasResizer` class manages responsive resizing of an HTMLCanvasElement, ensuring it maintains proper dimensions and pixel density when its container size changes. Key features:

- Automatically handles container resize events with debouncing
- Maintains high DPI/retina display support via devicePixelRatio
- Dispatches custom events when resizing occurs
- Clean resource management for proper cleanup

## Implementation Details

### Public Methods

#### `constructor(canvas: HTMLCanvasElement)`
- Initializes the resizer with a target canvas element
- Sets canvas CSS dimensions to 100% of its container
- Sets up resize observers and performs initial resize

#### `resize(): void`
- Calculates new canvas dimensions based on:
  - Current container size (via getBoundingClientRect)
  - Device pixel ratio
- Only updates canvas dimensions if they've actually changed
- Dispatches "canvas-resized" event when changes occur

#### `destroy(): void`
- Cleans up all resources:
  - Cancels any pending resize timers
  - Disconnects the ResizeObserver
- Should be called when the resizer is no longer needed

### Private Methods

#### `setupEventListeners(): void`
- Initializes ResizeObserver to monitor canvas container
- Implements debounced (100ms) resize handling
- Prevents multiple rapid resize operations

#### `dispatchResizeEvent(): void`
- Creates and dispatches a "canvas-resized" CustomEvent with details:
  - New canvas width (in pixels)
  - New canvas height (in pixels)
  - Current device pixel ratio

## Event System

The class dispatches a "canvas-resized" event on the canvas element whenever dimensions change. The event includes:

```typescript
{
    detail: {
        width: number,    // New canvas width in pixels
        height: number,   // New canvas height in pixels
        pixelRatio: number // Current device pixel ratio
    }
}
```

## Usage Example

```typescript
const canvas = document.getElementById('myCanvas') as HTMLCanvasElement;
const resizer = new CanvasResizer(canvas);

canvas.addEventListener('canvas-resized', (e) => {
    console.log('Canvas resized to:', e.detail);
});

// When done:
// resizer.destroy();
```
