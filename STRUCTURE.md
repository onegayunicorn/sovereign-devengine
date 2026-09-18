# Repository Structure

| Path | Responsibility |
|---|---|
| `src/core/handshake.py` | Flask pairing daemon, PIN lifecycle, credential storage, and bridge registration |
| `src/core/paean_bridge.py` | Root-pinned sync and build/deploy gateway |
| `src/core/control_plane.py` | Interactive client for pairing a target device |
| `src/core/claw_agent.py` | Local status/build CLI |
| `src/launcher/` | React/Vite operator dashboard |
| `src/rendering/` | PHOTONIC-Ω shader source |
| `src/xbox/sideload.py` | Xbox Device Portal client; only invoked explicitly |
| `services/qpu/` | Optional local simulator gateway; no remote quantum calls by default |
| `tests/` | Offline unit and integration tests |
| `.github/`, `.gitea/` | CI workflows for build validation |
| `docs/` | Protocol, Xbox, engine, runner, and QPU documentation |

The Python services are deliberately framework-light and can run on a local target device. The launcher is a visual control surface only; it does not contain deployment credentials.
