# Custom Button 0.48.6

## Compatibility

- Updated the Macro Deck SDK and CLI to the stable 3.0.0 release.
- **Macro Deck 3.0.0 or later is now required.**

## Event targets

- New Custom Button events use **This widget** (`$self`) as their target. These events follow the widget when it is copied or imported.
- Existing Custom Button events that target their own widget are converted to `$self` when you open and save the widget settings. Events targeting other widgets remain unchanged.
- For older copied or imported widgets, open and save the destination settings to apply target corrections based on the recorded source widget ID.

## Variable output

- **Write display value to variable** and **Remove display value** can now prefer a variable local to the current script or automation.
- The existing widget-first and global choices remain available. Existing actions keep their previous widget-first default.

## Rendering fixes

- Fixed transform animations that could stop updating on clients when the rotation angle was very large, such as an angle calculated from a Unix timestamp. Rotation direction and multi-turn animations are preserved.
- Improved handling of large rotation and skew angles in SVG transforms and supported arc paths.
