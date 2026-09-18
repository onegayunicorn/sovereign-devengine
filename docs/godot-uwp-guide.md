# 🎮 Godot UWP → Xbox Dev Mode — Complete Guide

## Version Selection
- ✅ **Godot 3.5.3** — Last stable with native UWP export
- ❌ Godot 4.x — UWP removed; use **GDK / Xbox on PC** path instead (see `godot-gdk-guide.md`)

## Install Export Templates
1. Download: `Godot_v3.5.3-stable_export_templates.tpz`
2. Rename to `.zip`, extract → `bin/` folder
3. Place at:
   - Linux: `~/.local/share/godot/templates/3.5.3.stable/bin/`
   - Windows: `%APPDATA%\Godot\templates\3.5.3.stable\bin\`
   - macOS: `~/Library/Application Support/Godot/templates/3.5.3.stable/bin/`

## Export Settings
- Platform → **UWP**
- Architecture → **x64** only (Xbox rejects ARM/x86)
- Publisher name → **exact match** with Xbox Dev Mode account
- Capabilities → check: `InternetClientServer`, `PrivateNetworkClientServer`
- ✅ **Enable Dev Mode** checkbox

## The .appx Fix (Critical!)
1. Rename `.appx` → `.zip`
2. **Delete** `[Content_Types].xml`
3. Rezip → rename back to `.appx`
4. Upload to `https://<xbox-ip>:11443` → Install

## Memory Limit Trap
- Manifest type = **Game** → ~5 GB RAM available
- Manifest type = **App** → ~1 GB → silent crash
- In Godot export → set **Game** as target type

## See also
- `docs/godot-gdk-guide.md` — Godot 4 + Microsoft GDK (Xbox on PC)
- `docs/xbox-device-portal-api.md` — REST endpoints used by sideload
