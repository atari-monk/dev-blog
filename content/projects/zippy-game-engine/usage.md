# Usage

## Install

Install required dependencies

```sh
pnpm add zippy-shared-lib
pnpm add fullscreen-canvas-vanilla
pnpm add zippy-game-engine
```

Check package.json (versions may differ)

```json
"dependencies": {
    "zippy-shared-lib": "^0.1.8",
    "fullscreen-canvas-vanilla": "^0.0.9",
    "zippy-game-engine": "^1.0.6"
}
```

## Index.html

Put component in index.html

```html
<div id="canvas-container" class="canvas-container">
    <canvas id="game-canvas"></canvas>
</div>
```

## Test scenes

To test if component is working save this code in cross-lines-scene.ts and rotating-rect-scene.ts. 

```ts
import type { FrameContext } from "zippy-shared-lib";
import type { Scene } from "zippy-game-engine";

interface CrossLinesSceneConfig {
    lineColor: string;
    lineWidth: number;
}

export class CrossLinesScene implements Scene {
    name: string = "Cross Lines";
    displayName?: string;

    private config: CrossLinesSceneConfig = {
        lineColor: "green",
        lineWidth: 3,
    };

    init(): void {
        console.log("Initializing Cross Lines Scene");
    }

    onEnter(): void {}

    onExit(): void {}

    update(_deltaTime: number): void {}

    render(context: FrameContext): void {
        this.renderBackground(context.ctx);
        this.renderLines(context.ctx);
    }

    resize(): void {}

    private renderBackground(ctx: CanvasRenderingContext2D): void {
        ctx.fillStyle = "#222";
        ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    }

    private renderLines(ctx: CanvasRenderingContext2D): void {
        ctx.strokeStyle = this.config.lineColor;
        ctx.lineWidth = this.config.lineWidth;
        ctx.beginPath();

        this.drawHorizontalLine(ctx);
        this.drawVerticalLine(ctx);

        ctx.stroke();
    }

    private drawHorizontalLine(ctx: CanvasRenderingContext2D): void {
        ctx.moveTo(0, ctx.canvas.height / 2);
        ctx.lineTo(ctx.canvas.width, ctx.canvas.height / 2);
    }

    private drawVerticalLine(ctx: CanvasRenderingContext2D): void {
        ctx.moveTo(ctx.canvas.width / 2, 0);
        ctx.lineTo(ctx.canvas.width / 2, ctx.canvas.height);
    }
}
```

```ts
import type { FrameContext } from "zippy-shared-lib";
import type { Scene } from "zippy-game-engine";

interface RotatingRectSceneConfig {
    rectSize: number;
}

export class RotatingRectScene implements Scene {
    name: string = "Rotating Rectangle";
    displayName?: string;

    private config: RotatingRectSceneConfig = {
        rectSize: 200,
    };

    init(): void {
        console.log("Initializing Rotating Rectangle Scene");
    }

    onEnter(): void {}

    onExit(): void {}

    update(_deltaTime: number): void {}

    render(context: FrameContext): void {
        this.renderBackground(context.ctx);
        this.renderRotatingRect(context);
    }

    resize(): void {}

    private renderBackground(ctx: CanvasRenderingContext2D): void {
        ctx.fillStyle = "#222";
        ctx.fillRect(0, 0, ctx.canvas.width, ctx.canvas.height);
    }

    private renderRotatingRect(context: FrameContext): void {
        const { ctx, width, height, totalTime } = context;

        ctx.fillStyle = `hsl(${(totalTime * 50) % 360}, 100%, 50%)`;
        ctx.save();
        ctx.translate(width / 2, height / 2);
        ctx.rotate(totalTime);
        ctx.fillRect(
            -this.config.rectSize / 2,
            -this.config.rectSize / 2,
            this.config.rectSize,
            this.config.rectSize
        );
        ctx.restore();
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

- Setup Engine
- Setup Scenes
- Setup Canvas

```ts
import "./style.css";
import "fullscreen-canvas-vanilla";
import {
    createGameCanvas,
    type FullscreenCanvasOptions,
} from "fullscreen-canvas-vanilla";
import { GameEngine, GameEngineFactory } from "zippy-game-engine";
import { RotatingRectScene } from "./rotating-rect-scene";
import { CrossLinesScene } from "./cross-lines-scene";
import type { EngineHook } from "zippy-shared-lib";

window.addEventListener("load", async () => {
    const gameEngine = setupEngine();
    setupScenes(gameEngine);
    setupCanvas(gameEngine);
});

function setupEngine() {
    const gameEngineFactory = new GameEngineFactory();
    const gameEngine = gameEngineFactory.getGameEngine();
    return gameEngine;
}

function setupScenes(gameEngine: GameEngine) {
    gameEngine.registerScene("Cross Lines", new CrossLinesScene());
    gameEngine.registerScene("Rotating Rectangle", new RotatingRectScene());
    gameEngine.transitionToScene("Rotating Rectangle");
    gameEngine.transitionToScene("Cross Lines");
}

function setupCanvas(gameEngine: EngineHook) {
    const options: FullscreenCanvasOptions = { isAnimLoop: true };
    createGameCanvas("canvas-container", "game-canvas", gameEngine, options);
}
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
