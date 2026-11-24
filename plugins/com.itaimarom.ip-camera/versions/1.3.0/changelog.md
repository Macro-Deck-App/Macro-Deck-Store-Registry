First public release.

- Camera widget with Fill or Fit, a label and Macro Deck's standard appearance settings.
- A short press opens the camera in Macro Deck's modal; your own Short Press flow wins.
- MJPEG video stream provider, so any widget that shows a video stream can use a camera.
- HTTP snapshot, HTTP MJPEG and RTSP through ffmpeg.
- ONVIF discovery and stream resolution with WS-Security.
- The setup fetches a live frame before saving, with a clear reason when it fails.
- Offline tiles say the camera is reconnecting, and the integration page offers Retry.
- Xiaomi Mi 360 support through go2rtc, with the required transcoded stream documented.
- Apache-2.0 license, README screenshots and Store listing copy.

Breaking change from the 1.x development builds: the package id is now `com.itaimarom.ip-camera` and the publisher is `ItaiMarom`. Install this build fresh and re-add the camera and the widget.

Requirements: Macro Deck 3, ffmpeg only for RTSP, and the camera reachable from the computer running Macro Deck.
