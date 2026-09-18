"""
🔐 Zero-Cloud Handshake — Sovereign Dev Engine
6-character ephemeral PIN → device pairing → scoped token storage
"""
from flask import Flask, request, jsonify
import secrets, string, time, os

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
