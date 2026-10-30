"""Procedural baked maps (no texture): python3 gen.py <kind> <key> [json opts]
kinds: plain (flat colour, fine noise), beads (bead foam: EPS/EPP/loose fill, 3D Voronoi
cells), crumple (wrinkled film), cells (fine closed-cell foam). Output baked/<key>/ in the
sphere's UV layout (2048 x 1024, three.js SphereGeometry)."""
import sys, os, json, numpy as np
from PIL import Image
kind, key = sys.argv[1], sys.argv[2]; o = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
W, H = 2048, 1024; O = f'baked/{key}'; os.makedirs(O, exist_ok=True)
u = (np.arange(W) + .5) / W; v = (np.arange(H) + .5) / H; U, V = np.meshgrid(u, v)
th, ph = U * 2 * np.pi, V * np.pi
P = np.stack([-np.cos(th) * np.sin(ph), np.cos(ph), np.sin(th) * np.sin(ph)], -1).astype(np.float32)
rng = np.random.default_rng(o.get('seed', 7))
def vnoise(P, f, oct=4):
    out = np.zeros(P.shape[:2], np.float32); a = 1
    for i in range(oct):
        d = rng.normal(size=(12, 3)).astype(np.float32); ph0 = rng.random(12).astype(np.float32) * 6.28
        out += a * np.mean(np.sin((P @ d.T) * f * (2 ** i) + ph0), -1); a *= .5
    return out
def voronoi(P, n):
    from scipy.spatial import cKDTree
    # evenly spaced (Fibonacci sphere + jitter), so beads are similar in size like real bead foam
    k = np.arange(n) + .5; z = 1 - 2 * k / n; t = np.pi * (1 + 5 ** .5) * k
    pts = np.stack([np.sqrt(1 - z * z) * np.cos(t), z, np.sqrt(1 - z * z) * np.sin(t)], 1)
    pts += rng.normal(scale=.35 * np.sqrt(4 / n), size=pts.shape); pts = (pts / np.linalg.norm(pts, axis=1, keepdims=True)).astype(np.float32)
    d, i = cKDTree(pts).query(P.reshape(-1, 3), k=2)
    return d[:, 0].reshape(P.shape[:2]).astype(np.float32), d[:, 1].reshape(P.shape[:2]).astype(np.float32), i[:, 0].reshape(P.shape[:2])
col = np.ones((H, W, 3), np.float32); rough = np.full((H, W), o.get('rough', .6), np.float32); h = np.full((H, W), .5, np.float32)
if kind == 'plain':
    n = vnoise(P, o.get('freq', 60), 3); h = .5 + .15 * n * o.get('amp', 1)
    col *= (1 + o.get('mottle', .03) * vnoise(P, 6, 3))[..., None]
elif kind in ('beads', 'cells'):
    # Voronoi on a coarse grid then upsampled (fast); beads = domes with dark seams
    s = 1
    d1, d2, idx = voronoi(P[::s, ::s], o.get('n', 3000))
    edge = np.clip((d2 - d1) / o.get('seam', .004), 0, 1)
    tone = 1 - o.get('var', .06) * (np.sin(idx * 12.9898) * 43758.5453 % 1)
    if kind == 'beads':   # rounded domes: high at the bead centre, falling to the seam between beads
        R = .6 * np.sqrt(4 * np.pi / o.get('n', 3000)) * o.get('size', 1) * (1 + .25 * (np.sin(idx * 78.233) * 43758.5453 % 1 - .5))
        r = d1 / R; hh = np.sqrt(np.clip(1 - r ** 2, 0, 1)); edge = np.clip((1 - r) / .25, 0, 1)
        hh = np.minimum(hh, np.clip((d2 - d1) / (R * .35), 0, 1) ** .5)   # beads press into each other
    else:
        hh = 1 - (1 - edge) * .8
    up = lambda a: np.asarray(Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC)).astype(np.float32) / 255
    h = up(hh); sh = up(.65 + .35 * edge) * up(tone)
    col *= sh[..., None]
    rough = np.full((H, W), o.get('rough', .7), np.float32) + .15 * (1 - h)
elif kind == 'crumple':
    n = np.zeros((H, W), np.float32)
    for f in (3, 7, 15, 31):
        n += np.abs(vnoise(P, f, 1)) / f ** .4
    h = 1 - n / n.max(); rough = np.full((H, W), o.get('rough', .08), np.float32)
sv = lambda a, f, m: Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8), m).save(os.path.join(O, f), quality=94)
sv(col, 'color.jpg', 'RGB'); sv(rough, 'rough.jpg', 'L'); sv((h - h.min()) / max(h.max() - h.min(), 1e-6), 'height.jpg', 'L')
print(O, kind)
