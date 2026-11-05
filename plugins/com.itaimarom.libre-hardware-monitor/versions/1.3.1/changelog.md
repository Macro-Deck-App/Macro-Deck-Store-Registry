## 🎉 Major Features

### Remote Machine Monitoring
- **Read sensors from remote LibreHardwareMonitor instances** — Add other PCs running LHM with Remote Web Server enabled
- **Each remote machine appears as its own branch** in the sensor tree, keeping local and remote sensors clearly separated
- **HTTP Basic Auth support** — Configure username/password for remote servers that require authentication
- **Test Connection button** — Verify connectivity and preview sensors before saving
  - Generates a stable key from the URL automatically for new entries
  - Shows live sensor values and controllable badges immediately
  - Displays connection status (success/error with details)

### Per-Sensor & Default Unit Selection
- **Choose display unit per sensor** — Override individual sensors (e.g., °C vs °F, GB vs GiB, MHz vs GHz)
- **Set default units per sensor kind** — Configure fallback units for Temperature, Data, Clock, Throughput, etc.
- **Live value updates** — Changing a unit selector instantly refreshes the value column in the configurator
- **Explicit "Default" option** — Selecting "Default" clears any explicit unit, letting the sensor follow kind defaults

### Variable Provider Improvements
- Remote sensors are read-only (no fan control across machines)
- Proper key-based namespacing so renaming a remote machine doesn't break variable bindings
- Duplicate URL detection prevents adding the same machine twice

## 🐛 Bug Fixes

### Configurator UI
- **Fixed `NS_ERROR_NET_RESET`** — Increased header limit from 16KB to 64KB to handle large query strings when many sensors have unit selectors
- **Removed flickering status text** — Eliminated the "fetching… /values?s=..." message that updated every second
- **Fixed live value refresh** — Values now update correctly when per-sensor unit is set to Default, and when a default is set to Default
- **Default unit selectors stay beside labels** — Fixed layout issue where dropdowns could separate from their labels

### Sensor Identity
- **Fixed duplicate sensor IDs** — Library sometimes reports the same sensor ID twice; now properly deduplicated
- **Stable remote keys** — Keys are derived from URL and preserved across renames

## 🔧 Technical Changes

- Updated Macro Deck SDK to 3.0.0
- Configurator web server now binds lazily (only when configurator is opened)
- Session-based security: 128-bit random keys, 30-minute expiry, loopback-only binding
- Backoff retry logic for failing remote connections (1s → 2s → 4s → 8s → 16s → 30s → 60s)

---

## Migration Notes

- **v1.2.x configurations are fully compatible** — No manual migration needed
- Remote machines and unit preferences are stored in the plugin configuration
- Existing sensor selections and polling intervals preserved
