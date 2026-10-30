# Clear/translucent spheres: ball pixels from the render with the in-scene backdrop (so it
# refracts the surface), shadow and transparency from a <key>-mask render, so the backdrop
# matches every other sphere. usage: python3 glass_merge.py [key=clear-glass]
import sys
import numpy as np
from PIL import Image
k = sys.argv[1] if len(sys.argv) > 1 else 'clear-glass'
g = np.asarray(Image.open(f'out2/{k}.png').convert('RGBA')).astype(np.float32)
m = np.asarray(Image.open(f'out2/{k}-mask.png').convert('RGBA')).astype(np.float32)
a = m[..., 3] / 255
sph = np.clip((a - 0.9) / 0.08, 0, 1)[..., None]
out = m.copy(); out[..., :3] = g[..., :3] * sph + m[..., :3] * (1 - sph); out[..., 3] = np.maximum(m[..., 3] * (1 - sph[..., 0]), 255 * sph[..., 0])
Image.fromarray(out.astype(np.uint8), 'RGBA').save(f'out2/{k}-final.png')
