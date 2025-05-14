# Creative Coding

- **Embrace imperfection.** Build prototypes with messy code or unconventional logic.
- **Steal time.** Write a tiny script, sketch a UI idea, or experiment with a new library in 10-minute bursts.
- **Explore constraints.** Try a language, framework, or paradigm you’ve avoided.

```javascript
// Example: A "useless" generative art snippet
function sketch() {
  noLoop();
  background(0);
  for (let i = 0; i < 100; i++) {
    fill(random(255), random(255), random(255));
    ellipse(random(width), random(height), random(50));
  }
}
```

```python
# Example: Brutally simple ASCII art generator
import random
chars = ['*', '#', '.', '|']
for _ in range(20):
    print(''.join(random.choice(chars) for _ in range(40)))
```

**Constraints:**
- No production use
- No tests
- No documentation