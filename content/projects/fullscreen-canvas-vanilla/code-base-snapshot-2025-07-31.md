# Fullscreen Canvas System Snapshot

## Source

### canvas-resizer.ts
**Role:** Manages canvas dimensions to match window size.
**Key Capabilities:**
- Automatically resizes canvas on window resize
- Handles viewport dimension tracking

**Integration Points:**
- Depends on: BrowserEnvironment, EventSystem
- Used by: FullscreenCanvas

---

### default-render-strategy.ts
**Role:** Provides basic canvas clearing behavior.
**Key Capabilities:**
- Clears canvas before each frame
- Serves as fallback rendering strategy

**Integration Points:**
- Implements: RenderStrategy
- Used by: factory.ts (as default)

---

### event-system.ts
**Role:** Centralized event listener management.
**Key Capabilities:**
- Tracks and manages all event listeners
- Handles listener addition/removal
- Prevents duplicate registrations

**Integration Points:**
- Depends on: BrowserEnvironment, ListenerEntry
- Used by: CanvasResizer, FullscreenService, FullscreenCanvas

---

### factory.ts
**Role:** Creates and configures FullscreenCanvas instances.
**Key Capabilities:**
- Composes all system components
- Handles dependency injection
- Validates DOM elements

**Integration Points:**
- Depends on: All major system components
- Primary entry point for consumers

---

### fullscreen-canvas.ts
**Role:** Main system controller and public API.
**Key Capabilities:**
- Coordinates component initialization
- Manages system lifecycle
- Exposes render strategy switching

**Integration Points:**
- Depends on: EventSystem, FullscreenService, CanvasResizer, Renderer
- Primary export for external use

---

### fullscreen-service.ts
**Role:** Handles fullscreen mode functionality.
**Key Capabilities:**
- Manages fullscreen button UI
- Handles fullscreen transitions
- Detects touch device capabilities

**Integration Points:**
- Depends on: BrowserEnvironment, EventSystem
- Used by: FullscreenCanvas

---

### real-browser-environment.ts
**Role:** Concrete implementation of browser environment interface.
**Key Capabilities:**
- Wraps native browser APIs
- Provides cross-browser compatibility
- Implements all BrowserEnvironment methods

**Integration Points:**
- Implements: BrowserEnvironment
- Used by: factory.ts (as default)

---

### renderer.ts
**Role:** Manages the rendering loop and frame timing.
**Key Capabilities:**
- Handles animation frame scheduling
- Calculates frame timing metrics
- Coordinates rendering strategy execution

**Integration Points:**
- Depends on: BrowserEnvironment, RenderStrategy
- Used by: FullscreenCanvas

---

## Types

### browser-environment.ts
**Role:** Defines the interface for browser environment interactions, abstracting DOM and window APIs.
**Key Capabilities:**
- Provides methods for DOM manipulation (getElementById, createElement)
- Handles event listeners for window/document
- Manages fullscreen and animation frame APIs
- Detects device capabilities (touch support)

**Integration Points:**
- Implemented by: real-browser-environment.ts
- Used by: EventSystem, CanvasResizer, FullscreenService, Renderer

---

### frame-context.ts
**Role:** Defines the structure of rendering context passed to frame callbacks.
**Key Capabilities:**
- Contains canvas rendering context and timing information
- Provides dimensions of the rendering surface

**Integration Points:**
- Used by: RenderStrategy implementations, frameTick callbacks

---

### fullscreen-canvas-options.ts
**Role:** Configures the behavior of the FullscreenCanvas system.
**Key Capabilities:**
- Controls rendering loop activation
- Specifies frame callback and rendering strategy
- Allows browser environment customization

**Integration Points:**
- Used by: factory.ts, FullscreenCanvas

---

### listener-entry.ts
**Role:** Defines the structure for event listener registration.
**Key Capabilities:**
- Standardizes event listener configuration
- Supports both window/document and element targets

**Integration Points:**
- Used by: EventSystem

---

### render-strategy.ts
**Role:** Interface for custom canvas rendering strategies.
**Key Capabilities:**
- Defines contract for render implementations
- Enables pluggable rendering logic

**Integration Points:**
- Implemented by: DefaultRenderStrategy
- Used by: Renderer

---
