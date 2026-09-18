# Sovereign Dev Engine Implementation Plan

## Scope

Implement the local-first pairing daemon, sandboxed Paean bridge, launcher UI, optional QPU stub, and Xbox Dev Mode sideload path described in the attached Sovereign Game & Dev Engine specification.

## Risk slices and acceptance criteria

1. **Pairing security:** generate a six-character A–Z/0–9 PIN, enforce expiry and single use, store the supplied scoped token with mode `0600`, and never log the token.
2. **Filesystem safety:** `/paean/sync` may write only beneath the repository root and must reject traversal and symlink escapes.
3. **Build reproducibility:** `npm run build` produces a Vite bundle; Python tests run without network or Xbox hardware.
4. **Deployment isolation:** Xbox sideloading is opt-in through `make deploy-xbox`; tests must not contact a console.
5. **Service health:** handshake and QPU endpoints return stable JSON contracts suitable for the launcher and local automation.

## Verification commands

```bash
python3 -m unittest discover -s tests -v
npm run build
make test
```
