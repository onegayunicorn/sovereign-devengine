.PHONY: all dev build clean deploy-xbox handshake setup status claw

# ── Configuration ──
DEVICE_IP ?= 0.0.0.0
XBOX_IP ?= $(shell grep XBOX_IP .env 2>/dev/null | cut -d'=' -f2)

all: dev

dev:  ## Start local dev server (root vite)
	@echo "⚡ Starting Sovereign Dev Engine..."
	npm run dev

handshake:  ## Start pairing daemon + Paean bridge
	@echo "🔐 Starting Zero-Cloud Handshake + Paean bridge..."
	python3 src/core/handshake.py

claw:  ## Run Claw Agent status
	python3 src/core/claw_agent.py status

build:  ## Build full project
	@echo "🔨 Building..."
	npm run build
	@echo "✅ Build complete → dist/"

deploy-xbox: build  ## Push to Xbox Dev Mode
	@echo "🎮 Deploying to Xbox @ $(XBOX_IP):11443..."
	python3 src/xbox/sideload.py
	@echo "✅ Installed — check your Xbox!"

status:  ## Claw agent status check
	python3 src/core/claw_agent.py status

clean:
	rm -rf dist/ node_modules/

setup:  ## First-time setup
	pip install -r requirements.txt
	npm install
	@echo "✅ Ready — run 'make handshake' then 'make dev'"
