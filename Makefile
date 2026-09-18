.PHONY: all dev build test clean deploy-xbox handshake setup status claw

DEVICE_IP ?= 0.0.0.0
XBOX_IP ?= $(shell grep '^XBOX_IP=' .env 2>/dev/null | cut -d'=' -f2 || echo 192.168.1.50)

all: dev

dev:
	@echo "⚡ Starting Sovereign Dev Engine..."
	npm run dev

handshake:
	@echo "🔐 Starting Zero-Cloud Handshake + Paean bridge..."
	python3 src/core/handshake.py

claw:
	python3 src/core/claw_agent.py status

build:
	@echo "🔨 Building..."
	npm run build
	@echo "✅ Build complete → dist/"

test:
	@echo "🧪 Running offline Python tests..."
	python3 -m unittest discover -s tests -v
	@echo "🧪 Running frontend production build..."
	npm run build

deploy-xbox: build
	@echo "🎮 Deploying to Xbox @ $(XBOX_IP):11443..."
	python3 src/xbox/sideload.py
	@echo "✅ Installed — check your Xbox!"

status:
	python3 src/core/claw_agent.py status

clean:
	rm -rf dist/ .pytest_cache/ __pycache__/ src/**/__pycache__ tests/**/__pycache__

setup:
	python3 -m pip install -r requirements.txt
	npm install
	@echo "✅ Ready — run 'make handshake' then 'make dev'"
