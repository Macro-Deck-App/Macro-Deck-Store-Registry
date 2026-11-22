### Changed

- **Breaking**: the plugin now uses Vikunja's API v2 and needs Vikunja 2.7.1 or newer. Setup checks the version and
  explains when Vikunja is too old, and a tile connected to an older Vikunja says so. For an older Vikunja, update
  Vikunja or stay on 1.0.0. The saved address and token are kept: nothing has to be set up again.
- Checking a task now changes only its done state. A task edited elsewhere is no longer overwritten with older values.
- The token needs only Tasks: Read All and Update. Read One is no longer used; a 1.0.0 token keeps working.
- Built against Macro Deck SDK 3.0.5.

### Fixed

- A Vikunja that returns fewer than 50 tasks per page is now read to the end instead of stopping after the first page.
