# Zero-Cloud Handshake Protocol

## Overview
Devices pair using a short-lived 6-character alphanumeric PIN. No cloud accounts required.

## Flow
1. **Target device** runs `python3 src/core/handshake.py`
   - Generates cryptographically random 6-char PIN (A-Z, 0-9)
   - Starts Flask on port 5000
   - Registers Paean Bridge at `/paean/*`
   - PIN expires after 300 seconds
2. **Control device** runs `python3 src/core/control_plane.py`
   - User enters target IP + PIN + scoped Git token
   - POSTs to `http://<target>:5000/pair`
3. On success the target stores the token at `~/.sovereign/credentials` (mode 0600)

## Endpoints
| Method | Path | Description |
|--------|------|-------------|
| POST | `/pair` | Body: `{ "pin": "XXXXXX", "token": "..." }` |
| GET | `/status` | `{ "paired": bool, "time_remaining": seconds }` |
| POST | `/paean/deploy` | Triggers `make deploy-xbox` |
| POST | `/paean/sync` | Writes files from JSON body |
| GET | `/paean/status` | Bridge health |
| POST | `/deploy` | Alias → `/paean/deploy` |

## Security Notes
- PIN is single-use within the expiry window
- Token is never logged in full
- File permissions restrict access to the local user only
