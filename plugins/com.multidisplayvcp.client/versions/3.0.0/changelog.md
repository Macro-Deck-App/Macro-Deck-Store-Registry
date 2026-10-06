# MultiDisplayVCP Client v3.0.0 for Macro Deck 3

This major release completely rebuilds and upgrades the MultiDisplayVCP plugin for **Macro Deck 3**, delivering multi-platform support, modern gRPC communication, and enhanced performance.

---

### 🌟 What's New in v3.0.0

- **Macro Deck 3 Ready**: Full migration to the modern Macro Deck 3 plugin SDK and architecture (.NET 10).
- **Unified Multi-Platform Package**: Native runtime support across all platforms:
  - **Windows** (`win-x64`)
  - **Linux** (`linux-x64`)
  - **macOS Apple Silicon** (`osx-arm64`)
  - **macOS Intel** (`osx-x64`)
- **Dual-Mode High Performance Networking**:
  - **MagicOnion / gRPC (Primary)**: High-throughput, zero-allocation protocol paired with MultiDisplayVCP Server v2.0+.
  - **TCP Fallback**: Retains backwards compatibility with standard TCP socket connections.
- **Enhanced Security**: HMAC-SHA256 authenticated handshake with replay-attack protection.
- **Streamlined Assets**: Modernized plugin manifest and iconography matching the Macro Deck 3 ecosystem.

---

### 🖥️ Requirements

- **Macro Deck**: Macro Deck 3.0.0 or higher.
- **Companion Server**: Requires [MultiDisplayVCP Server v2.0.0+](https://github.com/doggdogpack/MultiDisplayVCPServer) running on the host/network.
