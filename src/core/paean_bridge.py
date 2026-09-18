"""
🌐 PAEAN BRIDGE — Connect AI workspace → local file system & execution
Handshake daemon exposes /paean/* for remote orchestration
"""
from flask import Blueprint, request, jsonify
import subprocess
from pathlib import Path

paean_bridge = Blueprint('paean', __name__)

@paean_bridge.route('/deploy', methods=['POST'])
def deploy():
    """Triggered from Paean / launcher → run local deploy-xbox chain"""
    try:
        result = subprocess.run(
            ["make", "deploy-xbox"],
            capture_output=True, text=True, timeout=300,
            cwd=Path(__file__).parent.parent.parent
        )
        return jsonify({
            "status": "ok" if result.returncode == 0 else "error",
            "msg": "deploy triggered — check your Xbox" if result.returncode == 0 else "deploy failed",
            "stdout": result.stdout[-2000:] if result.stdout else "",
            "stderr": result.stderr[-500:] if result.stderr else ""
        })
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

@paean_bridge.route('/sync', methods=['POST'])
def sync():
    """Pull latest from Paean workspace → overwrite local files"""
    data = request.json or {}
    files = data.get("files", {})
    written = []
    root = Path(__file__).parent.parent.parent
    for path, content in files.items():
        try:
            p = root / path
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(content, encoding='utf-8')
            written.append(path)
        except Exception as e:
            print(f"⚠️  Skip {path}: {e}")
    return jsonify({"status": "synced", "files_written": written})

@paean_bridge.route('/status', methods=['GET'])
def bridge_status():
    return jsonify({
        "bridge": "active",
        "daemon": "paean-bridge",
        "capabilities": ["deploy", "sync", "status"]
    })
