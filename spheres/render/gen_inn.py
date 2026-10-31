"""Flat, tileable maps for innovation swatches (Rob, 31 Oct: generated stand-ins for the companies' photos,
to avoid the image-copyright problem). Each look is built from our own CC0 scans and procedural patterns,
following the innovation's description and tags; nothing is traced from the company photo.
usage: python3 gen_inn.py <kind> <key> '<json opts>'   -> src/<key>/Color.jpg, Roughness.jpg, Displacement.jpg
kinds:
  relief  - a base scan (opts.base = src key) with a moulded relief pattern on top:
            pattern 'chevron' (rows of zig-zag ridges), 'ribs' (parallel diagonal ribs), 'waves'; opts.rows, depth
  flecks  - a base colour with scattered flecks / short fibres in several colours (recycled textile, plastic,
            wood-filled bioplastic): base, colors [[r,g,b,weight]...], n, size, fibre (length/size ratio), gloss
  strips  - vertical strips (bamboo): base scan tinted per strip, node lines across: base, strips, nodes
"""
import sys, os, json
import numpy as np
from PIL import Image
kind, key = sys.argv[1], sys.argv[2]
o = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
S = 1024; O = f'src/{key}'; os.makedirs(O, exist_ok=True)
rng = np.random.default_rng(o.get('seed', 5))
yy, xx = np.mgrid[0:S, 0:S] / S

def base(k):
    ld = lambda f, m: np.asarray(Image.open(f'src/{k}/{f}').convert(m).resize((S, S), Image.LANCZOS)).astype(np.float32) / 255
    return ld('Color.jpg', 'RGB'), ld('Roughness.jpg', 'L'), ld('Displacement.jpg', 'L')

def recolour(c, rgb):
    lum = c.mean(-1, keepdims=True); return np.clip(lum / max(lum.mean(), 1e-6) * np.array(rgb, np.float32) / 255, 0, 1)

def pnoise(f):
    fy = np.fft.fftfreq(S)[:, None]; fx = np.fft.fftfreq(S)[None, :]; r = np.sqrt(fx ** 2 + fy ** 2)
    n = np.real(np.fft.ifft2(np.fft.fft2(rng.normal(size=(S, S))) * np.exp(-(r / (f / S)) ** 2))); return n / (np.abs(n).max() + 1e-9)

if kind == 'relief':
    c, r, h = base(o['base'])
    if 'hue_to' in o: c = recolour(c, o['hue_to'])
    rows = o.get('rows', 2); p = o.get('pattern', 'chevron')
    if p == 'chevron':      # zig-zag ridges: triangle wave across, rows stacked
        tri = np.abs(((xx * rows * 2) % 2) - 1)                       # 0..1 zig-zag, period 1/rows
        t = (yy * rows * o.get('lines', 6) + tri * o.get('amp', 1.6)) % 1
        rel = 0.5 - 0.5 * np.cos(2 * np.pi * t)
    elif p == 'ribs':       # diagonal ribs with rounded tops
        t = ((xx + yy) * rows * o.get('lines', 5)) % 1
        rel = np.clip(np.sin(np.pi * t), 0, 1) ** .6
    else:                   # waves
        t = (yy * rows * o.get('lines', 6) + .15 * np.sin(2 * np.pi * xx * rows)) % 1
        rel = 0.5 - 0.5 * np.cos(2 * np.pi * t)
    d = o.get('depth', .8)
    h = np.clip(h * (1 - d) + rel * d, 0, 1)
    shade = 1 - o.get('ao', .12) * (1 - rel)                          # a little darker in the grooves
    c = c * shade[..., None]; r = np.clip(r + .05 * (1 - rel), 0, 1)
elif kind == 'flecks':
    c = np.ones((S, S, 3), np.float32) * np.array(o.get('base', [230, 228, 222]), np.float32) / 255
    c *= (1 + o.get('mottle', .04) * pnoise(8))[..., None]
    h = .5 + .15 * pnoise(160); r = np.full((S, S), o.get('rough', .55), np.float32)
    cols = np.array([x[:3] for x in o['colors']], np.float32) / 255; w = np.array([x[3] for x in o['colors']], np.float32); w /= w.sum()
    n, size, fib = o.get('n', 4000), o.get('size', .004), o.get('fibre', 1.0)
    img = (np.clip(c, 0, 1) * 255).astype(np.uint8); from PIL import ImageDraw
    im = Image.fromarray(img); dr = ImageDraw.Draw(im); hm = Image.fromarray((h * 255).astype(np.uint8)); dh = ImageDraw.Draw(hm)
    for i in range(n):
        x, y = rng.random() * S, rng.random() * S; col = tuple(int(min(255, max(0, v * 255))) for v in cols[rng.choice(len(w), p=w)] * (0.85 + 0.3 * rng.random()))
        s = size * S * (0.5 + rng.random()); a = rng.random() * np.pi
        L = s * fib
        for ox in (-S, 0, S):           # draw wrapped copies so the map tiles
            for oy in (-S, 0, S):
                if fib > 1.5:
                    pts = [(x + ox - np.cos(a) * L, y + oy - np.sin(a) * L), (x + ox + np.cos(a) * L, y + oy + np.sin(a) * L)]
                    dr.line(pts, fill=col, width=max(1, int(s * .5))); dh.line(pts, fill=150, width=max(1, int(s * .5)))
                else:
                    pts = [(x + ox + s * np.cos(a + k * 2.1 + rng.random() * .6), y + oy + s * np.sin(a + k * 2.1 + rng.random() * .6)) for k in range(3 + int(rng.random() * 3))]
                    dr.polygon(pts, fill=col); dh.polygon(pts, fill=140)
    c = np.asarray(im).astype(np.float32) / 255; h = np.asarray(hm).astype(np.float32) / 255
elif kind == 'strips':
    c, r, h = base(o['base'])
    if 'hue_to' in o: c = recolour(c, o['hue_to'])
    k = o.get('strips', 6); idx = np.floor(xx * k).astype(int)
    tone = 1 + o.get('var', .08) * (np.sin(idx * 12.9898) * 43758.5453 % 1 - .5)
    seam = np.exp(-(((xx * k) % 1) / .012) ** 2) + np.exp(-((1 - (xx * k) % 1) / .012) ** 2)
    nodes = np.zeros((S, S), np.float32)
    for j in range(o.get('nodes', 2)):
        ny = (j + 0.5) / o.get('nodes', 2) + 0.35 * (np.sin(idx * 7.13) * 43758.5453 % 1 - .5)
        nodes += np.exp(-(((yy - ny) % 1) / .0035) ** 2)
    c = c * tone[..., None] * (1 - .35 * np.clip(seam, 0, 1))[..., None] * (1 - .15 * np.clip(nodes, 0, 1))[..., None]
    h = np.clip(h - .3 * np.clip(seam, 0, 1) + .2 * np.clip(nodes, 0, 1), 0, 1)
sv = lambda a, f, m: Image.fromarray((np.clip(a, 0, 1) * 255).astype(np.uint8), m).save(os.path.join(O, f), quality=94)
sv(c, 'Color.jpg', 'RGB'); sv(r if kind != 'flecks' else r, 'Roughness.jpg', 'L'); sv((h - h.min()) / max(h.max() - h.min(), 1e-6), 'Displacement.jpg', 'L')
print(O, kind)
