```tsx
//App.tsx
import { useState } from "react";
import { FullscreenCanvas } from "@atari-monk/fullscreen-canvas";
import "@atari-monk/fullscreen-canvas/FullscreenCanvas.css";
import { PongGame } from "./PongGame";
import { AnotherGame } from "./AnotherGame";
import "./App.css";

export function App() {
    const [currentGame, setCurrentGame] = useState<string | null>(null);

    const getDrawFunction = () => {
        switch (currentGame) {
            case "pong":
                return PongGame.draw;
            case "another":
                return AnotherGame.draw;
            default:
                return PongGame.draw;
        }
    };

    const handleGameSelect = (game: string) => {
        setCurrentGame(game);
    };

    if (!currentGame) {
        return (
            <div className="game-selection-screen">
                <h1>Select a Game</h1>
                <div className="game-buttons">
                    <button onClick={() => handleGameSelect("pong")}>
                        Pong
                    </button>
                    <button onClick={() => handleGameSelect("another")}>
                        Another Game
                    </button>
                </div>
            </div>
        );
    }

    return (
        <div className="app">
            <FullscreenCanvas draw={getDrawFunction()} loop={true} />
            <button
                className="back-button"
                onClick={() => setCurrentGame(null)}
            >
                Back to Menu
            </button>
        </div>
    );
}
```

App.css  

```css
.game-selection-screen {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
    width: 100vw;
    background-color: #121212;
    color: white;
    gap: 2rem;
}

.game-selection-screen h1 {
    font-size: 3rem;
    margin-bottom: 2rem;
}

.game-buttons {
    display: flex;
    gap: 1rem;
}

.game-selection-screen button {
    padding: 1rem 2rem;
    font-size: 1.2rem;
    background-color: #6200ea;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
}

.game-selection-screen button:hover {
    background-color: #3700b3;
}

.back-button {
    position: fixed;
    top: 20px;
    left: 20px;
    padding: 0.5rem 1rem;
    background-color: rgba(0, 0, 0, 0.5);
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    z-index: 1000;
}

.back-button:hover {
    background-color: rgba(0, 0, 0, 0.8);
}
```

```tsx
export const AnotherGame = {
    draw: (ctx: CanvasRenderingContext2D, width: number, height: number) => {
        ctx.fillStyle = "#222";
        ctx.fillRect(0, 0, width, height);

        ctx.fillStyle = "#0f0";
        ctx.font = "48px Arial";
        ctx.textAlign = "center";
        ctx.fillText("Another Game", width / 2, height / 2);
    },
};
```