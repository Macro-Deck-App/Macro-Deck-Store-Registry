# Custom Button 0.35.1
This release adds new drawing components, adaptive layouts, improved image support, and higher layout limits.
Requires Macro Deck 3.0.0-beta.15 or later.
## New components and drawing features
- Gauge: Create arc gauges with data-bound values and animated transitions.
- Icon: Display built-in icons with configurable names, sizes, colors, and transparency.
- Transform: Rotate, scale, and move groups of elements, with animation support.
- Modifier: Apply padding, clipping, size constraints, opacity, and disabled states.
- Responsive layouts: Select layout variants based on the available width, height, or aspect ratio.
- Dynamic text: Display time and dates that update on the client.
- Range bars: Set a custom start value and an optional marker.
- Line gradients
## Improved image support
- Use the beta.15 SDK APIs to display images from installed Icon Packs and artwork from other music players.
- Continue using supported host image paths or the artwork: source format.
- Try the new Image sources template for Icon Pack images, local files, and music-player artwork.
## Larger layouts
- Increased XML limits to 65,536 characters, 512 elements, and 32 nesting levels.
- Added checks for generated rendering data to report excessive size or depth before sending it to the host.
Actual rendering limits also depend on the generated component tree; not every layout reaching the XML limits can be rendered.
## Editor and template improvements
- Added editor controls and examples for the new components.
- Updated the clock, icon, transform, modifier, and responsive layout examples.
- Unified layout component colors in the editor.
