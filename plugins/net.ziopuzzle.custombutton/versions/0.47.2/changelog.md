# Custom Button v0.47.2
This update adds interactive modal views, scrollable layouts, text input, display-data transfer actions, image color extraction, and a new editor for variables and functions.
Requires Macro Deck 3.0.0-beta.17 or later.
## Modal views
- Added Show modal to display custom XML layouts on a connected device.
- Support live Channel data, interactive components, and an explicitly selected destination device.
- Added GUI layout editing to the Show modal action, including actions on standard Macro Deck buttons.
- Existing Channel values take priority over Initial JSON when opening a modal.
- Added Modal opened and Modal closed events for initialization and completion handling.
- Added custom close controls with optional result values and element IDs.
- New modal layouts include scrollable content and a Close control.
## Scrolling and text input
- Added the Scroll container with vertical and horizontal scrolling for both widgets and modals.
- Added Text Field, a single-line input with data binding, placeholder text, and interactive mode.
- Added Text changing and Text changed events with current and previous values.
- Added GUI properties and BASIC templates for the new components.
## Display-data transfer
- Added Copy display value to copy an individual value between Channels.
- Added Copy display data with merge and replace modes.
- Added Write display value to variable to write display data into an existing Macro Deck variable.
- Transfer actions include source-widget Initial JSON where configured, with live Channel values taking priority.
## Image colors and color expressions
- Added averageColorKey and averageColorFallback to extract average colors from local images, HTTP images, inline SVGs, and music-player artwork.
- Extracted colors become Channel data in live widgets and modals, making them available to drawing expressions and data-transfer actions.
- Artwork colors refresh independently of image downloads, approximately once per second while visible.
- Added color functions:
  - mixColor
  - shiftHue
  - setSaturation / scaleSaturation
  - setBrightness / scaleBrightness
  - setAlpha
- Color mixing supports linear RGB, sRGB, and HSV with shortest, increasing, or decreasing hue paths, including alpha-aware blending.
## Editor improvements
- Added a searchable variable/function editor with descriptions and usage examples.
- Edit the complete value directly and insert functions or data names at the current cursor or selection.
- Existing {{...}} bindings are respected without adding nested braces.
- Changes update the main GUI and preview while editing; closing the window keeps them.
- Binding-dependent rendering errors now show a warning instead of blocking editor changes. XML structure and duplicate IDs remain validated.
- Added search to template, input-target, and event-order selectors while retaining BASIC/ADVANCED template labels.
## Notes
- When opening a modal from a Custom Button event, select a Destination device.
- Modal closed requires Wait until closed (emit Modal closed) in the Show modal action.
- Modal GUI changes must be applied and saved, then the modal reopened to see layout changes.
- Icon Pack images remain supported for display, but average-color extraction is not available for them.
- Artwork colors may remain cached when the player replaces image content without changing its artwork ID.
