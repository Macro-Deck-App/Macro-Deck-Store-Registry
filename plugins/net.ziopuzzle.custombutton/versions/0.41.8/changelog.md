# Custom Button v0.41.8
This release adds new interactive controls, improves the GUI editor and diagnostics, and introduces text outlines and shadows.
Requires Macro Deck 3.0.0-beta.16 or later.
## New controls
- Dial — adjust values using a rotary control.
- Toggle — switch between on and off states.
- Segmented — select between multiple options, with centered content by default.
- Trackpad — control two values on a two-dimensional surface.
  - Configure axis direction using left/right and top/bottom values.
  - Set independent snapping increments for each axis.
  - Handle Trackpad start, Trackpad changing, and Trackpad end events.
  - Access current, starting, and previous coordinates.
  - Optionally show the crosshair only while touching.
  - Preserve active gestures across compatible widget session replacements.
Slider, Dial, Toggle, and Segmented events now include previousValue for calculating changes. Existing published event IDs are preserved, with clearer display names.
## Drawing improvements
- Add Text outlines using strokeColor and strokeWidth.
- Enable Text shadows with shadow="true", including inside nested transparent stacks. Shadows are disabled by default.
- Customize the unfilled Gauge track with trackColor.
- Control text fill/outline and gauge level/track transparency independently.
- Animate outline width and outline/track colours.
## Editor and setup improvements
- Group component properties into sections such as content, layout, appearance, interaction, and animation.
- Show safe default values as placeholders without adding them to XML.
- Organize templates and component menus from simpler to more complex examples.
- Assign unique default channels to new widgets.
- Follow automatic channels when opening copied or imported widgets, including matching channels in nested display-data actions. Manually named channels remain unchanged.
- Update matching local event filters after unambiguous element ID renames in either the GUI or XML editor.
- Warn about event filters that reference missing elements.
## Diagnostics and unavailable data
- Add a Diagnostics tab with readable, deduplicated errors and a copyable report.
- Inspect display-data keys, types, values, and initial/live sources.
- Clear resolved preview errors, including temporary errors caused by editing XML.
- Add number(key, fallback), isNumber(key), and isNumeric(key) to calculations and conditions, plus type(key) in conditions.
- Add Slider and Dial fallback values for unavailable or nonnumeric bound data, without overwriting the source value.
## Upgrade notes
- Widgets now use a native button root, applying the host’s tile corners and clipping. Check layouts that intentionally draw beyond the tile edges.
- Gauge colour alpha now affects only the corresponding level or track. Use opacity to fade the entire gauge.
- Existing widgets keep their saved layouts. Select a template again to use its updated example.
- Save copied/imported widget settings to apply automatic channel and event-target corrections.
