# contact sheet of composed spheres: python3 sheet.py out.jpg comp/a.jpg comp/b.jpg ...
import sys, os
from PIL import Image, ImageDraw
out, fs = sys.argv[1], sys.argv[2:]; T = 320; c = min(5, len(fs)); r = (len(fs) + c - 1) // c
S = Image.new('RGB', (c * T, r * (T + 18)), 'white'); d = ImageDraw.Draw(S)
for i, f in enumerate(fs):
    x, y = (i % c) * T, (i // c) * (T + 18); S.paste(Image.open(f).resize((T, T)), (x, y + 18)); d.text((x + 4, y + 3), os.path.basename(f)[:-4], fill='black')
S.save(out, quality=88)
