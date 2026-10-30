"""baked/plastic: one mid-light grey sphere for all solid plastics, split down the middle
(as the camera sees it, rotY=rotX=0): polished half on the left, matte spark-eroded half
on the right, with a fine parting line. UVs follow three.js SphereGeometry (x = -cos 2πu)."""
import os, numpy as np
from PIL import Image
W, H = 2048, 1024; O = 'baked/plastic'; os.makedirs(O, exist_ok=True)
u = (np.arange(W) + 0.5) / W
x = -np.cos(2 * np.pi * u)                  # left (-x) = gloss
matte = 0.5 * (1 + np.tanh(x / 0.004))      # crisp but antialiased edge
rng = np.random.default_rng(3)
n = rng.random((H // 2, W // 2)).astype(np.float32)
n = np.asarray(Image.fromarray((n * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)).astype(np.float32) / 255
rough = 0.06 * (1 - matte) + (0.52 + 0.06 * (n - 0.5)) * matte
groove = np.exp(-(x / 0.006) ** 2)
height = 0.5 + 0.25 * (n - 0.5) * matte - 0.35 * groove
col = np.full((H, W, 3), 1.0, np.float32)
save = lambda a, f, m: Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8), m).save(os.path.join(O, f), quality=95)
save(np.tile(rough, (1, 1)) if rough.ndim == 2 else rough, 'rough.jpg', 'L')
save(np.broadcast_to(height, (H, W)) if height.ndim == 1 else height, 'height.jpg', 'L')
save(col, 'color.jpg', 'RGB')
print('plastic baked')
