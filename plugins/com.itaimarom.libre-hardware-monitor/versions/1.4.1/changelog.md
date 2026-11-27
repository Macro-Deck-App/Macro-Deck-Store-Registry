**Enable elevated readings** - and **Start elevated readings at startup** - now work on a PC without a
system-wide .NET 10 install.

The helper is the plugin relaunched as an administrator. It was started through the apphost beside the
plugin, and that apphost finds a runtime only where .NET is installed for the machine - not the private
runtime Macro Deck ships and starts plugins on. On a PC with no global .NET 10 the apphost stopped at its
"You must install .NET" dialog; because the helper is started windowless, the dialog was hidden, and the
plugin waited for a helper that never connected and reported a timeout. Pointing it at Macro Deck's
runtime was not an option either: Windows does not pass the caller's environment across a UAC elevation,
so `DOTNET_ROOT` never reached the helper.

The helper now starts through the same `dotnet` host that is already running the plugin, which resolves
the runtime the plugin itself came in on. The apphost is still used by a self-contained build.

- **The UAC prompt names ".NET Host"** rather than the plugin, and is signed by Microsoft Corporation.
- Everything else is unchanged: the same binary, the same pipe, the same checks on who may serve.

## Upgrading

Nothing to do. Variables, fan controls, sensor selections and remote machines are unchanged. If Macro
Deck runs as an administrator, there is no helper to start and this release changes nothing for you.
