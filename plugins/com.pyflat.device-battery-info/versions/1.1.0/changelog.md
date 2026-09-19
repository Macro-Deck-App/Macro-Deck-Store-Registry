### Fixes
* **Bluetooth device picker:** Paired Bluetooth devices now show up in the list when adding a device. Previously a device only appeared if Windows already had a cached battery reading for it, so many working headsets and earbuds were missing.
* **Bluetooth battery reading:** Battery levels are now looked up by the device's Bluetooth address instead of by name. Typing a device name by hand now works with the name Windows Settings shows.
* **Unsupported devices hidden:** Devices that can never report a battery level through Windows (for example speakers without a hands-free profile) are no longer offered.

### Improvements
* The Bluetooth device list is now a real dropdown that shows each device's current battery level, or "no reading yet" if Windows has none.
* You can enter a device name manually below the list for a device that isn't connected right now. A name entered there takes priority over the dropdown.

**Full Changelog**: https://github.com/PyFlat/Device-Battery-Info/compare/v1.0.2...v1.1.0
