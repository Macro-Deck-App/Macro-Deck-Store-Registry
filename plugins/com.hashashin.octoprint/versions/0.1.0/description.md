# OctoPrint for Macro Deck 3

A Macro Deck 3 plugin for controlling an OctoPrint printer through its REST API.
The plugin uses Macro Deck's language setting: English is the default, and
Spanish is available for action names, setup fields and messages.

## Actions

| Action | Effect | OctoPrint permission |
| --- | --- | --- |
| Get print status | Shows the job state, file and completion in the action result | STATUS |
| Connect printer / Disconnect printer | Uses OctoPrint's saved connection settings | CONNECTION |
| Start / Pause / Resume / Cancel print | Controls the selected or running print job | PRINT |
| Send G-code | Sends one command to the connected printer | CONTROL |

## Live variables

Use these in Macro Deck button text or widgets, for example
`{{ vars.octoprint_progress }}`. Macro Deck polls them every five seconds.

| Variable | Value |
| --- | --- |
| `octoprint_state` | State reported by OctoPrint |
| `octoprint_file` | Selected or printing file |
| `octoprint_progress` | Completion in % |
| `octoprint_print_time` | Elapsed print time in seconds |
| `octoprint_time_left` | Estimated remaining time in seconds |
| `octoprint_is_printing` | Whether the job is printing |
| `octoprint_nozzle_actual`, `octoprint_nozzle_target` | First nozzle temperature in °C |
| `octoprint_bed_actual`, `octoprint_bed_target` | Bed temperature in °C |

Macro Deck formats the numeric units, including percentages and durations.
Values without a reading appear as unavailable. Temperature values are unavailable
while the printer is disconnected. Requests to each OctoPrint endpoint are shared
briefly across variable reads to avoid repeated polling.
The shared plugin configuration is read once for concurrent variable requests
and refreshed every 30 seconds, so setup changes take effect automatically.

Open the OctoPrint plugin's setup page in Macro Deck and enter the OctoPrint
base URL (for example `http://octopi.local:5000`) and a user-specific API key.
Macro Deck checks the connection and stores the key as an encrypted secret.
For an HTTPS server with a self-signed certificate, select **Self-signed local
certificate** in the same setup form. This accepts an untrusted certificate
whose name differs from the URL, while still checking its validity dates and
rejecting other certificate errors. Use this option only for a local server you
control. Leave **Trusted certificate** selected when the certificate is issued
by a trusted authority.
All buttons then use this one configuration; only the Send G-code action needs
an action parameter. The key is sent in the `X-Api-Key` header. Use HTTPS when
accessing OctoPrint across an untrusted network. Do not put the key in the URL
or commit it to the repository.

Starting a print requires a file already selected in OctoPrint. Connecting uses
OctoPrint's existing port, baud rate and printer profile preferences. Cancelling
a print is immediate. G-code can affect an active print, so use commands suited
to your printer and job.

## Build

Requires the .NET 10 SDK and the Macro Deck 3 prerelease SDK packages:

```powershell
dotnet build
dotnet tool install --global MacroDeck.Plugin.Cli --prerelease
macrodeck-plugin run --project hashashin.OctoPrint.csproj --stub-host
macrodeck-plugin build --rid win-x64 --output artifacts
```

The packaged `.macroDeckPlugin` in `artifacts` can then be installed in Macro
Deck 3. A Macro Deck 3 host is needed for a live printer test.

API behavior follows the [OctoPrint REST API](https://docs.octoprint.org/en/main/api/)
and plugin structure follows the [Macro Deck 3 quickstart](https://docs.macro-deck.app/introduction/quickstart/).
