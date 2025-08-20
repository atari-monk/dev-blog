# EngineHook Interface

**Action Taken:** Generated new documentation.

## Documentation for `engine-hook.ts`

### Overview
The `engine-hook.ts` file defines the core interface for engine hooks in the system. Engine hooks provide a way to execute code on each frame tick with access to the current frame context.

### Interface: `EngineHook`

#### Description
The `EngineHook` interface defines a contract for objects that need to perform operations on each frame tick. Implementing this interface allows objects to participate in the engine's frame processing loop.

#### Method: `frameTick(context: FrameContext): void`

**Purpose:**  
Called by the engine on each frame update to perform frame-based operations.

**Parameters:**
- `context` (FrameContext): The frame context object containing information about the current frame state

**Returns:**  
`void` - This method does not return a value

**Usage:**
```typescript
class MyEngineHook implements EngineHook {
    frameTick(context: FrameContext): void {
        // Perform frame-based operations here
        console.log(`Frame ${context.frameNumber} processed`);
    }
}
```

### Dependencies
- **FrameContext**: Imported from `./frame-context` module, provides contextual information about the current frame

### Implementation Notes
- Classes implementing `EngineHook` should ensure the `frameTick` method is efficient as it executes every frame
- The method should avoid heavy computations that could impact frame rate
- Multiple engine hooks can be registered with the engine to create complex frame-based behaviors

### Typical Use Cases
- Animation controllers
- Input handling systems
- Game state updates
- Visual effects processing
- Performance monitoring tools