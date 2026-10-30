# Composite a transparent sphere render onto the warm off-white studio backdrop, square crop.
import sys
import numpy as np
from PIL import Image
src, out = sys.argv[1], sys.argv[2]
size = int(sys.argv[3]) if len(sys.argv) > 3 else 640
im = Image.open(src).convert('RGBA'); W, H = im.size
y, x = np.mgrid[0:H, 0:W] / np.array([H, W])[:, None, None]
top, bot = np.array([246, 245, 242]), np.array([233, 231, 227])
bg = top * (1 - y[..., None]) + bot * y[..., None]
vig = 1 - 0.05 * (((x - 0.5) ** 2 + (y - 0.45) ** 2) * 2.2)
bg = (bg * vig[..., None]).clip(0, 255).astype(np.uint8)
back = Image.fromarray(bg, 'RGB').convert('RGBA')
back.alpha_composite(im)
back.convert('RGB').resize((size, size), Image.LANCZOS).save(out, quality=88)
