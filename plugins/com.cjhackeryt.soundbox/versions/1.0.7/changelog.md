## [1.0.7] - 2026-09-27

### Added
- Play Sound now counts down on its own widget while the sound plays, and returns
  the widget to its configured text and icon when playback ends. No variable,
  widget or extra configuration is needed.
- Each Play Sound action instance drives its own countdown from its own
  `OwnerWidgetId`, so several sound buttons stay independent and each one shows
  the duration of the sound configured on it.

### Changed
- Marked the `soundbox_playback_remaining` variable as deprecated in its
  description. It still works for configurations that already reference it, but
  the widget countdown no longer depends on it.
