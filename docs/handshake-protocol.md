# Zero-Cloud Handshake Protocol

## Overview
Devices pair using a short-lived 6-character alphanumeric PIN. No cloud accounts or external identity providers are required.

## Flow
1. **Target device** runs `src/core/handshake.py`
   - Generates a cryptographically random 6-char PIN (A-Z, 0-9)
   - Starts a local Flask server on port 5000
   - PIN expires after 300 seconds
2. **Control device** (phone/laptop) runs `src/core/control_plane.py`
   - User enters target IP + PIN + scoped Git token
   - POSTs to `http://<target>:5000/pair`
3. On success the target stores the token at `~/.sovereign/credentials` (mode 0600)

## Endpoints
| Method | Path | Description |
|--------|------|-------------|
| POST | `/pair` | Body: `{ "pin": "XXXXXX", "token": "..." }` |
| GET | `/status` | Returns `{ "paired": bool, "time_remaining": seconds }` |

## Security Notes
- PIN is single-use within the expiry window
- Token is never logged in full
- File permissions restrict access to the local user only
