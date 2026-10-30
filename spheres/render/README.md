# Realistic material spheres (v2)

Lit like Rob's oak reference (soft light from the left, warm off-white backdrop, sphere resting with a soft shadow to the right).

1. Download a CC0 texture set (ambientCG or Poly Haven, 2K JPG) into `src/<sphere-key>/` (Color, Roughness, Displacement/Height, Metalness if any).
2. `python3 bake.py src/<key> baked/<key> <tiles_per_sphere>` bakes it triplanar onto the sphere's UV map (no seams, no pinched poles). tiles_per_sphere sets the real-world scale (sphere ≈ 15 cm across: a 1 m texture → 0.15).
3. Serve this folder (`python3 -m http.server 8765 --bind 127.0.0.1`, with `npm i three@0.160.0` here) and run `node run2.js '[{"slug":"<key>","params":{...}}]'` (Playwright, swiftshader). Params: roughness, metalness, bumpScale, clearcoat, clearcoatRoughness, sheen, sheenColor, sheenRoughness, transmission, thickness, ior, attenuationColor, attenuationDistance, rotY, rotX, envIntensity.
4. `python3 compose.py out2/<key>.png ../<key>.jpg 640` puts it on the backdrop; the sample page loads `spheres/<key>.jpg`.
