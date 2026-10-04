## Printer Control 1.0.0

### Widgets
- **Printer status:** a progress ring with percentage and time left while printing, and the file and finish time on wide tiles. When idle, hotend and bed gauges fill as they heat. Fits square, wide and tall tiles.
- **Printer webcam:** your printer's camera on the deck, with the print progress drawn on top.

### Actions
- Pause, resume, cancel or restart a print, or start a file from the printer.
- Preheat with OctoPrint's temperature presets, set temperatures, or cool down.
- Home, move the print head, extrude or retract.
- Set the part cooling fan, feed and flow rates.
- Send G-code, connect or disconnect the printer, run system commands, and switch lights and relays (with the GPIO Control plugin).
- Buttons can follow the job, the connection or a light, with their own label, colors and icon per state.

### Variables and events
- Status, progress, time left, finish time, file, Z height and all temperatures, ready for the history graph.
- Events when a print starts, finishes, fails, is cancelled, paused or resumed, plus progress, connection and error events.

### Setup
- Enter your OctoPrint address and approve Macro Deck in OctoPrint. Pasting an API key works too.
- Any number of printers

Works on Windows, macOS and Linux. Requires OctoPrint, and an MJPEG stream for the webcam (OctoPi's default).


**Full Changelog**: https://github.com/PyFlat/Printer-Control/commits/v1.0.0
