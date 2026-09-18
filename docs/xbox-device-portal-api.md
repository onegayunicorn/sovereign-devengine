# Xbox Device Portal REST API — Dev Mode

Base URL (Dev Mode): `https://<XBOX_IP>:11443`  
Auth: HTTP Basic (username/password set in Remote Access Settings)  
TLS: self-signed — clients must use `verify=False` or trust the cert.

## Core endpoints used by Sovereign sideload

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/os/info` | Console OS / identity |
| GET | `/api/os/version` | Version probe (legacy) |
| GET | `/ext/xbox/info` | Device info |
| GET | `/api/app/packagemanager/packages` | List installed packages |
| POST | `/api/appx/packagemanager/package?package=<filename>` | Install .appx / .msix (multipart body) |
| DELETE | `/api/appx/packagemanager/package?package=<PackageFullName>` | Uninstall |
| POST | `/api/app/packagemanager/upload` | Upload loose folder to DevelopmentFiles |
| POST | `/api/app/packagemanager/register` | Register loose app folder |
| POST | `/ext/app/deployinfo` | Deploy metadata for packages |

## Install flow (what `src/xbox/sideload.py` does)

1. Ping `/api/os/info` (or fallbacks).
2. Open package file as multipart form field.
3. `POST /api/appx/packagemanager/package?package=<name>` with file body.
4. Accept 200/201/202 as success.

## Related tooling

- Browser UI: open `https://<IP>:11443` on the same LAN.
- Community managers (e.g. XB Homebrew Vault) use the same REST surface + WebSockets for live metrics.

## Security notes

- Only enable Device Portal on trusted networks.
- Prefer authentication required + strong password.
- Dev Mode apps are isolated from retail mode storage.
