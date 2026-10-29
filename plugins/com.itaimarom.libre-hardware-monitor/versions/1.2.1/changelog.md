## Elevated readings

The driver-backed sensors – processor temperature and clocks, fan speeds, voltages, drive health – used
to need Macro Deck itself to run as an administrator. The plugin now asks Windows for that privilege
itself: from the issue list, and at every start if you tick **Start elevated readings at startup** in
the sensor window. Dismissing the prompt leaves the plugin in the limited mode it was already in, and a
helper that dies falls back to the readings this process can still reach.

## Smaller

19 dependencies instead of 48. The Linux/macOS/Android serial-port shim and the Mono.Posix runtime a
Windows-only plugin never loads are gone, along with framework packages Macro Deck already provides.
Nothing that ships changed.

## Upgrading

Nothing to do. PawnIO and administrator rights remain optional.
