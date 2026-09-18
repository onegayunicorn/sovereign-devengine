"""
Optional QPU gateway stub — local simulator only.
Does not contact external QPUs unless BACKEND=remote and credentials exist.
"""
from flask import Flask, request, jsonify
import time
import uuid

app = Flask(__name__)
JOBS = {}

@app.route("/qpu/backends", methods=["GET"])
def backends():
    return jsonify({
        "backends": [
            {"id": "sim-local", "type": "simulator", "online": True},
            {"id": "remote", "type": "qpu", "online": False, "note": "configure credentials"}
        ]
    })

@app.route("/qpu/submit", methods=["POST"])
def submit():
    body = request.get_json(silent=True) or {}
    job_id = str(uuid.uuid4())[:8]
    JOBS[job_id] = {
        "id": job_id,
        "status": "completed",
        "backend": body.get("backend", "sim-local"),
        "shots": body.get("shots", 1024),
        "result": {"counts": {"0": 512, "1": 512}, "note": "stub simulator"},
        "ts": time.time()
    }
    return jsonify({"job_id": job_id, "status": "queued"})

@app.route("/qpu/job/<job_id>", methods=["GET"])
def job(job_id):
    j = JOBS.get(job_id)
    if not j:
        return jsonify({"error": "not found"}), 404
    return jsonify(j)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5055)
