# Xbox Dev Mode Sideload Guide

## Prerequisites
1. Enable Developer Mode on your Xbox (Microsoft Partner Center account required for initial activation)
2. Note the Device Portal IP shown in Dev Home (bottom-right)
3. Default port: **11443** (HTTPS, self-signed certificate)

## Configuration
Copy `.env.example` → `.env` and set:
```
XBOX_IP=192.168.x.x
XBOX_USER=admin
XBOX_PASS=<password shown in Device Portal>
```

## Deploy
```bash
make deploy-xbox
```
This runs `src/xbox/sideload.py`, which:
- Pings `/api/os/version`
- Uploads the `.msix` / `.appx` package via the Device Portal REST API

## Notes
- Dev Mode only accepts UWP packages
- Your game engine must export to UWP / WinRT (Godot UWP export, Unity UWP target, etc.)
- For fully offline workflows, host the built package on a local asset server and point the Sovereign Launcher at it
