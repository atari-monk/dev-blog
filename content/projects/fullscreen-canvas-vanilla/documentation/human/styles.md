# Styles Documentation (High level overview)

## canvas-container 

This .canvas-container class is typically used as a fullscreen container for rendering canvas-based graphics (like animations, visual effects, or games) while making sure that any overflowing content is hidden. The black background helps create a "clean slate" or cinematic effect.

## canvas

Fill its container completely,  
Have no borders,  
Use a black background,  
And behave like a proper block-level visual element.  
Perfect setup for fullscreen graphics, games, animations, or effects when  the  canvas is inside something like .canvas-container.  

## fullscreen-button

The .fullscreen-button is a hidden, centered button styled for good UX/UI, designed to appear on top of fullscreen graphics (like a canvas). It blends in visually but remains legible and clickable when made visible.

## fullscreen-button.visible

.fullscreen-button.visible is a conditional style that makes a hidden button appear when the visible class is added — typically used to control UI dynamically.