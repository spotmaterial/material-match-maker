"""Generated hanging swatches for all Spotlight innovations (Rob, 31 Oct): stand-ins for the companies'
photos (copyright). Each innovation reuses one of the 103 general swatch looks (its form, thickness, gloss)
recoloured / patterned after the innovation's description, tags and a look at its photo for colour only.
Nothing is traced or copied from the photo; maps come from our CC0 scans and procedural patterns.
usage: python3 inn_all.py [code ...]   -> comp/inn-<code>.jpg  (specs in inn_specs.py)

Spec: code: (general key, rgb or None, options)
  options: mm (rigid thickness), soft (stiff, shape, sag), tiles, p (render param overrides),
           tint opts (contrast, rough, rough_add, rgb2, mottle, mfreq), g = (gen_inn kind, opts) to replace the tint
"""
import sys, os, json, subprocess
_s = open('swatch_all.py').read(); exec(_s[:_s.rindex('if __name__')])      # job(), run(), B1, F2 ...
from inn_specs import SPEC

FULLER = {'knit': (.22, .003, .65), 'silk': (.2, .003, .65), 'yarn-light': (.25, .004, .6), 'yarn-natural': (.25, .004, .6), 'yarn-coir': (.3, .004, .6)}
hexc = lambda c: '#%02x%02x%02x' % tuple(int(v) for v in c)

def build(code):
    key, rgb, o = SPEC[code]
    slug, p = job(key)
    p = {k: v for k, v in p.items()}
    tint = {k: o[k] for k in ('contrast', 'rough', 'rough_add', 'rgb2', 'mottle', 'mfreq', 'mpow', 'seed') if k in o}
    if key in ('silk', 'yarn-light') and 'contrast' not in tint: tint['contrast'] = .25   # tone down the rope stripes
    if 'g' in o:
        kind, go = o['g']; go = dict(go)
        if kind in ('relief', 'strips') and 'base' not in go: go['base'] = slug
        if kind in ('relief', 'strips') and rgb is not None and 'hue_to' not in go: go['hue_to'] = list(rgb)
        run('python3', '-I', 'gen_inn.py', kind, f'inn-{code}', json.dumps(go)); slug = f'inn-{code}'
        p.pop('noMap', None)
    elif rgb is not None:
        if p.get('noMap') or slug.startswith('split-'): p['color'] = hexc(rgb)
        else:
            run('python3', '-I', 'gen_inn.py', 'tint', f'inn-{code}', json.dumps({'base': slug, 'rgb': list(rgb), **tint})); slug = f'inn-{code}'
            p.pop('color', None)
    if 'mm' in o: p.update({'stiff': 1, 'thickMM': o['mm']}); [p.pop(k, None) for k in ('shape', 'sag')]
    if key in FULLER and 'soft' not in o: o = {**o, 'soft': FULLER[key]}     # show the cloth, not a strip
    if 'soft' in o:
        st, sh, sg = o['soft']; p.pop('thickMM', None); p['stiff'] = st
        p.pop('shape', None); p.pop('sag', None)
        if sh is not None: p['shape'] = sh
        if sg is not None: p['sag'] = sg
    if 'tiles' in o: p['tiles'] = o['tiles']
    p.update(o.get('p', {}))
    return {'slug': slug, 'out': f'inn-{code}', 'params': p}

if __name__ == '__main__':
    codes = sys.argv[1:] or list(SPEC)
    jobs, glass = [], []
    for c in codes:
        j = build(c); jobs.append(j)
        if j['params'].get('backdrop'):
            glass.append(j['out']); jobs.append({**j, 'out': j['out'] + '-mask', 'params': {**j['params'], 'transmission': 0, 'backdrop': False}})
    for i in range(0, len(jobs), 10):
        print(run('node', 'runsw.js', json.dumps(jobs[i:i + 10])).count('rendered'), 'rendered', min(i + 10, len(jobs)), '/', len(jobs), flush=True)
    for c in codes:
        out = f'inn-{c}'; src = f'outsw/{out}.png'
        if out in glass: run('python3', '-I', 'glass_merge.py', out, 'outsw'); src = f'outsw/{out}-final.png'
        run('python3', '-I', 'compose.py', src, f'comp/{out}.jpg', '640')
    print('done', len(codes))
