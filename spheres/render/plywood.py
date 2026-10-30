"""Build baked/plywood from baked/plywood-face and baked/plywood-cross: a ball turned from a
stack of plies shows them as rings (horizontal bands at equal heights), alternating grain
direction, with a thin darker glue line between plies.
usage: python3 plywood.py [plies_across_diameter=40]
"""
import sys, os
import numpy as np
from PIL import Image

n_plies = float(sys.argv[1]) if len(sys.argv) > 1 else 40
A, B, O = 'baked/plywood-face', 'baked/plywood-cross', 'baked/plywood'
os.makedirs(O, exist_ok=True)
ld = lambda d, f, g: np.asarray(Image.open(os.path.join(d, f)).convert('L' if g else 'RGB')).astype(np.float32) / 255
H = ld(A, 'color.jpg', False).shape[0]
v = (np.arange(H) + 0.5) / H
y = np.cos(v * np.pi)                      # sphere height of each row (-1..1)
t = (y + 1) / 2 * n_plies                  # ply coordinate
idx = np.floor(t).astype(int); frac = t - idx
# slope of the cut surface: plies look wider near the top/bottom, so glue width follows |dy/dv|
glue_w = 0.05
glue = np.exp(-((np.minimum(frac, 1 - frac)) / glue_w) ** 2)
odd = (idx % 2 == 1)
for f, g in (('color.jpg', False), ('rough.jpg', True), ('height.jpg', True)):
    a, b = ld(A, f, g), ld(B, f, g)
    sel = odd[:, None, None] if not g else odd[:, None]
    m = np.where(sel, b, a)
    gl = glue[:, None, None] if not g else glue[:, None]
    if f == 'color.jpg':
        m = m * (1 - 0.45 * gl) + np.array([0.33, 0.24, 0.15]) * 0.45 * gl
    elif f == 'height.jpg':
        m = m * (1 - 0.5 * gl)
    else:
        m = np.clip(m + 0.1 * gl, 0, 1)
    Image.fromarray((np.clip(m, 0, 1) * 255).astype(np.uint8), 'L' if g else 'RGB').save(os.path.join(O, f), quality=92)
print('plywood: %d plies' % n_plies)
