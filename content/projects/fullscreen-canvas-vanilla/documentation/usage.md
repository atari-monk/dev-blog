# Usage

## Install

Install required dependency on zippy-shared-lib

```
pnpm add zippy-shared-lib
```

Install component

```
pnpm add fullscreen-canvas-vanilla
```

Check package.json (versions may differ)

```json
"dependencies": {
    "fullscreen-canvas-vanilla": "^0.0.9",
    "zippy-shared-lib": "^0.1.8"
}
```

## Index.html

Put component in index.html

```html
<div id="canvas-container" class="canvas-container">
    <canvas id="game-canvas"></canvas>
</div>
```

## Test scene

To test if component is working save this code in cross-lines-scene.ts  

```ts
import type { EngineHook, FrameContext } from "zippy-shared-lib";

export class CrossLinesScene implements EngineHook {
    private lineColor: string = "green";
    private lineWidth: number = 3;

    frameTick(context: FrameContext): void {
        this.renderBackground(context);
        this.renderLines(context);
    }

    private renderBackground(context: FrameContext): void {
        const { ctx, width, height } = context;
        ctx.fillStyle = "#222";
        ctx.fillRect(0, 0, width, height);
    }

    private renderLines(context: FrameContext): void {
        const { ctx, width, height } = context;

        ctx.strokeStyle = this.lineColor;
        ctx.lineWidth = this.lineWidth;
        ctx.beginPath();

        ctx.moveTo(0, height / 2);
        ctx.lineTo(width, height / 2);

        ctx.moveTo(width / 2, 0);
        ctx.lineTo(width / 2, height);

        ctx.stroke();
    }
}
```

## Styles

Reset main styles to get fullscreen effect.

```css
html,
body,
#root {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: black;
}
```

## Main.ts

Import:
- main style
- component style
- factory
- test scene

```ts
import "./style.css";
import "fullscreen-canvas-vanilla";
import { createGameCanvas } from "fullscreen-canvas-vanilla";
import { CrossLinesScene } from "./cross-lines-scene";
```

Use factory

```ts
createGameCanvas("canvas-container", "game-canvas", new CrossLinesScene());
```

## Run and test

```sh
pnpm dev
```

Test:
- Open page and check if there is a green cross
- Canvas with cross should scale to any window size
- Press F11 on desktop to see if it scales to fullscreen
- On mobile there should be a button for fullscreen
- Go fullscreen - button should be hidden
- Canvas should fill screen in portrait and horizontal modes
