# QPU Integration Notes — Sovereign Pipeline

This document maps **quantum processing unit (QPU)** stacks into the Sovereign Dev Engine as optional, offline-friendly research/accelerator paths. No cloud account is required for local simulation; real QPUs remain vendor-mediated.

## Practical stacks (2025–2026)

| Stack | Language | QPU / backend model | Notes |
|-------|----------|---------------------|-------|
| **CUDA-Q** (NVIDIA) | Python / C++ | Hybrid CPU+GPU+QPU; 75%+ public QPUs | Kernel model; MLIR/LLVM/QIR; strong for hybrid ML |
| **Qiskit** | Python | IBM + many simulators | Broad ecosystem; REST/cloud jobs |
| **qBraid SDK** | Python | Multi-provider (IonQ, QuEra, IQM, …) | Framework conversion layer |
| **Q-AIM** | Python / FastAPI | Vendor-agnostic microservices | Dockerized gateway; good fit for local bridge |
| **Photonic / NVQLink** | CUDA-Q + vendor | Low-latency GPU↔QPU (~30 ms class demos) | Research path for real-time hybrid |

## Sovereign-friendly pattern

Treat a QPU (or simulator) like any other **local service**:

1. Run a thin Flask/FastAPI gateway (or extend Paean Bridge) that accepts circuit payloads.
2. Execute on:
   - local simulator (Qiskit Aer, CUDA-Q sim, PennyLane),
   - or a configured remote QPU endpoint (token in `~/.sovereign/credentials`, never in git).
3. Return results JSON to the launcher or Claw agent.

### Suggested endpoints (future)

```
POST /qpu/submit   { "circuit": "...", "shots": 1024, "backend": "sim|remote" }
GET  /qpu/job/<id>
GET  /qpu/backends
```

Sandbox the same way as `/paean/sync`: only allow writes under repo `artifacts/qpu/`.

## Relation to PHOTONIC-Ω

The engine’s photonic/resonance naming is **artistic and signal-processing oriented** (Schumann, φ tint, edge-aware shaders). It is **not** a claim of physical QPU hardware. Real quantum integration stays behind an explicit `/qpu` gateway so creative rendering and scientific backends remain decoupled.

## Dependencies (optional)

```
# requirements-qpu.txt (optional extra)
qiskit>=1.0
cuda-quantum  # when NVIDIA stack available
# or: qbraid
```

Install only if you actively develop quantum workflows; keep core `requirements.txt` lean.
