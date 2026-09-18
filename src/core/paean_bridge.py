"""
🌐 PAEAN BRIDGE — AI ↔ Local Execution Gateway
Secure · Sandboxed · Root-Pinned
"""
from flask import Blueprint, request, jsonify
from pathlib import Path
import subprocess

# ── Sandbox everything inside repo root ──
ROOT = Path(__file__).resolve().parent.parent.parent
BRIDGE_VERSION = "1.0.1-secured"

paean_bridge = Blueprint('paean', __name__)


@paean_bridge.route('/status', methods=['GET'])
def bridge_status():
    return jsonify({
        "bridge": "active",
        "version": BRIDGE_VERSION,
        "root": str(ROOT),
        "capabilities": ["deploy", "sync", "status"],
        "sandbox": "enabled — root only"
    })


@paean_bridge.route('/sync', methods=['POST'])
def sync():
    """Paean workspace → local file sync — SANDBOXED to repo root"""
    files = (request.get_json(silent=True) or {}).get("files", {})
    if not isinstance(files, dict):
        return jsonify({"status": "error", "msg": "files must be an object"}), 400
    written = []
    skipped = []

    for rel_path, content in files.items():
        # Resolve and ENFORCE sandbox — never escape repo root
        target = (ROOT / rel_path).resolve()

        # Strict: target must be under ROOT
        try:
            target.relative_to(ROOT)
        except ValueError:
            skipped.append(f"{rel_path} — PATH ESCAPE BLOCKED")
            continue

        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content if isinstance(content, str) else str(content), encoding='utf-8')
            written.append(rel_path)
        except Exception as e:
            skipped.append(f"{rel_path} — {str(e)}")

    return jsonify({
        "status": "synced",
        "files_written": written,
        "skipped": skipped,
        "root": str(ROOT)
    })


@paean_bridge.route('/deploy', methods=['POST'])
def deploy():
    """Trigger build → deploy — PINNED to repo root directory"""
    try:
        result = subprocess.run(
            ["make", "deploy-xbox"],
            cwd=str(ROOT),  # always run from repo root
            capture_output=True,
            text=True,
            timeout=300
        )
        return jsonify({
            "status": "ok" if result.returncode == 0 else "error",
            "code": result.returncode,
            "msg": "deploy triggered — check your Xbox" if result.returncode == 0 else "deploy failed",
            "stdout": (result.stdout or "")[-2000:],
            "stderr": (result.stderr or "")[-500:]
        })
    except subprocess.TimeoutExpired:
        return jsonify({"status": "timeout", "msg": "Deploy timed out — check Xbox connection"}), 504
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500
