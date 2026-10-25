Changes since 1.0.1

New
- Bundled icon pack: 51 flat white icons for every action and state, added to Macro Deck when you install the plugin.
- New plugin icon.
- New lighting effects: Fire, Ambient Awareness and Audio Meter.
- Go to mouse DPI stage: pick a stage from a list of your mouse's own stages, for example "Stage 2 (1200 DPI)".
- Cycle Synapse lighting effects: each press moves a device to the next effect you tick.
- Restart Razer Synapse: a button that restarts Synapse so Synapse control applies. Runs only when you press it.
- Synapse popups: after a profile switch, a lighting change or a DPI stage change from Macro Deck, Synapse shows its own on-screen popup. Turn it off with "Show Synapse popups" in the settings.
- New variables: razer_mouse_dpi_stage_number, razer_mouse_effect, razer_chroma_effect.

Improved
- DPI Up/Down and Go to DPI stage go through Synapse when Synapse control is on, so Synapse shows and saves the stage. Without Synapse control they set the stage on the mouse directly.
- The lighting effect variables show Off while the lighting is switched off.

Fixed
- Lighting "Off" now switches the lighting off like Synapse's own switch, instead of showing Fire on some keyboards.
- Restarting Synapse from the plugin no longer leaves Synapse control off at the next Windows sign-in.
- The Synapse control switch in the settings now shows as on after saving.

Other
- Built with Macro Deck SDK 3.0.0-beta.18.
