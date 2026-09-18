# Services filesystem

Layout for local daemons and optional sidecar processes.

```
services/
├── handshake/     # symlink or docs pointing at src/core/handshake.py
├── paean-bridge/  # secured /paean/* gateway
├── claw/          # CLI agent entry
├── xbox-portal/   # sideload client notes
├── gitea-runner/  # docker-compose runner
└── qpu/           # optional quantum gateway stubs
```

Start core stack:

```bash
make handshake   # :5000
make dev         # :8080
```
