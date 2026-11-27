<img width="1920" height="1080" alt="IP Camera for Macro Deck 3" src="store/01-hero.png">

# IP Camera Plugin for Macro Deck 3

A Macro Deck 3 plugin that shows live IP camera pictures on a deck widget. It reads the camera on the
computer that runs Macro Deck and relays the frames to the deck, so a phone or tablet only ever talks
to Macro Deck.

The plugin was built for the Xiaomi Mi 360 1080p camera, and it accepts any camera that offers an HTTP
snapshot, an MJPEG stream, RTSP or ONVIF. Snapshot and MJPEG cameras need nothing else installed; RTSP
is converted with ffmpeg.

<a href="https://macro-deck.app/store/com.itaimarom.ip-camera">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://assets.macro-deck.app/branding/Open%20in%20the%20Macro%20Deck%20Store%20Badge%20Dark.png">
    <img alt="Open in the Macro Deck Store" src="https://assets.macro-deck.app/branding/Open%20in%20the%20Macro%20Deck%20Store%20Badge%20Light.png" height="56">
  </picture>
</a>

## Screenshots

These are real captures from Macro Deck 3 with the plugin installed, composed into Store slides. The
camera picture is a local test stream.

| | |
| --- | --- |
| ![The camera setup dialog with a stream URL and the connection check](store/02-setup.png) | ![A short press opens the camera in Macro Deck's modal with movement arrows](store/03-modal.png) |
| ![A camera wall filling a Macro Deck folder](store/04-wall.png) | ![A split camera tile with movement arrows](store/05-four.png) |

## What it adds to Macro Deck

- **A Camera widget**: one, two or four cameras on the same tile. Pick a camera per cell, choose whether
  the pictures fill their cell or fit inside it, and give the widget a label, background and colours. A
  short press on a picture opens that cell's camera in a modal as large as Macro Deck's fixed dialog box
  allows. The status overlay is available on every configured cell. Each cell can also show optional
  left, right, up and down arrows with their own opacity, so a Xiaomi or ONVIF camera can be moved from
  the deck. The arrows make the tile claim presses, so Macro Deck skips the tile's Short Press flow;
  choose a **Press script** to run actions while the arrows stay.
- **A video stream provider**: every configured camera is listed under Source in any widget or action
  that can show a video stream, not only in this plugin's own widget.
- **A camera setup flow**: one Macro Deck configuration entry per camera. The flow fetches one frame
  before saving, so a wrong URL, rejected credentials or a go2rtc stream that only offers H.265 is
  reported immediately. It also discovers ONVIF cameras on the LAN and resolves their RTSP or
  snapshot address. Stream quality can be a Low, Balanced or High preset, or Custom with your own frame
  rate and maximum width.
- **Offline feedback**: a camera that drops out shows "The camera is offline. Reconnecting." on its
  widget, and the plugin reports an integration issue with a Retry action.
- **A Save snapshot action**: writes the pressed camera's current picture as a JPEG. The folder is set
  per action; empty means `Pictures\IP Camera`.
- **A Show camera action**: opens a camera in the enlarged modal. It can name its camera, so a plain
  button opens a chosen one; left empty it opens the camera of the pressed widget.
- **A camera wall folder view**: replace a folder's widget grid with one camera or up to four in a
  configurable wall. Pick it in the folder's settings; see [Camera wall](#camera-wall).
- **Camera controls**: Move left, Move right, Move up, Move down and Stop actions for pan and tilt, plus
  Night vision auto/on/off. Each action can name its camera, so a plain button controls a camera that
  has no camera tile; left empty it controls the camera of the pressed widget. ONVIF cameras use
  `http://<address>/onvif/device_service` and may set the camera's own address when the stream goes
  through a relay. Xiaomi cameras move over the local miIO channel with the camera address and the
  device token from Mi Home, entered in the camera's advanced settings. The camera widget can also draw
  optional movement arrows, with an opacity slider, on every configured cell. A camera that only speaks
  a vendor API is not covered yet.
- **A status overlay** (optional, off for existing widgets): a small live dot and the age of the last
  frame on the tile, or "RECONNECTING" when the source drops. New widgets enable it by default. It can
  be turned off in the widget settings, and a background opacity slider controls the dark strip behind
  it; 0 leaves only the dot and text over the picture.

## Running actions from a camera tile

Macro Deck gives a tile press either to the controls in its tree or to its Short Press flow, never both.
The movement arrows are controls, so they disable the tile's press flows. To run actions with the arrows
on:

1. Create a script in Macro Deck with the actions you want.
2. In the camera widget settings, set **Press script** to that script.
3. Press the picture. The script runs with the pressed widget and client, and the arrows still move the
   camera.

**None** keeps the press opening the enlarged camera window. A script that needs inputs without defaults
is not offered.

## Requirements

- Macro Deck 3.0 or newer.
- ffmpeg only for RTSP cameras. Install it and make sure `ffmpeg` is on the `PATH`, or set
  `IPCAM_FFMPEG_PATH` to the executable before starting Macro Deck. Without ffmpeg the integration
  reports an issue and RTSP streams stay disconnected.
- The camera must be reachable from the computer running Macro Deck. A camera on the same LAN is fine;
  it does not have to be reachable from the device showing the deck.

## Adding a camera

1. Open Macro Deck, then **Integrations > IP Camera > Configure**.
2. If ONVIF cameras answer on the network, pick one from the ONVIF field. Otherwise enter a name, a
   source type and the stream URL.
3. Repeat for every camera. Each one appears in the widget's camera picker immediately.

| Source type | What it expects | Example |
| --- | --- | --- |
| HTTP snapshot (JPEG) | A URL that returns one JPEG per request. The plugin polls it at the configured frame rate. | `http://192.168.1.20/snapshot.jpg` |
| HTTP MJPEG | A `multipart/x-mixed-replace` stream. The plugin reads it once and shares it between viewers. | `http://192.168.1.20/video.mjpg` |
| RTSP | An RTSP URL. ffmpeg turns it into JPEG frames, scaled to the configured maximum width. | `rtsp://192.168.1.30:554/Streaming/Channels/101` |

Optional settings are in **Advanced configuration**:

- **Username and password**: HTTP basic authentication for snapshot and MJPEG cameras. The password is
  stored in Macro Deck's encrypted secret store. RTSP credentials are written into the ffmpeg input URL,
  which means they are visible to processes on the same computer (the RTSP protocol has no separate
  credential option).
- **Frames per second**: 1 to 15, default 5. A tile does not need more, and a lower rate leaves the
  camera free for its own recording.
- **Maximum width**: frames are scaled down to this width before they reach Macro Deck, default 640.
  Set it to 0 to keep the camera's native size. Scaling RTSP happens in ffmpeg; scaling snapshots
  happens in the deck client.
- **RTSP transport**: TCP is the safe default. Use UDP only if the camera performs better with it.

### Common camera URLs

The exact path is model specific. These are the usual shapes:

| Camera | Snapshot | MJPEG | RTSP |
| --- | --- | --- | --- |
| Hikvision | `http://<ip>/ISAPI/Streaming/channels/101/picture` | | `rtsp://<ip>:554/Streaming/Channels/101` |
| Dahua | | | `rtsp://<ip>:554/cam/realmonitor?channel=1&subtype=0` |
| Reolink | `http://<ip>/cgi-bin/api.cgi?cmd=Snap&channel=0` | | `rtsp://<ip>:554/h264Preview_01_main` |
| TP-Link Tapo | | | `rtsp://<ip>:554/stream1` (needs a camera account) |
| Xiaomi Mi 360 1080p | | see below | see below |

## Camera wall

A camera wall is a **folder view**, not a widget. It replaces the folder's widget grid with one to four
cameras drawn edge to edge, so the pictures use the whole deck area without tile borders, gaps or
per-widget chrome. Macro Deck keeps its own folder navigation and back button.

Create one like this:

1. In the **Deck** view, open the folder you want, or create one with **New Folder** in the folder list.
2. Open the folder's view menu: use **Change folder view** in the folder header, or right-click the
   folder in the folder list and choose **Change view**.
3. Choose **Camera wall**. If the entry is missing, the IP Camera plugin is disabled.
4. Press **Configuration** and choose:
   - **Camera 1** to **Camera 4**: any slot you leave empty is skipped.
   - **Columns**: **One** or **Two**.
   - **Picture size**: **Fill** crops the picture to its cell, **Fit** shows the whole picture with
     black bars.
5. Save. Macro Deck reloads the folder with the wall.

How the chosen cameras are laid out:

| Cameras | Columns: One | Columns: Two |
| --- | --- | --- |
| 1 | fills the folder | fills the folder |
| 2 | stacked | side by side |
| 3 | stacked | two rows, the last one half width |
| 4 | stacked | 2 x 2 |

A single camera always fills the folder, which is the quickest way to give one camera a whole page. The
wall has no widgets of its own; pressing a cell opens that cell's camera in the modal. Per-cell arrows
are available when the wall controls are switched on.

Each cell can also show the same movement arrows as the camera widget. Enable **Movement arrows** in the
wall's Configuration and set **Arrow transparency**; every configured cell then draws left, right, up and
down buttons for its own camera. The arrows use the camera's ONVIF or Xiaomi control settings.

The folder's widgets are not deleted when you switch views. While the wall is active they are hidden,
and switching back to **Widget Grid** in the same menu brings them back. The wall uses the plugin's video
stream provider, so one producer per camera is still shared by every cell that shows that camera. An empty
wall shows "Choose cameras in the folder settings" until at least one camera is picked.

## Xiaomi Mi 360 1080p

Xiaomi does not document an RTSP or ONVIF endpoint for the Mi 360 1080p, and the stock firmware does
not answer on one. The model therefore needs one of two local routes:

1. **go2rtc (recommended).** go2rtc speaks Xiaomi's own camera protocol and can serve the picture as
   MJPEG without changing the camera. The first connection of each session needs Internet access to
   fetch the encryption keys; the video itself stays on the LAN. Add a stream to `go2rtc.yaml`:

   ```yaml
   streams:
     mi360: xiaomi://<account-id>:<region>@<camera-ip>?did=<device-id>&model=<model-code>
   ```

   The exact `xiaomi://` URL comes from go2rtc's Xiaomi documentation and the tokens from your Mi Home
   account. Then add a **HTTP MJPEG** camera in this plugin with:

   ```text
   http://<go2rtc-host>:1984/api/stream.mjpeg?src=mi360
   ```

   Use go2rtc's `/api/frame.jpeg?src=mi360` as an HTTP snapshot camera if you prefer polling.

2. **A community firmware that exposes RTSP.** Some legacy revisions, such as the MJSXJ02CM, can run
   community hacks. Treat this as unsupported and risky: it can brick the camera or remove Mi Home
   features, and the available hacks do not all include an RTSP server. If the camera does answer on
   RTSP, add an **RTSP** camera with the URL its firmware documents, commonly
   `rtsp://<camera-ip>/live/ch00_0`.

No cloud login or account token is used by this plugin. Camera control uses the camera's local miIO
channel and its device token, which is stored as a secret and never leaves the computer.

## How the frames flow

```text
camera --HTTP/RTSP--> plugin (one producer per camera) --multipart MJPEG--> 127.0.0.1:<random port>
                                                                                 |
                                                                        Macro Deck relay
                                                                                 |
                                                                     deck widget / browser / app
```

- One producer runs per camera while at least one client watches it. It stops 20 seconds after the
  last client leaves, so an idle deck does not keep ffmpeg or the camera busy.
- A slow client drops old frames instead of delaying the camera or other clients.
- When the source stalls, the last frame is repeated every 10 seconds so Macro Deck's relay keeps the
  session open instead of dropping it.
- The relay listens on `127.0.0.1` only. The camera URL never reaches a client, and no firewall rule is
  needed.
- Audio is not carried. Macro Deck's video streams play muted.

## Security

- The plugin fetches the camera URL from the computer running Macro Deck, so add only addresses you
  trust. A URL you configure can reach any service that computer can reach.
- Every client signed in to Macro Deck can open the streams, and the devices showing a deck receive the
  picture through Macro Deck. Do not put a camera on a deck that guests can open.
- HTTP camera passwords are stored by Macro Deck in its encrypted secret store and sent as an
  `Authorization` header.
- RTSP passwords are passed to ffmpeg in its input URL, because RTSP has no separate credential
  option. Other processes on the same computer can read that command line while a stream is open.

## Limitations

- MJPEG only. Every Macro Deck client can play it; the plugin does not produce HLS.
- The enlarged view is a Macro Deck modal. Its box is fixed by the client at roughly 34rem by 36rem on
  the desktop, and a plugin cannot make it true full screen. The modal carries movement arrows when the
  tile that opened it has them enabled; a Show camera action enables them by default.
- Panning inside a filled frame is not supported by Macro Deck's video component today. It crops inside
  its own element, so a transform can only move the cropped picture, not reveal the hidden part.
- ONVIF discovery follows the standard WS-Discovery and WS-Security flow and is covered by protocol
  tests. A real ONVIF camera has not been used yet to verify every vendor's dialect.
- HTTP digest authentication is not supported, only basic. Use a local restreamer such as go2rtc if
  the camera insists on digest.
- No talk-back, no recordings and no motion notifications. Camera controls are limited to the move, stop
  and night vision actions above.
- The picture is polled or streamed at the configured rate; it is not a 30 fps video. At 5 fps a deck
  tile looks live, and the camera stays available for its own app and recordings.

## Development

Requires the .NET 10 SDK and the Macro Deck plugin CLI (the version matches the SDK, 3.0.5 here):

```bash
dotnet tool install --global MacroDeck.Plugin.Cli --version 3.0.5
dotnet build -c Release -warnaserror
dotnet test -c Release
macrodeck-plugin test --project src/IpCamera
```

Run it against the installed Macro Deck app:

```bash
macrodeck-plugin run --project src/IpCamera
```

Approve the pairing prompt in Macro Deck once. The plugin then appears under Integrations with the
camera setup flow.

Package a release:

```bash
macrodeck-plugin build --source src/IpCamera --output ./artifacts
macrodeck-plugin validate --level publication --artifact ./artifacts/*.macroDeckPlugin
```

`macrodeck-plugin build` publishes the Windows, Linux and macOS builds and packs them. The output is
framework dependent and runs on the .NET 10 runtime Macro Deck ships.

### Project layout

```text
src/IpCamera/
  PluginIntegration.cs        lifecycle, capabilities, camera entries
  Composition.cs              DI wiring
  Cameras/                    camera model, config parsing, per-camera pipelines
  Streaming/                  JPEG framing, HTTP snapshot/MJPEG sources, ffmpeg, loopback relay
  VideoStreams/              the video stream provider
  Widgets/                    camera widget view, configuration, UI session adapter
  ConfigFlow/                 the camera setup flow
  Actions/                    the full-screen camera action
  Localization/Strings.resx   all user-facing text
store/                       Store screenshots, listing copy and their check
```

### Publishing

The manifest id is `com.itaimarom.ip-camera`, the publisher is `ItaiMarom`, and the repository is
`https://github.com/dominic25/ItaiMarom.IpCameraPlugin`. To publish to the Macro Deck Store, run the
release workflow by publishing a GitHub release. The Store builds and signs the package from that
workflow.

## Licence

Apache-2.0. See [LICENSE](LICENSE), [NOTICE](NOTICE) and [THIRD-PARTY-NOTICES](THIRD-PARTY-NOTICES).
ffmpeg is not bundled or redistributed; it is used from the host when it is installed.
