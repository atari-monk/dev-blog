# Exports Documentation

## Core Imports
- `"./styles/fullscreen-canvas.css"` - Default styles for the fullscreen canvas (automatically imported)

## Types
- `FullscreenCanvasOptions` - Interface defining configuration options for the FullscreenCanvas

## Classes
- `FullscreenCanvas` - Main class that handles fullscreen canvas functionality

## Factory Functions
- `createGameCanvas` - Helper function to quickly create and configure a game canvas instance

## Detailed Usage

### Styles
File: `fullscreen-canvas.css`  
Description: Default CSS styles that are automatically applied to ensure proper fullscreen behavior  
Key features:
- Ensures canvas takes up 100% of viewport
- Removes default margins/padding
- Handles basic responsive behavior

### FullscreenCanvasOptions
Type: `interface`  
Description: Configuration options for the FullscreenCanvas instance  
Typical options include:
- `canvasElement`: Optional existing canvas element to use
- `autoResize`: Whether to automatically handle window resize events (default: true)
- `styles`: Custom CSS styles to apply (extends/overrides default styles)

### FullscreenCanvas
Type: `class`  
Description: The main class that manages a fullscreen canvas element  
Key methods:
- `initialize()` - Sets up the canvas and applies styles
- `cleanup()` - Removes event listeners and styles
- `getCanvas()` - Returns the canvas element

### createGameCanvas
Type: `function`  
Description: Factory function that creates and configures a FullscreenCanvas instance  
Parameters:
- `options`: FullscreenCanvasOptions (optional)
Returns: 
- Configured FullscreenCanvas instance with styles applied