.PHONY: all dev build clean deploy-xbox handshake setup

# ── Configuration ──
DEVICE_IP ?= 0.0.0.0
XBOX_IP ?= $(shell grep XBOX_IP .env 2>/dev/null | cut -d'=' -f2)

all: dev

dev:  ## Start local dev server
	@echo "⚡ Starting Sovereign Dev Engine..."
	cd src/launcher && npm run dev

handshake:  ## Start pairing daemon
	@echo "🔐 Starting Zero-Cloud Handshake..."
	python3 src/core/handshake.py

build:  ## Build full project
	@echo "🔨 Building..."
	cd src/launcher && npm run build
	@echo "✅ Build complete → dist/"

deploy-xbox: build  ## Push to Xbox Dev Mode
	@echo "🎮 Deploying to Xbox @ $(XBOX_IP):11443..."
	python3 src/xbox/sideload.py
	@echo "✅ Installed — check your Xbox!"

clean:
	rm -rf dist/ src/launcher/node_modules/ src/launcher/dist/

setup:  ## First-time setup
	pip install -r requirements.txt
	cd src/launcher && npm install
	@echo "✅ Ready — run 'make handshake' to begin"
