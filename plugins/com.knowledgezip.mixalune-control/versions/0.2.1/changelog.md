Version 0.2.1 updates the plugin logo and resolves Store review packaging requirements. Full README and MIT LICENSE are at the repository root; compiled packages are excluded from Git and dependencies restore from NuGet. GitHub release assets are from the trusted publishing workflow.

Includes channel volume/mute, microphone mute, reconnect, and Set/Up/Down noise-gate threshold controls. Gate controls require Mixalune capabilities effects.setThreshold and effects.adjustThreshold. Range -80 to -10 dB; default step 1 dB.

Installed trusted 0.2.1 package tested with updated Mixalune: authenticated connection, four channels, live gate state, successful threshold Up/Down; original threshold restored. 43 automated tests passed; Windows stub suite: 34 passed, 0 failed, 16 skipped.

Optional button icons: https://github.com/knowledgezip/Mixalune/releases/download/v0.2.0/mixalune-icons-1.0.0.zip
