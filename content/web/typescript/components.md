## Suggested Approach for Components:

```ts
class MyComponent {
  private element: HTMLElement;
  private clickHandler: (e: Event) => void;
  private resizeHandler: () => void;

  constructor(element: HTMLElement) {
    this.element = element;
    
    // Bind handlers to maintain 'this' context
    this.clickHandler = this.handleClick.bind(this);
    this.resizeHandler = this.handleResize.bind(this);

    // Add event listeners
    this.element.addEventListener('click', this.clickHandler);
    window.addEventListener('resize', this.resizeHandler);
  }

  private handleClick(e: Event) {
    // Handle click
  }

  private handleResize() {
    // Handle resize
  }

  destroy() {
    // Clean up event listeners
    this.element.removeEventListener('click', this.clickHandler);
    window.removeEventListener('resize', this.resizeHandler);
  }
}
```
