# Code Functionality Analysis

## `createGameCanvas` Factory Function (`factory.ts`)
- Creates a `FullscreenCanvas` instance with simplified configuration
- Takes container ID, canvas ID, game engine with `frameTick` method, and optional options
- Merges default options (like `loop: true`) with user-provided options
- Binds the game engine's `frameTick` method to maintain proper `this` context
- Provides a cleaner interface for creating game canvases compared to direct `FullscreenCanvas` instantiation

## `FullscreenCanvas` Class (`fullscreen-canvas.ts`)
### Core Functionality:
- Creates and manages a fullscreen canvas element
- Handles canvas resizing to match window dimensions
- Implements animation loop using `requestAnimationFrame`
- Provides frame timing information (deltaTime, totalTime)

### Fullscreen Features:
- Detects touch devices and shows/hides fullscreen button accordingly
- Implements fullscreen mode with fallbacks for different browsers
- Manages fullscreen button visibility based on current state

### Rendering:
- Clears canvas before each frame
- Invokes provided `frameTick` callback with rendering context and timing data
- Supports optional looping control (can be disabled via options)

### Lifecycle Management:
- Sets up event listeners for resize and fullscreen changes
- Provides `destroy()` method for clean-up (removes listeners, stops animation)

## Supporting Files
### CSS (`fullscreen-canvas.css`)
- Styles canvas container to be full viewport size
- Styles fullscreen button with responsive positioning
- Manages button visibility with `visible` class

### Type Definitions
- `FrameContext`: Provides rendering context and timing information to frame callbacks
- `FullscreenCanvasOptions`: Defines configuration interface for canvas instances

### Index (`index.ts`)
- Exports main functionality: `FullscreenCanvas` class, `FrameContext` type, and `createGameCanvas` factory

## Overall Purpose
Provides a complete solution for creating and managing fullscreen canvas applications with:
- Automatic resizing
- Animation loop management
- Fullscreen mode support (especially for mobile/touch devices)
- Clean interface for game/app developers to focus on rendering logic