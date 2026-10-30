"""Flat (tileable) texture maps for swatches, for materials that have no scan. Writes src/<key>/
Color.jpg, Roughness.jpg, Displacement.jpg (what swatch.html reads).
usage: python3 gen_flat.py <kind> <key> [json opts]
kinds:
  plain  - fine noise height, slight colour mottle (rubbers, bio-plastics, ceramics)
  beads  - bead foam (EPS/EPP/loose fill): round beads, evenly spaced, tileable
  cells  - fine closed-cell foam (neoprene)
  split  - whole swatch, NOT tiled (render with tiles 0.75 -> one repeat): polished on one side of the
           diagonal, matte or the given scan on the other, so a corner-hung swatch shows a vertical split
           (Rob: plastics and metals half gloss / half matte). opts: src (scan key for the matte side, or
           none), gloss (roughness of the polished half), matte (roughness when no scan).
"""
import sys, os, json
import numpy as np
from PIL import Image
kind, key = sys.argv[1], sys.argv[2]
o = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
S = o.get('size', 1024); O = f'src/{key}'; os.makedirs(O, exist_ok=True)
rng = np.random.default_rng(o.get('seed', 11))

def pnoise(f, octaves=4):
    """periodic noise from filtered white noise (tiles seamlessly)"""
    out = np.zeros((S, S), np.float32); a = 1.0
    fy = np.fft.fftfreq(S)[:, None]; fx = np.fft.fftfreq(S)[None, :]; r = np.sqrt(fx ** 2 + fy ** 2)
    for i in range(octaves):
        ff = f * 2 ** i / S
        spec = np.fft.fft2(rng.normal(size=(S, S))) * np.exp(-(r / ff) ** 2)
        n = np.real(np.fft.ifft2(spec)); n /= n.std() + 1e-9; out += a * n; a *= .5
    return out / np.abs(out).max()

def voronoi(n):
    from scipy.spatial import cKDTree
    k = int(np.sqrt(n)); g = (np.stack(np.meshgrid(np.arange(k), np.arange(k)), -1).reshape(-1, 2) + .5) / k
    pts = (g + rng.normal(scale=.22 / k, size=g.shape)) % 1
    tiled = np.concatenate([pts + [dx, dy] for dx in (-1, 0, 1) for dy in (-1, 0, 1)])
    yy, xx = np.mgrid[0:S, 0:S] / S
    d, i = cKDTree(tiled).query(np.stack([xx.ravel(), yy.ravel()], 1), k=2)
    return d[:, 0].reshape(S, S), d[:, 1].reshape(S, S), (i[:, 0] % len(pts)).reshape(S, S), 1 / k

col = np.ones((S, S, 3), np.float32); rough = np.full((S, S), o.get('rough', .6), np.float32); h = np.full((S, S), .5, np.float32)
if kind == 'plain':
    h = .5 + .5 * pnoise(o.get('freq', 90), 3) * o.get('amp', 1)
    col *= (1 + o.get('mottle', .03) * pnoise(6, 3))[..., None]
elif kind in ('beads', 'cells'):
    d1, d2, idx, sp = voronoi(o.get('n', 900))
    tone = 1 - o.get('var', .06) * ((np.sin(idx * 12.9898) * 43758.5453) % 1)
    if kind == 'beads':
        R = .62 * sp * (1 + .2 * (((np.sin(idx * 78.233) * 43758.5453) % 1) - .5))
        r = d1 / R; hh = np.sqrt(np.clip(1 - r ** 2, 0, 1)); hh = np.minimum(hh, np.clip((d2 - d1) / (R * .35), 0, 1) ** .5)
        edge = np.clip((1 - r) / .25, 0, 1)
    else:
        edge = np.clip((d2 - d1) / (sp * .08), 0, 1); hh = 1 - (1 - edge) * .8
    h = hh; col *= ((.65 + .35 * edge) * tone)[..., None]; rough = rough + .15 * (1 - hh)
elif kind == 'split':
    yy, xx = np.mgrid[0:S, 0:S] / S
    v = 1 - yy                                   # texture v runs upwards
    matte = 0.5 * (1 + np.tanh((xx - v) / .004)) # polished where u < v -> left half of the hanging diamond
    groove = np.exp(-((xx - v) / .005) ** 2)
    if o.get('src'):
        reps = o.get('reps', 4)
        ld = lambda f, m: np.asarray(Image.open(f'src/{o["src"]}/{f}').convert(m).resize((S // reps, S // reps), Image.LANCZOS)).astype(np.float32) / 255
        c, r_, hh = ld('Color.jpg', 'RGB'), ld('Roughness.jpg', 'L'), ld('Displacement.jpg', 'L')
        tile = lambda a: np.tile(a, (reps, reps, 1) if a.ndim == 3 else (reps, reps))[:S, :S]
        c, r_, hh = tile(c), tile(r_), tile(hh)
        if o.get('gray'): c = np.repeat(c.mean(-1, keepdims=True), 3, -1)
        col = c * matte[..., None] + c.reshape(-1, 3).mean(0) * (1 - matte[..., None])
        rough = r_ * matte + o.get('gloss', .05) * (1 - matte); h = hh * matte + hh.mean() * (1 - matte)
    else:
        n = pnoise(140, 2)
        rough = o.get('gloss', .06) * (1 - matte) + (o.get('matte', .52) + .06 * n) * matte
        h = .5 + .25 * n * matte
    h = h - .35 * groove
sv = lambda a, f, m: Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8), m).save(os.path.join(O, f), quality=94)
sv(col, 'Color.jpg', 'RGB'); sv(rough, 'Roughness.jpg', 'L'); sv((h - h.min()) / max(h.max() - h.min(), 1e-6), 'Displacement.jpg', 'L')
print(O, kind)
