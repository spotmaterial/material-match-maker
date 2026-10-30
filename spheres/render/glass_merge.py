# Clear glass: sphere pixels from the render with the in-scene backdrop (so it refracts the
# surface), shadow and transparency from a mask render, so the backdrop matches every sphere.
import numpy as np
from PIL import Image
g = np.asarray(Image.open('out2/clear-glass.png').convert('RGBA')).astype(np.float32)
m = np.asarray(Image.open('out2/clear-glass-mask.png').convert('RGBA')).astype(np.float32)
a = m[..., 3] / 255
sph = np.clip((a - 0.9) / 0.08, 0, 1)[..., None]
out = m.copy(); out[..., :3] = g[..., :3] * sph + m[..., :3] * (1 - sph); out[..., 3] = np.maximum(m[..., 3] * (1 - sph[..., 0]), 255 * sph[..., 0])
Image.fromarray(out.astype(np.uint8), 'RGBA').save('out2/clear-glass-final.png')
