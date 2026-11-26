<a href="https://macro-deck.app/store/de.christianalpen.reaperdeck"><img alt="Open in the Macro Deck Store" src="https://assets.macro-deck.app/branding/Open%20in%20the%20Macro%20Deck%20Store%20Badge%20Dark.png" height="56"></a>

# ReaperDeck

A [Macro Deck](https://macro-deck.app) plugin that controls [REAPER](https://www.reaper.fm) through
REAPER's built-in web interface. No hotkeys, no window focus: REAPER reacts even while another program is
in front. Buttons show live state (playing, muted, locked, current marker, …).

*Unofficial plugin - not affiliated with or endorsed by Cockos.*

## Features

- **Run any REAPER command:** native actions, custom actions and ReaScripts, picked by name.
- **Transport:** play/stop, pause, record, repeat and more, with state-dependent icons and colors.
- **Item / Track:** mute, solo, lock, phase, loop source, item ruler, open in external editor … -
  lit while the selected items/tracks have the setting.
- **View, Toolbars, Insert:** show REAPER's windows, open/close toolbars (as toolbar or menu), insert markers and regions.
- **Markers and regions:** jump-to buttons named and colored like in REAPER, next/previous, name filters,
  markers / regions / both, four filter groups, and "set to cursor" (e.g. on Long Press).
- **Faders:** track volume, item volume, or whatever was clicked last - for Macro Deck's Slider widget.
- **Timecode tile:** the play/edit cursor in any of REAPER's time formats, colored by transport state,
  with playback rate and record mode.
- **Trigger** "REAPER context changed" (tracks / items / envelopes), e.g. to open the matching folder.
- **Render presets:** open the render dialog with a preset loaded.

## Requirements

- Macro Deck 3, REAPER on the same computer (Windows or macOS).
- For some features: the SWS extension, and cfillion's "Apply render preset" (ReaPack) for render presets.

## Setup

1. **REAPER:** Options → Preferences → Control/OSC/web → **Add** → *Web browser interface*. Note the port
   (default 8080).
2. **Macro Deck:** add the ReaperDeck integration. Enter host (`127.0.0.1`) and port; the dialog tests the
   connection.
3. **Scripts** (needed for item/track feedback, faders, extra timecode formats, marker colors, set markers,
   render presets): in the integration settings under *Advanced*, set the **REAPER resource path**
   (REAPER: Options → *Show REAPER resource path*), tick **Install/update REAPER scripts** and save.
   The scripts are copied to `Scripts/ReaperDeck`.
4. **In REAPER, once:** Actions → Show action list → *New action → Load ReaScript…* → choose
   `Scripts/ReaperDeck/ReaperDeck_Setup.lua` and run it. It adds all scripts to the action list.
   Repeat only when an update brings a new script.

Nothing needs to go into `__startup.lua`: ReaperDeck starts its background scripts in REAPER only while
buttons need them, and they stop by themselves when Macro Deck closes.

After a plugin update: save the integration settings once more (with *Install/update REAPER scripts*
ticked) and restart REAPER, so the new scripts are used.

## Tips

- **Adopt states and icons:** when adding an action to a button, let Macro Deck use the states and icon
  the action provides - that is where labels, colors and icons come from.
- **Faders:** in the Slider widget choose a *REAPER: … volume* variable, switch on *Show value*, and use
  variables in the label, e.g. `{{ vars.reaper_track_number }}: {{ vars.reaper_track_name }}`.
- **Go to + set on one button:** set up *Short Press* with "Go to marker", copy the block to *Long Press*
  and switch only *On press* to *Set it to the cursor*.

## Known limitations

- "Play, skip time selection" lights only for playback started from the deck.
- The fader's *Show value* and label are settings of Macro Deck's Slider widget and have to be set per slider.
- Tested on Windows with REAPER 7. Feedback from macOS users is welcome.

## License

See [LICENSE](LICENSE).

Developer documentation (German): [docs/ENTWICKLUNG.md](docs/ENTWICKLUNG.md).
