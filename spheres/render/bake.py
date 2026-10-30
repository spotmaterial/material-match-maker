"""Bake a flat (tileable) material texture onto a sphere's equirectangular UV map using
triplanar projection, so the sphere has no seam and no pinched poles.

usage: python3 bake.py <src_dir> <out_dir> <tiles_per_sphere> [size]
src_dir holds the ambientCG / Poly Haven maps; recognised by name:
  *Color* / *diff*           -> colour
  *Roughness* / *rough*      -> roughness
  *Displacement* / *disp*    -> height (used as bump)
  *Metalness* / *metal*      -> metalness
  *Opacity*                  -> ignored
tiles_per_sphere: how many texture repeats across the sphere's diameter (sets real-world scale).
"""
import sys, os, glob
import numpy as np
from PIL import Image

def find(src, keys):
    for f in sorted(glob.glob(os.path.join(src, '*'))):
        n = os.path.basename(f).lower()
        if any(k in n for k in keys) and n.endswith(('.jpg', '.jpeg', '.png')):
            return f
    return None

def load(path, gray=False):
    im = Image.open(path)
    im = im.convert('L' if gray else 'RGB')
    a = np.asarray(im).astype(np.float32) / (65535.0 if im.mode == 'I;16' else 255.0)
    return a

def triplanar(tex, tiles, W, H, sharp=6.0):
    th, tw = tex.shape[:2]
    u = (np.arange(W) + 0.5) / W
    v = (np.arange(H) + 0.5) / H
    U, V = np.meshgrid(u, v)
    theta = U * 2 * np.pi
    phi = V * np.pi
    x = np.sin(phi) * np.cos(theta)
    y = np.cos(phi)
    z = np.sin(phi) * np.sin(theta)
    w = np.stack([np.abs(x), np.abs(y), np.abs(z)], -1) ** sharp
    w /= w.sum(-1, keepdims=True)
    s = tiles / 2.0  # sphere radius 1 -> diameter 2

    def sample(a, b):
        px = ((a * s) % 1.0) * (tw - 1)
        py = ((b * s) % 1.0) * (th - 1)
        x0 = np.floor(px).astype(int); y0 = np.floor(py).astype(int)
        x1 = (x0 + 1) % tw; y1 = (y0 + 1) % th
        fx = px - x0; fy = py - y0
        if tex.ndim == 3:
            fx = fx[..., None]; fy = fy[..., None]
        top = tex[y0, x0] * (1 - fx) + tex[y0, x1] * fx
        bot = tex[y1, x0] * (1 - fx) + tex[y1, x1] * fx
        return top * (1 - fy) + bot * fy

    sx = sample(z, y)   # projection along x
    sy = sample(x, z)   # along y
    sz = sample(x, y)   # along z
    if tex.ndim == 3:
        return sx * w[..., 0:1] + sy * w[..., 1:2] + sz * w[..., 2:3]
    return sx * w[..., 0] + sy * w[..., 1] + sz * w[..., 2]

def save(a, path, gray=False):
    a = np.clip(a, 0, 1)
    Image.fromarray((a * 255).astype(np.uint8), 'L' if gray else 'RGB').save(path, quality=92)

if __name__ == '__main__':
    src, out, tiles = sys.argv[1], sys.argv[2], float(sys.argv[3])
    size = int(sys.argv[4]) if len(sys.argv) > 4 else 2048
    W, H = size, size // 2
    os.makedirs(out, exist_ok=True)
    maps = {
        'color': (['color', 'diff', 'albedo', 'basecolor'], False),
        'rough': (['roughness', 'rough'], True),
        'height': (['displacement', 'disp', 'height'], True),
        'metal': (['metalness', 'metal'], True),
    }
    for name, (keys, gray) in maps.items():
        f = find(src, keys)
        if not f:
            continue
        tex = load(f, gray)
        save(triplanar(tex, tiles, W, H), os.path.join(out, name + '.jpg'), gray)
        print(name, '<-', os.path.basename(f))
