# Gitea Actions Runner — Self-Hosted CI

## Enable Actions
In `gitea/app.ini`:
```ini
[actions]
ENABLED = true
```

Then: Site Admin → Actions → Runners → Create New Runner → copy the registration token.

## Docker Compose
See root `docker-compose.yml`. Update:
- `GITEA_INSTANCE_URL` → your Gitea host (e.g. `http://192.168.1.100:3000`)
- `GITEA_RUNNER_REGISTRATION_TOKEN` → the token from admin UI

```bash
docker compose up -d
```

## Workflow
Mirror of GitHub Actions lives at `.gitea/workflows/build.yml`.
Gitea Actions syntax is largely compatible with GitHub Actions.

## Labels
Runner is registered with labels `ubuntu-latest,self-hosted` so `runs-on: ubuntu-latest` works.
