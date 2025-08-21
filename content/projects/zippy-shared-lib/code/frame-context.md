# FrameContext Type

## Overview
The `FrameContext` type defines the rendering context and timing information for a single animation frame, providing essential data for canvas-based rendering operations.

## Type Definition

### FrameContext
```typescript
export type FrameContext = {
    readonly ctx: CanvasRenderingContext2D;
    readonly width: number;
    readonly height: number;
    readonly deltaTime: number;
    readonly totalTime: number;
};
```

## Properties

| Property | Type | Description | Read-only |
|----------|------|-------------|-----------|
| `ctx` | `CanvasRenderingContext2D` | The 2D rendering context of the canvas element | Yes |
| `width` | `number` | The width of the canvas in pixels | Yes |
| `height` | `number` | The height of the canvas in pixels | Yes |
| `deltaTime` | `number` | The time elapsed since the previous frame (in milliseconds) | Yes |
| `totalTime` | `number` | The total time elapsed since the animation started (in milliseconds) | Yes |

## Usage
The `FrameContext` type is typically used in animation loops and rendering functions to provide frame-specific information:

```typescript
function renderFrame(frame: FrameContext) {
    const { ctx, width, height, deltaTime, totalTime } = frame;
    // Rendering logic using the frame context
}
```

## Characteristics
- **Immutable**: All properties are marked as `readonly` to ensure frame data consistency
- **Canvas-focused**: Designed specifically for 2D canvas rendering operations
- **Time-aware**: Includes both delta time and total time for animation control

## Dependencies
- Built-in TypeScript types
- Standard Canvas API types (`CanvasRenderingContext2D`)

## Export
This type is exported as a named export and can be imported using:
```typescript
import { FrameContext } from './frame-context';
```