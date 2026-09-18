# Hello Sovereign

Minimal example that exercises the handshake → build → deploy path.

```bash
# From repo root
make handshake          # start PIN daemon
# In another terminal:
python3 src/core/control_plane.py
make dev                # launch UI at :8080
```
