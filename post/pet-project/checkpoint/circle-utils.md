# C:\Atari-Monk\project\checkpoint\src\utils\circle-utils.ts 

## Code Quality Check 2025-11-23

Point of this is to ensure i understand code well and to point out problems.  
Then AI will peer check it.

```ts
// Depends on Point
import { point, type Point } from "./point-math";
// Depends on ShapeStyle
import {
    DEFAULT_SHAPE_STYLE,
    mergeShapeStyle,
    type ShapeStyle,
} from "./shape-style";

// Main data structure, center of circle and its radius.
// Simplest way to describe circle.
export interface Circle {
    center: Point;
    radius: number;
}

// Util function to set and apply styles in 2d context based on style data
export function applyStyle(ctx: CanvasRenderingContext2D, style: ShapeStyle) {
    // Conditional fill style based on useFill flag
    if (style.useFill) {
        // Sets fill style (color) in 2d context
        // todo: rename style to name same as in context
        ctx.fillStyle = style.fillColor!;
        // Apply style
        ctx.fill();
    }
    // Conditional stroke style based on useStroke flag
    if (style.useStroke) {
        // Sets stroke style (color) and lineWidth in 2d context
        // todo: rename style to name same as in context
        ctx.strokeStyle = style.strokeColor!;
        ctx.lineWidth = style.strokeWidth!;
        // Apply style
        ctx.stroke();
    }
}

// This is util template function
// It ensures default and custom style mix is applayed to shape
// It begins path and calls path function
// Todo: This maybe should be shared standard for all utils
// I dont like callbacks but this seems simplest way
export function drawShape(
    ctx: CanvasRenderingContext2D,
    pathCallback: (ctx: CanvasRenderingContext2D) => void,
    style?: ShapeStyle
) {
    // Merging default and custom style
    const mergedStyle = mergeShapeStyle(DEFAULT_SHAPE_STYLE, style);

    // Begins 2d context Path
    ctx.beginPath();
    // Draws path with callback function
    pathCallback(ctx);
    // Applay state to path
    applyStyle(ctx, mergedStyle);
}

// Function with Path to draw circle
function circlePath(circle: Circle, ctx: CanvasRenderingContext2D) {
    // Destructures data for drawing circle
    // This is done evry frame but seems fine
    // I need data struct to define data even if drawing gets slower
    const { x, y } = circle.center;
    // Draws circle with canvas api
    // x, y center point, radius, full angle 0-360 deg
    ctx.arc(x, y, circle.radius, 0, 2 * Math.PI);
}

// Public api to draw circle
// Takes 2d context, circle data and style
export function drawCircle(
    ctx: CanvasRenderingContext2D,
    circle: Circle,
    style?: ShapeStyle
) {
    drawShape(ctx, (ctx) => circlePath(circle, ctx), style);
}

// Public api convinience function to use primitive lang values as circle data
// todo: I think i should provide functions on primitive values and use circle data destructuring when passing to them ?
export function drawCircleAt(
    ctx: CanvasRenderingContext2D,
    x: number,
    y: number,
    radius: number,
    style?: ShapeStyle
): void {
    drawCircle(ctx, { center: point(x, y), radius }, style);
}
```

## ✅ **FINAL PRODUCTION VERSION — `circle-utils.ts`** 2025-11-23

C:\Atari-Monk\project\checkpoint\src\utils\shape-utils.ts

```ts
import {
    type ShapeStyle,
    mergeShapeStyle,
    DEFAULT_SHAPE_STYLE,
} from "./shape-style";

export function applyStyle(ctx: CanvasRenderingContext2D, style: ShapeStyle) {
    if (style.useFill) {
        ctx.fillStyle = style.fillColor!;
        ctx.fill();
    }
    if (style.useStroke) {
        ctx.strokeStyle = style.strokeColor!;
        ctx.lineWidth = style.strokeWidth!;
        ctx.stroke();
    }
}

export function drawShape(
    ctx: CanvasRenderingContext2D,
    path: (ctx: CanvasRenderingContext2D) => void,
    style?: ShapeStyle
) {
    const merged = mergeShapeStyle(DEFAULT_SHAPE_STYLE, style);
    ctx.beginPath();
    path(ctx);
    applyStyle(ctx, merged);
}
```

C:\Atari-Monk\project\checkpoint\src\utils\circle-utils.ts

```ts
import { type Point } from "./point-math";
import { type ShapeStyle } from "./shape-style";
import { drawShape } from "./shape-utils";

export interface Circle {
    center: Point;
    radius: number;
}

export function createCircle(center: Point, radius: number): Circle {
    if (radius <= 0) {
        throw new Error("Invalid circle radius");
    }
    return { center, radius };
}

export function drawCircle(
    ctx: CanvasRenderingContext2D,
    circle: Circle,
    style?: ShapeStyle
) {
    drawShape(
        ctx,
        (ctx) =>
            ctx.arc(
                circle.center.x,
                circle.center.y,
                circle.radius,
                0,
                Math.PI * 2
            ),
        style
    );
}

export function drawCircleAt(
    ctx: CanvasRenderingContext2D,
    x: number,
    y: number,
    radius: number,
    style?: ShapeStyle
) {
    drawShape(ctx, (ctx) => ctx.arc(x, y, radius, 0, Math.PI * 2), style);
}
```
