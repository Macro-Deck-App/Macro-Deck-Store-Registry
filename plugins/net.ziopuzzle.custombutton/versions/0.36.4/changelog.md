# Custom Button v0.36.4 — Variable-driven SVG and image improvements

## New features
- Added an SVG component with variable bindings and expressions for text, colors, and geometry.
- Added SVG editing to the GUI editor and a BASIC Variable SVG template.
- Added optional image and SVG tinting through color, including variable bindings, conditional styles, transparency, and color transitions. Leave the color unset to preserve the original colors.
## Improvements and fixes
- Fixed image and SVG alignment in horizontal and vertical stacks. Elements now use a square footprint based on size, allowing stack alignment to position them correctly.
- Fixed transparent pixels showing a background color or obscuring lower layers when using image cover or zoom.
- Fixed repeated Use this widget selections leaving $self in Custom Button event targets instead of the current widget’s ID.
## Notes
- Existing layouts that relied on images occupying extra space may need explicit fill or mainSize settings.
- SVG supports self-contained shapes, paths, text, gradients, and clipping paths. Scripts, external references, embedded images, and stylesheets are not supported. Variable-driven SVG updates are limited to five renders per second per element. (It is converted to an image internally and sent to the client)
- On Macro Deck beta.15, image tinting requires client mask support and disables artwork crossfade.
