* Name: TypeScript Scene Implementation Generator  
* Purpose / Goal: Create a complete, production-ready TypeScript scene implementation for the Scenelet project based on a detailed specification.  
* Input Data:  
  - Scene Concept (Name, Description, Key Visual Elements, Motion Principles, Emotional Impact)  
  - Technical Specifications (Math/Physics, Rendering Techniques, Performance Considerations)  
  - Implementation Requirements (Class structure, TypeScript practices, State management)  
* Constraints / Requirements:  
  - Follow the same class structure as AnimatedCirclesScene.ts.  
  - Implement all Scene interface methods properly.  
  - Include appropriate configuration and state interfaces.  
  - Adhere to strict TypeScript practices (strict typing, access modifiers, modern ES6+ features).  
  - Maintain code quality (small methods, comments for complex logic, explicit types).  
* Task / Action:  
  - Refactor the provided scene specification into a fully implemented TypeScript class.  
  - Replace all placeholder items (e.g., [SceneName], [Display Name]) with actual implementation details.  
  - Ensure the code works with strict TypeScript compiler flags (strictNullChecks, noImplicitAny).  
* Expected Output / Format:  
  ```typescript  
  import type { GameEngine, Scene } from "zippy-game-engine";  

  interface [SceneName]Config {  
      // Configuration parameters  
  }  

  interface [SceneName]State {  
      // State properties  
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