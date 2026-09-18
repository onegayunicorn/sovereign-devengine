# ⚡ SOVEREIGN DEV ENGINE
**Sovereign Game Engine & Dev Portal — Zero-Cloud · Local-First · PHOTONIC-Ω Powered**

> Build, render, and deploy games entirely on your own terms.
> No external store, no gatekeeper, fully yours.

## ✨ What It Is
- 🔐 **Zero-Cloud Handshake** — Pair devices with 6-char PIN, no account needed
- 🤖 **Claw Agent** — Local CLI orchestrator (`status` / `build`)
- 🌐 **Paean Bridge** — AI workspace ↔ local deploy & sync (`/paean/*`)
- 🎮 **Xbox Dev Mode Sideload** — Push builds over local WiFi (`:11443`)
- 💫 **PHOTONIC-Ω Render Core** — Schumann 7.83 Hz · Golden Ratio φ · 5-channel tint
- 🏠 **Local-First CI/CD** — GitHub Actions + Gitea self-hosted runner
- 🎮 **Godot 3.5.x UWP path** — Documented templates + .appx fix

## 🚀 Quick Start
```bash
git clone https://github.com/onegayunicorn/sovereign-devengine.git
cd sovereign-devengine
cp .env.example .env          # fill XBOX_* values
make setup

# Terminal 1 — pairing + Paean bridge
make handshake

# Terminal 2 — launcher UI
make dev                      # → http://0.0.0.0:8080

# Optional
make status                   # Claw agent health
make deploy-xbox              # build + sideload
```

## 📋 Architecture

| Layer | Tech / Port |
|-------|-------------|
| Pairing | Flask ephemeral PIN → scoped PAT (`:5000`) |
| Paean Bridge | `/paean/deploy`, `/paean/sync` |
| Claw Agent | `python src/core/claw_agent.py status\|build` |
| Rendering | WebGL / GLSL — dual-pass + 5-channel tint |
| Launcher | React + Vite (`:8080`) |
| Console | Xbox Device Portal REST (`:11443`) |
| CI/CD | GitHub Actions + Gitea act_runner |

## 📚 Docs
- [Handshake Protocol](docs/handshake-protocol.md)
- [Xbox Dev Mode](docs/xbox-dev-mode.md)
- [Godot UWP Guide](docs/godot-uwp-guide.md)
- [Gitea Runner Setup](docs/gitea-runner-setup.md)
- [PHOTONIC-Ω Rendering](docs/photonic-rendering.md)

---

*"Not by plans or being comfortable — by finding the side that's not in control."*
