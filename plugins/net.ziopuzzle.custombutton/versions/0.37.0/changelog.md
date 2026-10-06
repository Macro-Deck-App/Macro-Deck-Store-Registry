# Custom Button v0.37.0 — Easier action setup and improved editing
## Action configuration
- New "Set display value" and "Set display data from JSON" actions automatically use the widget’s Channel.
- Changing the sidebar Channel also updates matching channels in existing display-data actions, including nested loops and branches. Other channels remain unchanged.
- Added Target this widget in all events to update all event widget targets in one click while preserving other conditions.
## Copying and importing widgets
- Automatically correct event targets matching the source widget’s ID when opening a copied or imported widget’s configuration. References to other widgets remain unchanged.
- Show a prominent red notice above the bulk-target button when corrections are made.
- Enable saving these corrections without manually editing another field.
To use automatic correction: save the source widget once with this version before copying or exporting it, then open and save the destination’s configuration. Older data without a recorded source ID can still use the bulk-target button.
## GUI editor
- Improved Undo/Redo grouping: continuous changes to one field form a single step; switching fields or pausing starts another.
- Expanded history to 100 steps and disabled unavailable Undo/Redo buttons.
- Undo can discard incomplete property input while keeping the last valid layout.
- Error messages now identify the component, ID, and XML line/column. Duplicate IDs report both definition locations.
- Applying invalid XML selects the offending line for easier correction.
