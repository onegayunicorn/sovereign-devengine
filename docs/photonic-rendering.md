# PHOTONIC-Ω Rendering Core

## Constants
| Parameter | Value |
|-----------|-------|
| Schumann Resonance | 7.83 Hz |
| Golden Ratio φ | 1.61803399 |
| Luminance bloom low | 0.75 |
| Luminance bloom high | 0.92 |

## 5-Channel Tint
| Channel | Frequency | Color |
|---------|-----------|-------|
| Base | 7.83 Hz | `#336699` |
| Violet | 7.83 × φ | `#b333e6` |
| Life | 7.83 × 2 | `#33e666` |
| Gold | 7.83 × φ² | `#ffd933` |
| Field | 7.83 ÷ φ | `#80e6b3` |

## Pipeline
1. **Capture** — scene to HalfFloat FBO
2. **Gate** — luminance extraction + smoothstep threshold
3. **Spread** — separable Gaussian blur
4. **Composite** — 5-channel weighted mix driven by Schumann/φ oscillators

Shader source: `src/rendering/photonic_core.glsl`
