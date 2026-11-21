# Custom Button 0.49.0

This release adds shared display values for widgets and modals on any channel. You can change a theme color from one action, rerun a widget's initialization after editing, and jump directly to a field that causes a preview error.

## Shared display values

- Open **Integrations > Custom Button** and enter `{"themeAccent":"#54dfcc"}` in **Shared values (JSON)**. Use `color="{{themeAccent}}"` in any widget or modal layout. Changing the shared color updates open displays that use it, and the setting persists across restarts.
- Use the new **Set shared display value** action to update one key from a button, automation, or variable binding. Save the integration settings once before the first action write. An empty `{}` is enough.
- Values are resolved per top-level key, in this order: **live channel value → widget or modal initial JSON → shared value**. This lets an individual widget override a shared color. The layout editor includes shared keys in suggestions and preview checks, and **Diagnostics** shows where each value came from.

## Widget initialization and actions

- On the **Actions** tab, click **Trigger Display activated** next to **Target this widget in all events** to rerun the widget's matching saved flows. Use it to refresh a track title, artwork colors, or other initial data after editing a widget or updating the plugin.
- **Set display data from JSON** now accepts hex colors produced by unquoted property-value bindings. A music player can set its track title and album colors in the same action.
- If an action edit is rejected, the editor restores the last accepted actions and shows the reason.

## Layout editor

- Invalid input marks the affected block and field. **Show field** focuses the property, and **Show in XML** selects its source. If an error blocks another edit, the original message stays visible. Validation also checks modifier sizes, conditional styles, responsive variants, and every row of a scroll-follow **Repeat**.
- Discard an incomplete property or unapplied XML while keeping valid edits. Formatting XML now leaves it in the editor until you apply it. If the editor disconnects or encounters a conflict, you can copy the XML from either tab before closing.
- **Restore previous drawing** recovers the layout and initial JSON after a template change while keeping the current channel and actions. Diagnostics also indicates when its results need refreshing after a draft change.
- The expression picker now includes arithmetic, comparison, and logical operators, with short descriptions and editable examples.

## Rendering fixes

- Visible local and HTTP images, including animated GIFs, and inline SVGs recover if Macro Deck loses their image registration. Animations whose resources are still available continue playing without restarting.
- Stacks with animated borders now support `background="transparent"` and translucent hex colors. The border and its contents stay visible.

## Compatibility

Built with Macro Deck SDK and CLI 3.0.1. The minimum supported Macro Deck version remains **3.0.0**.
