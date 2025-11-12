# 🧩 Procedural Programming — Quick Cheat Sheet

### **Definition**

**Functions + Data** > Objects
Explicit, predictable, testable.

---

## **Core Principles**

| Icon | Principle                     | Key Idea                                      |
| ---- | ----------------------------- | --------------------------------------------- |
| 🗂️  | **Separate Data & Functions** | `struct`s store data, functions operate on it |
| 🔄   | **Explicit Flow**             | Clear sequence of function calls              |
| 🧱   | **Predictable Data**          | Flat memory → fast & simple                   |
| ⚡    | **Pure / Explicit Effects**   | Return new data or modify passed-in data      |
| ✅    | **Testable & Reasonable**     | Self-contained functions                      |

---

## **Example: Entity Physics (C)**

```c
typedef struct { float x,y; } v2;
typedef struct { int id; v2 pos,vel; float mass; } Entity;

Entity SimulateEntity(Entity e, float dt){
    e.pos.x += e.vel.x*dt; e.pos.y += e.vel.y*dt;
    e.vel.x *= 0.98f; e.vel.y *= 0.98f;
    if(e.pos.x<0){ e.pos.x=0; e.vel.x*=-0.5f; }
    if(e.pos.x>800){ e.pos.x=800; e.vel.x*=-0.5f; }
    return e;
}
```

**Usage:**

```c
Entity e={1,{100,0},{30,0},1};
for(int i=0;i<5;i++) e=SimulateEntity(e,0.016f);
```

---

## **Traits at a Glance**

| 🔹  | Trait                | Why It Matters                     |
| --- | -------------------- | ---------------------------------- |
| 🗄️ | Simple containers    | Structs/arrays, no classes         |
| 🔧  | Explicit ops         | Easy to follow modifications       |
| 🚫  | No hidden effects    | All state changes visible          |
| 🎯  | Pure functions       | Deterministic → testable           |
| ↔️  | Flat control         | Direct calls, no inheritance magic |
| ⚡   | Performance-friendly | Cache-friendly layout              |
| 👀  | Readable             | Easy to maintain                   |

---

### **Summary**

✅ Focus: **Clarity, transparency, explicit control**
💡 Ideal for **game loops, simulations, embedded systems**