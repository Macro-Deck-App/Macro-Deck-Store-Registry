Fan and pump control, and Slider-ready fans.

- **Set fan speed** and **Restore fan control** actions: drive a controllable fan or pump at 0–100 %
  of its own range, clamped to what the chip reports, and hand it back to the motherboard's curve.
- **Writable fans for the Slider widget**: every sensor with a control is a writable variable, so
  Macro Deck's built-in Slider binds to it with no plugin-specific widget. The track comes from the
  chip, and the write happens when you let go.
- **The sensor window marks what can be driven**: `controllable` on a fan, `control below` on the
  branches that contain one, and `read-only` on a control sensor with nothing attached.
- **Widgets update at your polling rate**, not the host's five-second default.
- **Last review cleared**: the AI declaration matches generated assets only, the README is a user
  guide with the internals in DEVELOPMENT.md, and administrator rights and PawnIO are now described
  as optional.

PawnIO and administrator rights are needed only for processor temperature and clocks, fan speeds,
voltages, drive health and fan control. GPU, memory, storage and network sensors need neither.
