"""
🔐 Zero-Cloud Handshake — Sovereign Dev Engine
6-character ephemeral PIN → device pairing → scoped token storage
+ Paean Bridge endpoints for AI ↔ local orchestration
"""
from flask import Flask, request, jsonify
import secrets, string, time, os
from pathlib import Path

# Wire Paean Bridge
try:
    from paean_bridge import paean_bridge
except ImportError:
    # Allow running from different cwd
    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from paean_bridge import paean_bridge

app = Flask(__name__)
app.register_blueprint(paean_bridge, url_prefix='/paean')

# Generate secure 6-char PIN
def generate_pin():
    chars = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(chars) for _ in range(6))

PIN = generate_pin()
PIN_EXPIRY = time.time() + 300  # 5 minutes
TOKEN_STORE = os.path.expanduser("~/.sovereign/credentials")

print(f"""
╔════════════════════════════════════════
║   🔐 SOVEREIGN PAIRING ACTIVE          ║
║                                        ║
║   YOUR CODE:  {PIN}                   ║
║   Expires: 5 minutes                   ║
║                                        ║
║   On your control device, enter this   ║
║   code to link.                        ║
║   Paean bridge: /paean/deploy | /sync  ║
╚════════════════════════════════════════
""")

@app.route('/pair', methods=['POST'])
def pair():
    if time.time() > PIN_EXPIRY:
        return jsonify({"status": "expired", "msg": "PIN timed out — restart"}), 400

    data = request.json or {}
    if data.get("pin", "").upper() != PIN:
        return jsonify({"status": "denied", "msg": "Incorrect code"}), 401

    token = data.get("token")
    if not token:
        return jsonify({"status": "error", "msg": "Missing token"}), 400

    # Save securely
    os.makedirs(os.path.dirname(TOKEN_STORE), exist_ok=True)
    with open(TOKEN_STORE, 'w') as f:
        f.write(token)
    os.chmod(TOKEN_STORE, 0o600)

    print("✅ Device paired — credentials stored")
    return jsonify({"status": "paired", "msg": "Sovereign link established"})

@app.route('/status', methods=['GET'])
def status():
    paired = os.path.exists(TOKEN_STORE)
    return jsonify({
        "paired": paired,
        "time_remaining": max(0, int(PIN_EXPIRY - time.time()))
    })

@app.route('/deploy', methods=['POST'])
def deploy_shortcut():
    """Convenience alias so launcher can hit /deploy"""
    from flask import redirect
    return redirect('/paean/deploy', code=307)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
