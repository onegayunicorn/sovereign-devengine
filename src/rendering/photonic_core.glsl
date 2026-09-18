// =====================================================
// PHOTONIC-Ω — Sovereign Render Core
// Schumann 7.83 Hz · Golden Ratio φ · 5-Channel Tint
// =====================================================
precision highp float;
varying vec2 vUv;

uniform sampler2D tScene;
uniform vec2 uResolution;
uniform float uTime;

#define SCHUMANN 7.83
#define PHI      1.61803399

float lum(vec3 c) { return dot(c, vec3(0.299, 0.587, 0.114)); }

vec3 photonicTint(vec3 rgb, float L, float t) {
  const vec3 cBase    = vec3(0.20, 0.40, 0.60);
  const vec3 cViolet  = vec3(0.70, 0.20, 0.90);
  const vec3 cLife    = vec3(0.20, 0.90, 0.40);
  const vec3 cGold    = vec3(1.00, 0.85, 0.20);
  const vec3 cField   = vec3(0.50, 0.90, 0.70);

  float wBase   = 0.5 + 0.5*sin(t * SCHUMANN);
  float wViolet = 0.5 + 0.5*sin(t * SCHUMANN * PHI);
  float wLife   = 0.5 + 0.5*sin(t * SCHUMANN * 2.0);
  float wGold   = 0.5 + 0.5*sin(t * SCHUMANN * PHI*PHI);
  float wField  = 0.5 + 0.5*sin(t * SCHUMANN / PHI);

  vec3 tint = cBase * wBase;
  tint = mix(tint, cViolet, smoothstep(0.3, 0.5, L) * wViolet);
  tint = mix(tint, cLife,   smoothstep(0.5, 0.7, L) * wLife);
  tint = mix(tint, cGold,   smoothstep(0.7, 0.85, L) * wGold);
  tint = mix(tint, cField,  smoothstep(0.85, 1.0, L) * wField);

  return rgb * tint * 1.2;
}

void main() {
  vec3 scene = texture2D(tScene, vUv).rgb;
  float L = lum(scene);

  float glow = smoothstep(0.75, 0.92, L);
  vec3 final = mix(scene, photonicTint(scene, L, uTime), glow);

  gl_FragColor = vec4(final, 1.0);
}
