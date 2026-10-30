"""Half polished / half matte version of a baked sphere, split down the middle as the camera
sees it (render with rotY=rotX=0): polished on the left, the baked (matte/brushed) surface on
the right, with a fine parting line. Same layout as plastic.py.
usage: python3 split.py <key> <polished_roughness>   -> baked/<key>-split
"""
import sys, os, numpy as np
from PIL import Image
key, pr = sys.argv[1], float(sys.argv[2]); S, O = f'baked/{key}', f'baked/{key}-split'
os.makedirs(O, exist_ok=True)
ld = lambda f, m: np.asarray(Image.open(os.path.join(S, f)).convert(m)).astype(np.float32) / 255
col, rough, h = ld('color.jpg', 'RGB'), ld('rough.jpg', 'L'), ld('height.jpg', 'L')
H, W = rough.shape
x = -np.cos(2 * np.pi * (np.arange(W) + 0.5) / W)[None, :]   # three.js SphereGeometry UVs; left = -x
m = 0.5 * (1 + np.tanh(x / 0.004))                           # 0 polished, 1 matte
groove = np.exp(-(x / 0.006) ** 2)
col = col * m[..., None] + col.reshape(-1, 3).mean(0) * (1 - m[..., None])
rough = rough * m + pr * (1 - m)
h = (h * m + h.mean() * (1 - m)) - 0.35 * groove
sv = lambda a, f, mode: Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8), mode).save(os.path.join(O, f), quality=95)
sv(col, 'color.jpg', 'RGB'); sv(rough, 'rough.jpg', 'L'); sv(h, 'height.jpg', 'L')
print(O)
