# ⚡ SOVEREIGN DEV ENGINE
**Sovereign Game Engine & Dev Portal — Zero-Cloud · Local-First · PHOTONIC-Ω Powered**

> Build, render, and deploy games entirely on your own terms.
> No external store, no gatekeeper, fully yours.

## ✨ What It Is
- 🔐 **Zero-Cloud Handshake** — Pair devices with 6-char PIN, no account needed
- 🎮 **Xbox Dev Mode Sideload** — Push builds directly to your console over local WiFi (`:11443`)
- 💫 **PHOTONIC-Ω Render Core** — RYYB clarity · Sobel edge protection · Schumann 7.83 Hz pulse · Golden Ratio φ modulation
- 🏠 **Local-First CI/CD** — Gitea/Forgejo runner → build → deploy → run — all yours
- 📱 **Samsung A17 / Termux Ready** — Develop, test, deploy from your phone

## 🚀 Quick Start
```bash
# Pair your device
python3 src/core/handshake.py

# Build & run
make dev

# Deploy to Xbox
make deploy-xbox
```

## 📋 Architecture

| Layer | Tech |
|-------|------|
| Pairing | Flask ephemeral PIN → scoped PAT |
| Rendering | WebGL/Three.js — dual-pass FBO bloom + 5-channel tint |
| Console | Xbox Device Portal REST API — port 11443 |
| CI/CD | GitHub Actions / Gitea → UWP .msix builder |
| Sensors | RYYB edge-aware reconstruction — 69.5% fidelity gain |

## 🤝 Built With
- PHOTONIC-Ω — Light & resonance pipeline
- Samsung A17 / Termux — Mobile dev workspace
- Xbox Dev Mode — Living room console target
- You — The architect 🔥

---

*"Not by plans or being comfortable — by finding the side that's not in control."*
