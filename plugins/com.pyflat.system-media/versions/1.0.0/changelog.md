## System Media 1.0.0

The first release. System Media connects Macro Deck's **Music Player** widget to whatever is playing on your computer, through the system's own media controls. There is nothing to set up for most apps.

### Works with
- **Windows:** every app in the media overlay (Spotify, browsers, Apple Music, TIDAL, foobar2000, MusicBee, ...), several at once.
- **macOS:** the app Now Playing shows (needs `brew install media-control`).
- **Linux:** every MPRIS player (Spotify, Firefox, Chromium, VLC, Rhythmbox, Elisa, ...).
- **SMPlayer and mpv**, which the system doesn't see, are supported directly.

### Features
- **Widget instances:** pick *Any app* to follow whatever is playing, or pin a widget to one app. Apps are remembered, so a pinned widget keeps working while the app is closed.
- **Controls:** play/pause, next, previous, seek, shuffle, repeat and per-app volume (Windows and Linux), as widget buttons and as actions.
- **Several apps playing:** let an *Any app* widget cycle through them, with a `2/3` badge, or flip through them with the **Show the next playing app** action.
- **Variables and events:** variables for track, artist, album, position, volume and more. Events for track changes, playback state and switching apps, each narrowable to one app.
- **Cleaner browser info:** leftover covers and timelines from other tabs are hidden.
- **Exact YouTube info** (Windows, opt-in): shows the video you're actually watching instead of one you hovered over.
- **VLC on Windows:** a guided setup for the add-on VLC needs to report what it plays.

### Privacy
Nothing is sent anywhere by default. The README lists every network request and every file the plugin stores.

Missing a player? [Request it](https://github.com/PyFlat/System-Media/issues/new?template=player_request.yml).
