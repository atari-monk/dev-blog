Here's a basic proposal for a TypeScript ECS inspired by Unity's structure:

**Entity:**

```typescript
interface Entity {
  id: string;
  components: Map<string, Component>;
  tags: Set<string>;
}
```

**Component:**

```typescript
interface Component {
  // Base interface for all components
}

class Position implements Component {
  x: number;
  y: number;
}

class Health implements Component {
  value: number;
}
```

**System:**

```typescript
interface System {
  update(entities: Entity[], dt: number): void;
}

class MovementSystem implements System {
  update(entities: Entity[], dt: number) {
    entities.forEach(entity => {
      const position = entity.components.get("Position");
      if (position) {
        // Modify position based on other components or entities
      }
    });
  }
}

class HealthSystem implements System {
  update(entities: Entity[], dt: number) {
    entities.forEach(entity => {
      const health = entity.components.get("Health");
      if (health) {
        // Modify health based on other components or events
      }
    });
  }
}
```

**World:**

```typescript
class World {
  private entities: Map<string, Entity>;
  private systems: System[];

  constructor() {
    this.entities = new Map();
    this.systems = [];
  }

  createEntity(id: string) {
    this.entities.set(id, { id, components: new Map(), tags: new Set() });
  }

  addComponent(entityId: string, component: Component) {
    const entity = this.entities.get(entityId);
    if (entity) {
      entity.components.set(component.constructor.name, component);
    }
  }

  addTag(entityId: string, tag: string) {
    const entity = this.entities.get(entityId);
    if (entity) {
      entity.tags.add(tag);
    }
  }

  addSystem(system: System) {
    this.systems.push(system);
  }

  update(dt: number) {
    for (const system of this.systems) {
      const filteredEntities = Array.from(this.entities.values()).filter(
        entity => system.update(entity, dt)
      );
      system.update(filteredEntities, dt);
    }
  }
}
```

**Usage:**

```typescript
const world = new World();

const entity1 = world.createEntity("entity1");
world.addComponent(entity1, new Position(10, 5));
world.addComponent(entity1, new Health(100));

const entity2 = world.createEntity("entity2");
world.addComponent(entity2, new Position(20, 10));
world.addComponent(entity2, new Health(50));

world.addTag(entity1, "enemy");

world.addSystem(new MovementSystem());
world.addSystem(new HealthSystem());

world.update(0.1); // Update all entities and systems
```

This is a basic structure, and you can further customize it to fit your specific needs. Remember to handle edge cases, implement event systems, and optimize performance based on your project's requirements.

I hope this proposal helps you get started with building your TypeScript ECS!