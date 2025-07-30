# TypeScript Scene Implementation Generator

Create a complete, production-ready TypeScript scene implementation for the Scenelet project based on the following specification:

## Scene Concept
**Name**: [Insert scene name]
**Description**: [Insert 1-2 paragraph description of the visual effect and user experience]
**Key Visual Elements**: [List main graphical components]
**Motion Principles**: [Describe movement/animation patterns]
**Emotional Impact**: [Describe intended emotional response]

## Technical Specifications
**Math/Physics**: [Specify any mathematical models, algorithms, or physics systems needed]
**Rendering Techniques**: [List required canvas rendering methods]
**Performance Considerations**: [Note any performance-sensitive aspects]

## Implementation Requirements
1. Use the exact same class structure as AnimatedCirclesScene.ts
2. Implement all Scene interface methods properly
3. Include appropriate configuration interface
4. Maintain state in a clearly defined state object
5. Follow these TypeScript practices:
   - Strict typing everywhere
   - Proper access modifiers
   - Clear interface definitions
   - Modern ES6+ features
   - Readable, maintainable code

## Example Output Format
```typescript
import type { GameEngine, Scene } from "zippy-game-engine";

interface [SceneName]Config {
    // TODO: Define configuration parameters
}

interface [SceneName]State {
    // TODO: Define state properties
}

export class [SceneName]Scene implements Scene {
    private readonly config: [SceneName]Config = {
        // Default configuration
    };

    private state: [SceneName]State = {
        // Initial state
    };

    public readonly name = "[Scene Name]";
    public readonly displayName = "[Display Name]";

    constructor(private game: GameEngine) {}

    public init(): void { /* ... */ }
    public onEnter(): void { /* ... */ }
    public onExit(): void { /* ... */ }
    public update(deltaTime: number): void { /* ... */ }
    public render(ctx: CanvasRenderingContext2D): void { /* ... */ }
    public resize(): void { /* ... */ }

    // Private methods follow...
}
```

## Quality Standards
- Code must work with `strictNullChecks: true` and `noImplicitAny: true`
- All types must be explicitly defined
- Methods should be small and focused (SRP)
- Include appropriate comments for complex logic
- Preserve all existing functionality patterns from AnimatedCirclesScene.ts

> Note: Replace all [bracketed] items with actual implementation details. Maintain the same code organization patterns as the reference implementation.

## Example Usage

For your "Cosmic Birth" example, you would fill the template like this:

```
## Scene Concept
**Name**: Cosmic Birth
**Description**: A visualization of universe formation starting from a singularity, expanding into galaxies and nebulae through mathematical patterns. Begins with a black canvas that gradually reveals cosmic structures.

**Key Visual Elements**: 
- Singularity point
- Expanding fractal patterns
- Galaxy spirals
- Nebula clouds
- Star particles

**Motion Principles**: 
- Slow initial expansion accelerating over time
- Fibonacci spiral patterns for galaxy arms
- Particle systems for star fields
- Perlin noise for nebula textures

**Emotional Impact**: Awe, wonder, and perspective about cosmic scale and origins.

## Technical Specifications
**Math/Physics**: 
- Mandelbrot set algorithms
- Fibonacci spiral calculations
- Particle systems with gravitational attraction
- Perlin noise for organic textures

**Rendering Techniques**: 
- Canvas 2D context drawing
- Gradient fills for nebulas
- Particle rendering
- Fractal path generation

**Performance Considerations**: 
- Limit fractal iteration depth based on performance
- Use object pooling for particles
- Implement level-of-detail scaling
```