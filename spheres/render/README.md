# Realistic material spheres (v2)

Lit like Rob's oak reference (soft light from the left, warm off-white backdrop, sphere resting with a soft shadow to the right).

1. Download a CC0 texture set (ambientCG or Poly Haven, 2K JPG) into `src/<sphere-key>/` (Color, Roughness, Displacement/Height, Metalness if any).
2. `python3 bake.py src/<key> baked/<key> <tiles_per_sphere>` bakes it triplanar onto the sphere's UV map (no seams, no pinched poles). tiles_per_sphere sets the real-world scale (sphere ≈ 15 cm across: a 1 m texture → 0.15).
3. Serve this folder (`python3 -m http.server 8765 --bind 127.0.0.1`, with `npm i three@0.160.0` here) and run `node run2.js '[{"slug":"<key>","params":{...}}]'` (Playwright, swiftshader). Params: roughness, metalness, bumpScale, clearcoat, clearcoatRoughness, sheen, sheenColor, sheenRoughness, transmission, thickness, ior, attenuationColor, attenuationDistance, rotY, rotX, envIntensity.
4. `python3 compose.py out2/<key>.png ../<key>.jpg 640` puts it on the backdrop; the sample page loads `spheres/<key>.jpg`.

## Draft set, 30 Oct (textures without ambientCG access)
ambientcg.com / polyhaven were blocked, so the colour + normal maps of ambientCG scans (CC0) came from the GitHub mirror `PatrickJnr/cc0-texture-pack` (Source 2 `.vtex_c`), decoded with ValveResourceFormat's `Source2Viewer-CLI -i <file> -d -o <out.png>` (release asset cli-linux-x64.zip).
- `prep.py <color.png> <normal.png> src/<key> '<json>'`: colour tweaks, roughness map, height from the normal map (Fourier integration). Then `bake.py` as above.
- `jobs.sh`: the textures, scales and options used (oak wood058, softwood wood019, plywood wood017 via `plywood.py`, cork001, wool felt fabric043, PET felt fabric034, woven synthetic fabric039, woven natural fabric036, leather028, concrete006, aluminium metal011, stainless metal010).
- `plastic.py`: grey sphere, polished left half / matte right half (Rob: all solid plastics). `split.py <key> <roughness>`: same split for metals (aluminium, stainless; copper / gold / silver are aluminium-split with a colour). Render split spheres with rotY = rotX = 0.
- render2.html: `env: 'studio'` (glass), `'soft'` (polished metal), `backdrop` (glass refracts an in-scene backdrop); `glass_merge.py` puts the glass ball back on the standard backdrop.
- Which spheres use which image: Supabase table `match_sphere_images` (applied by `match_build_spheres()`).

## Hanging swatches (30 Oct, replaces the spheres; same file names in spheres/*.jpg)
Rob: squares hanging from one corner in a white space, no visible wire; rigid materials hang flat and show their thickness, soft ones drape.
- `swatch.html` + `runsw.js`: ~20 cm square hung from one corner. Rigid = box with thickness (mm), turned to show the edge (plywood shows ply lines). Soft = Verlet cloth hung from the corner; `stiff` (bending), `shape` (pull back to flat, for felts/leathers/foams), `sag`. Uses the flat maps in `src/<key>/` (prep.py; `gen_flat.py` for generated ones), tiled to real scale (`tiles` as for the spheres). `backdrop` + `glass_merge.py <out> outsw` for clear/translucent; `opacity` for film.
- `gen_flat.py`: tileable plain / beads / cells maps, and `split` (whole-swatch gloss/matte split along the diagonal = vertical on the hanging diamond) for plastics and metals.
- `swatch_all.py [key…]`: table of form per image (rigid + thickness, or soft + stiffness), renders outsw/ → comp/sw-<key>.jpg; copy to ../<key>.jpg.
