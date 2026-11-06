The plugin now keeps the numbers fresh by itself.

- Claude Code renews its usage cache only when asked (for example by /usage). When the cache is 5 minutes old or more, the plugin runs `claude -p /usage --no-session-persistence`, which prints the usage and updates the cache. No prompt is sent to a model and no session is saved.
- A failed run, or one that does not update the cache, backs off (5, 10, up to 30 minutes) so Claude Code is never started in a loop.
- Claude Code is found on PATH, in ~/.local/bin, in %LOCALAPPDATA%\Programs\claude and in the newest Claude Code extension of VS Code, VS Code Insiders, Cursor or Windsurf. Set CLAUDE_USAGE_CLI to use a specific copy, or CLAUDE_USAGE_REFRESH=off to turn the refresh off.
- New permission: process:spawn (the plugin starts Claude Code). The README's privacy section describes it.

Still Windows (win-x64) only.
