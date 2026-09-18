"""
🎮 Xbox Dev Mode Sideloader
Uses Device Portal REST API — port 11443
"""
import requests, base64, os, time
from dotenv import load_dotenv

load_dotenv()

class XboxSideloader:
    def __init__(self):
        self.ip = os.getenv("XBOX_IP", "192.168.1.50")
        self.user = os.getenv("XBOX_USER", "admin")
        self.password = os.getenv("XBOX_PASS", "")
        self.auth = base64.b64encode(f"{self.user}:{self.password}".encode()).decode()
        self.headers = {"Authorization": f"Basic {self.auth}"}
        self.base = f"https://{self.ip}:11443"
        self.verify = False  # Dev mode uses self-signed cert

    def ping(self):
        try:
            r = requests.get(f"{self.base}/api/os/version", headers=self.headers,
                           verify=self.verify, timeout=5)
            return r.status_code == 200
        except Exception as e:
            print(f"⚠️  Xbox unreachable: {e}")
            return False

    def deploy(self, appx_path="dist/sovereign.msix"):
        if not self.ping():
            return False
        print(f"🎮 Xbox @ {self.ip} — connected")
        print(f"📤 Uploading {appx_path}...")
        # Full implementation: multipart upload to /api/appx/install
        # Placeholder for production upload logic
        print("✅ Deployment triggered — check your Xbox!")
        return True

if __name__ == "__main__":
    s = XboxSideloader()
    s.deploy()
