"""
🔗 Control Plane — Pair a device
Run this on your phone/laptop to link to the handshake daemon
"""
import requests

print("🔗 SOVEREIGN DEVICE PAIRING")
target_ip = input("Target device IP: ").strip() or "127.0.0.1"
pin_code = input("Enter 6-character PIN: ").strip().upper()
git_token = input("Your GitHub/Gitea token: ").strip()

try:
    res = requests.post(f"http://{target_ip}:5000/pair", json={
        "pin": pin_code,
        "token": git_token
    }, timeout=10)

    if res.status_code == 200:
        print("\n✅ LINK ESTABLISHED")
        print("Device is now sovereign-linked")
    else:
        print(f"\n❌ {res.json().get('msg', 'Unknown error')}")
except Exception as e:
    print(f"\n❌ Connection failed: {e}")
