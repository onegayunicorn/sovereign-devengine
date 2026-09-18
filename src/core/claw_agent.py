"""
🤖 CLAW AGENT — Local Execution Orchestrator
Direct, fast, offline-capable task runner
"""
import subprocess, json, os, sys
from pathlib import Path

class ClawAgent:
    def __init__(self, root=None):
        self.root = Path(root or Path(__file__).parent.parent.parent)
        self.state = {"tasks": [], "active": None}

    def run(self, cmd, cwd=None):
        """Execute shell command, stream output"""
        print(f"⚡ CLAW → {cmd}")
        proc = subprocess.Popen(
            cmd, shell=True, cwd=cwd or self.root,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
        )
        output = []
        for line in iter(proc.stdout.readline, ''):
            sys.stdout.write(line)
            output.append(line)
        returncode = proc.wait()
        return {
            "ok": returncode == 0,
            "code": returncode,
            "output": ''.join(output)
        }

    def status(self):
        """Check all services"""
        return {
            "handshake_daemon": self._ping(5000),
            "dev_server": self._ping(8080),
            "git_repo": (self.root / ".git").exists()
        }

    def _ping(self, port):
        import socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.1)
        alive = s.connect_ex(('127.0.0.1', port)) == 0
        s.close()
        return alive

    def build(self):
        """Full build sequence"""
        yield "📦 Installing deps..."
        yield self.run("pip install -r requirements.txt")
        yield self.run("npm ci || npm install")
        yield "🔨 Building launcher..."
        yield self.run("npm run build")
        yield "✅ Build complete → dist/"

if __name__ == "__main__":
    agent = ClawAgent()
    if len(sys.argv) > 1 and sys.argv[1] == "status":
        print(json.dumps(agent.status(), indent=2))
    elif len(sys.argv) > 1 and sys.argv[1] == "build":
        for step in agent.build():
            if isinstance(step, str):
                print(step)
            elif isinstance(step, dict) and not step["ok"]:
                print(f"❌ Failed: {step['code']}")
                sys.exit(1)
    else:
        print("Usage: python src/core/claw_agent.py [status|build]")
