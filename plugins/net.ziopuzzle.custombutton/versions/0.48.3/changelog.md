# Custom Button 0.48.3
This release adds repeatable layouts, array and object editing, and new text and array functions, alongside rendering and editor improvements.
## New features
- Repeat component: Generate elements from arrays, including arrays of objects. Access each item's properties, index and key, with customizable local variable names. Events from repeated controls include information about the selected item.
- Structured data editing: Set display value now supports targets such as settings.volume and playlist[2].title. New actions let you insert or remove array items and object properties. Removed values can optionally be stored in a Macro Deck variable.
- Text and array functions: Added length, contains, startsWith, endsWith, replace, substring, lower, upper, trim, split, join, at and slice. Array-returning expressions can also supply Repeat content.
- Experimental scroll following: Follow an item index using a display-data value, with configurable item offset and delay. Start/end scroll anchoring is also available.
## Rendering improvements
- Image and SVG elements can use frame="container" to fit their parent's rectangular area instead of a square frame. Existing layouts retain square framing by default.
- Added opt-in text shadows in modals without introducing rounded corners around the modal content.
## Editor and usability improvements
- Fields that specify data names now use direct name selection instead of opening the variable/function editor.
- Repeat's array source supports both name selection and expression editing.
- Added descriptions for Repeat variables and marked experimental scrolling settings.
- Clarified that Initial JSON supplies defaults when Channel values are absent, including after a value is removed.
- Write display value to variable now supports nested property and array targets.
## Notes
- Array and object editing actions operate on live Channel data. Initialize editable data using Set display data from JSON; rendering defaults alone do not initialize the Channel.
- Automatic scroll following is experimental. It may flicker or behave differently depending on timing and item sizes, and its configuration may change.
- Requires Macro Deck 3.0.0-beta.18 or later.
