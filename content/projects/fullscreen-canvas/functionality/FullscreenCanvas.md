* Creates a fullscreen canvas that fills the entire window.  
* Dynamically adjusts the canvas size when the window is resized.  
* Renders frames using a provided `draw` function, passing canvas context, dimensions, and timing information.  
* Supports optional looping animation via `requestAnimationFrame`.  
* Detects touch devices and shows a button to enter fullscreen mode when applicable.  
* Handles fullscreen mode requests and updates the UI accordingly.  
* Clears the canvas before each frame and tracks time between frames for animation purposes.  
* Cleans up event listeners and animation frames when the component unmounts.