"""Turn a colour + normal map pair into the Color / Roughness / Displacement set bake.py reads.

Used when only colour and normal maps are available (e.g. the ambientCG scans in the
PatrickJnr/cc0-texture-pack mirror, decoded from .vtex_c with Source2Viewer-CLI).

usage: python3 prep.py <color.png> <normal.png|-> <out_dir> '<json opts>'
opts: rough (base roughness 0-1), rough_var (how much darker/lighter areas change roughness),
      sat (saturation x), bright (brightness x), tint ([r,g,b] multipliers), gray (true = desaturate),
      hue_to ([r,g,b] target colour: keeps the texture's light/dark detail, recolours it),
      size (resize to this square size, default 2048), rot90 (true = rotate texture 90 degrees)
Height comes from the normal map by Frankot-Chellappa integration; both green-channel
conventions are tried and the one that integrates more cleanly is kept.
"""
import sys, os, json
import numpy as np
from PIL import Image, ImageEnhance

def integrate(n):
    nx = n[..., 0] * 2 - 1; ny = n[..., 1] * 2 - 1; nz = np.clip(n[..., 2] * 2 - 1, 0.2, 1)
    H, W = nx.shape
    wx = np.fft.fftfreq(W) * 2 * np.pi; wy = np.fft.fftfreq(H) * 2 * np.pi
    WX, WY = np.meshgrid(wx, wy)
    den = WX ** 2 + WY ** 2; den[0, 0] = 1
    best = None
    for sy in (1, -1):
        p = -nx / nz; q = -(sy * ny) / nz  # dz/dx, dz/d(row)
        P = np.fft.fft2(p); Q = np.fft.fft2(q)
        Z = (-1j * WX * P - 1j * WY * Q) / den; Z[0, 0] = 0
        z = np.real(np.fft.ifft2(Z))
        # residual: how well the height reproduces the given slopes
        gx = (np.roll(z, -1, 1) - np.roll(z, 1, 1)) / 2; gy = (np.roll(z, -1, 0) - np.roll(z, 1, 0)) / 2
        r = np.mean((gx - p) ** 2 + (gy - q) ** 2)
        if best is None or r < best[0]:
            best = (r, z, sy)
    z = best[1]
    lo, hi = np.percentile(z, [0.5, 99.5])
    return np.clip((z - lo) / max(hi - lo, 1e-6), 0, 1), best[2]

if __name__ == '__main__':
    cpath, npath, out = sys.argv[1], sys.argv[2], sys.argv[3]
    o = json.loads(sys.argv[4]) if len(sys.argv) > 4 else {}
    size = o.get('size', 2048)
    os.makedirs(out, exist_ok=True)
    col = Image.open(cpath).convert('RGB').resize((size, size), Image.LANCZOS)
    if o.get('rot90'): col = col.rotate(90)
    if o.get('gray'): col = col.convert('L').convert('RGB')
    if 'sat' in o: col = ImageEnhance.Color(col).enhance(o['sat'])
    a = np.asarray(col).astype(np.float32) / 255
    if 'hue_to' in o:
        lum = a.mean(-1, keepdims=True); a = lum / max(lum.mean(), 1e-6) * np.array(o['hue_to'], np.float32) / 255
    if 'tint' in o: a = a * np.array(o['tint'], np.float32)
    a = a * o.get('bright', 1.0)
    a = np.clip(a, 0, 1)
    Image.fromarray((a * 255).astype(np.uint8)).save(os.path.join(out, 'Color.jpg'), quality=94)
    lum = a.mean(-1)
    rough = np.clip(o.get('rough', 0.8) + o.get('rough_var', 0.15) * (lum.mean() - lum) / max(lum.std(), 1e-6) * 0.25, 0.02, 1)
    Image.fromarray((rough * 255).astype(np.uint8), 'L').save(os.path.join(out, 'Roughness.jpg'), quality=94)
    if npath != '-':
        n = np.asarray(Image.open(npath).convert('RGB').resize((size, size), Image.LANCZOS)).astype(np.float32) / 255
        if o.get('rot90'): n = np.rot90(n).copy(); n[..., [0, 1]] = n[..., [1, 0]]; n[..., 1] = 1 - n[..., 1]
        h, sy = integrate(n)
        Image.fromarray((h * 255).astype(np.uint8), 'L').save(os.path.join(out, 'Displacement.jpg'), quality=94)
        print(out, 'height ok (green', '+' if sy > 0 else '-', ')')
    else:
        print(out, 'no height')
