# Godot + Microsoft GDK — Xbox on PC Path

## Reality Check

| Path | Godot version | Target | Status |
|------|---------------|--------|--------|
| **UWP** | 3.5.x | Xbox Dev Mode (console) | Templates exist; .appx fix required |
| **GDK / Xbox on PC** | 4.x | Windows PC (Xbox app / PC Game Pass style) | Official Microsoft sample |
| **Console Series X\|S** | 4.x + NDA | Hardware console | Requires W4 Games (or similar) middleware + approved developer status |

Godot Foundation does **not** ship official console export templates (NDA / closed SDKs conflict with open development). For true Series X\|S you need a licensed middleware port.

## Official sample (2026)

- Repo: [microsoft/XBOX-Godot-Sample](https://github.com/microsoft/XBOX-Godot-Sample)
- Docs: [Get started with Godot for Xbox](https://learn.microsoft.com/en-us/gaming/gdk/docs/gdk-dev/pc-dev/tutorials/getting-started-with-godot/gc-get-started-godot)
- Covers: Microsoft GDK, Xbox services, PlayFab, GameInput as **GDExtension** addons for Godot 4
- Target: **Xbox on PC** (not retail console OS)
- Breaking rename in v0.3.0: `GDK*` types → `Xbox*` (e.g. `GDKUser` → `XboxUser`)

### Addons

| Addon | Role |
|-------|------|
| `godot_gdk` | Users, achievements, presence, social, stats, title storage, XStore, GameUI, … |
| `godot_playfab` | PlayFab sign-in, Game Saves, multiplayer, Party |
| `godot_gdk_editortools` | Packaging / sandbox helpers |

### High-level steps

1. Install [Microsoft Public GDK](https://github.com/microsoft/GDK) (April 2026 or later edition).
2. Clone and build the sample (CMake + vcpkg).
3. Mirror addons into your Godot 4 project.
4. Configure Partner Center Title ID / SCID / MicrosoftGame.config.
5. Export via **Project → Export → Xbox on PC**.

For **retail Xbox Series X\|S**, contact W4 Games (or another approved middleware vendor) after ID@Xbox / Partner Center approval.

## Sovereign pipeline recommendation

- **Dev Mode console sideload** → keep Godot **3.5.3 UWP** path (see `docs/godot-uwp-guide.md`).
- **Xbox on PC / Game Pass PC** → adopt XBOX-Godot-Sample + GDK for Godot 4.
- Do not expect a single Godot 4 export to both UWP Dev Mode and Series hardware without middleware.
