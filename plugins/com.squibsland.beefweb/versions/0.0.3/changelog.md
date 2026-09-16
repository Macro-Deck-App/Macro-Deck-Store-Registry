## Features
- Display Artwork, Music Player Widget, and Track Metadata
- Support for foobar2000 and DeaDBeef
    -  _DeaDBeef is currently untested_
- 16 Actions
- 17 Variables
- 1 Event

### Actions
- Play: Resume the playback of the music
- Pause: Pause the playback of the music
- Toggle Play/Pause: Toggle between paused and playing, regardless of the previous state
- Next Track: Advance to the Next Track
- Refresh State: Force an update for the now playing data
- Set Volume: Set the volume from 0-100 (Note: this calculated from decibel to percent, and will only work if your player is set to decibel.)
- Volume Up
- Volume Down
- Seek: Set the playback to a specific second
- Toggle Shuffle: Enables/Disables shuffle. (Note: Due to some players having multiple shuffle states, this may use the wrong one)
- Set Repeat Mode: Changes the repeat mode (Note: Due to some players having more/less repeat modes, this may use the wrong one)
- Seek Relatively: Advance the playback position relative to its current location
- Set Volume Relatively: Increase/Decrease the volume relative to its current position 
- Set Active Playlist: Sets the current playing playlist, allowing you to play a specific or random song
- Play Item: Play a selected song based on its playlist. 

### Variables
All variables start with `beefweb_player`

- `current_album`
- `current_artist`
- `current_position`: Float of the position in seconds
- `current_track_name`
- `device_name`
- `device_type`
- `is_connected`
- `is_playing`
- `playback_state`
- `playlist`: This is the playlist ID, not the playlist name
- `playqueue_size`
- `progress_percentage`: A value from 0-100 for progress percent
- `player_rating`
- `repeat_mode`
- `shuffled_enabled` (Note: this is experiencing issues)
- `track_duration` Float of the track's length in seconds
- `player_volume` Calculated percent for the players volume

### Events
- Track Changed

**Full Changelog**: https://github.com/SquibsLand/MacroDeck-BeefWeb/commits/v0.0.3
