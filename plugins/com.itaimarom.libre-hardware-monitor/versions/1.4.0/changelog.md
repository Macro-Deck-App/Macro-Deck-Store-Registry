Fan control can be handed back on its own, automations can start from a sensor instead of polling one,
and a remote machine reports whether it is answering even when you watch none of its sensors.

## Hand fans back

- **Restore all fans** resets every controllable fan and pump at once - for the end of a session, or a
  "silence everything" button.
- **Restore fan control on exit** does the same when Macro Deck stops, and is on by default. A speed
  written by software outlives the plugin process, so this is what stops a fan staying where the last
  button left it.
- Speeds set before **Rescan hardware** are applied again to the rebuilt controls, so docking a laptop
  or plugging a drive back in does not silently drop what you set.

## Automations without polling

Five events in the automation editor, evaluated at the polling rate:

- **Sensor threshold crossed**, with **For at least** and **Clear by** (hysteresis), in the sensor's own
  unit.
- **Sensor stopped reporting**, after a grace period.
- **Remote machine offline** and **Remote machine online**, on the transition only.
- **Elevated readings changed**, when the helper starts or stops.

Each event carries what a flow needs - the sensor name and stable id, the machine, the reading, the
threshold and the unit - so a notification can say what happened instead of pointing at a variable.

## Remote machines say whether they are up

Every configured machine now publishes `<key>_online` and `<key>_status` (`Online`, `Reconnecting`,
`Offline`, `Connecting`), whether or not you ticked any of its sensors. An unticked machine is still
checked every 30 seconds, so a tile's state mapping and the issue list's **Retry now** button work
without watching a reading. One notification is raised when a machine goes down, not one per retry, and
recovery dismisses it; a machine that was already asleep when Macro Deck started shows the flag and the
issue but does not notify.

## Fixes

- A remote answer whose synthetic root node carried a hardware id no longer collapses the whole machine
  into one bogus device.
- **Sensor stopped reporting** measures its grace from the last sample rather than from when the cached
  reading expired, so it no longer waits an extra stale window before firing.
- **Retry now** on an unreachable machine reports the error instead of claiming success.
- Rescanning no longer holds up readings while the hardware library resets, and closing a remote no
  longer leaves a second polling loop behind.

## Upgrading

Nothing to do. Sensor selections, units and remote machines are kept. The new **Restore fan control on
exit** option starts ticked, so a fan still being driven when Macro Deck closes is now handed back
unless you untick it.
