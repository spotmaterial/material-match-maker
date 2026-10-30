"""Hanging swatches for every image in spheres/ (Rob, 30 Oct: squares hanging from one corner in a white
space, no visible wire; rigid materials stay flat and show their thickness, soft ones drape).
usage: python3 swatch_all.py [key ...]  -> outsw/<key>.png, comp/sw-<key>.jpg (640 px)
Needs the http server on :8765 (README) and the flat maps in src/<key>/ (prep.py / gen_flat.py).

Each image key: texture source, tiles (per 15 cm, as for the spheres), material params, form.
Form: ('rigid', thickness_mm) or ('soft', stiffness 0..1, shape memory or None, sag or None).
"""
import sys, os, json, subprocess
exec(open('draft2.py').read().split("if __name__")[0])          # J: texture / tiles / params of batch 2

RIGID = lambda mm: ('rigid', mm)
SOFT = lambda st, shape=None, sag=None: ('soft', st, shape, sag)
GLASS = {'roughness': 0, 'transmission': 1, 'ior': 1.5, 'thickness': 0.15, 'env': 'soft', 'noMap': True, 'backdrop': True}
METAL = {'metalness': 1, 'env': 'soft', 'bumpScale': 0.15}

# batch-1 images (textures in src/<key> from jobs.sh, params from params.json / params2.json)
B1 = {
 'oak': ('oak', .22, {'bumpScale': 1.2, 'clearcoat': .15, 'clearcoatRoughness': .5}, RIGID(20)),
 'softwood': ('softwood', .22, {'bumpScale': 1, 'clearcoat': .1, 'clearcoatRoughness': .5}, RIGID(20)),
 'plywood': ('plywood-face', .25, {'bumpScale': .8, 'plies': 11}, RIGID(18)),
 'cork': ('cork', .9, {'bumpScale': 1.4}, RIGID(10)),
 'wool-felt': ('wool-felt', 1.2, {'bumpScale': .5, 'sheen': 1, 'sheenColor': '#bdb7ae', 'sheenRoughness': .6}, SOFT(.75, .02, .2)),
 'pet-felt': ('pet-felt', .9, {'bumpScale': .4, 'sheen': .8, 'sheenColor': '#b5b5b5', 'sheenRoughness': .6}, SOFT(.85, .035, .1)),
 'woven-synthetic': ('woven-synthetic', .45, {'bumpScale': 2.5, 'sheen': .4, 'sheenColor': '#9a9a9a', 'sheenRoughness': .5}, SOFT(.1, None, .8)),
 'woven-natural': ('woven-natural', .45, {'bumpScale': 1.6, 'sheen': .3, 'sheenColor': '#efe6d6', 'sheenRoughness': .7}, SOFT(.12, None, .8)),
 'leather': ('leather', .35, {'bumpScale': 1.5, 'clearcoat': .25, 'clearcoatRoughness': .45}, SOFT(.45, .006, .5)),
 'concrete': ('concrete', .2, {'bumpScale': 2}, RIGID(25)),
 'clear-glass': (None, 0, {**GLASS, 'color': '#eef6f2'}, RIGID(8)),
 'plastic': ('split:plastic', .75, {'color': '#8c8d8e', 'bumpScale': .6, 'env': 'soft', 'clearcoat': .2, 'clearcoatRoughness': .1}, RIGID(4)),
 'aluminium': ('split:aluminium', .75, {**METAL, 'color': '#f2f3f4'}, RIGID(3)),
 'stainless': ('split:stainless', .75, {**METAL, 'color': '#e1e1df'}, RIGID(3)),
 'copper': ('split:aluminium', .75, {**METAL, 'color': '#e8a57e'}, RIGID(3)),
 'gold': ('split:aluminium', .75, {**METAL, 'color': '#f3cf7a'}, RIGID(2)),
 'silver': ('split:aluminium', .75, {**METAL, 'color': '#fbfbf9'}, RIGID(2)),
}
# batch-2 forms (textures / params from draft2.J)
F2 = {**{k: RIGID(20) for k in ('ash', 'balsa', 'beech', 'birch', 'chestnut', 'elm', 'cherry', 'maple', 'poplar', 'sycamore', 'teak', 'walnut', 'wenge', 'cedar',
                                'marble', 'granite', 'gabbro', 'basalt', 'slate', 'sandstone', 'limestone', 'quartz', 'clay')},
 'gypsum': RIGID(12), 'lime': RIGID(15), 'brick': RIGID(25), 'polymer-concrete': RIGID(15), 'solid-surface': RIGID(12),
 'porcelain': RIGID(8), 'tech-ceramic': RIGID(8), 'glass-ceramic': RIGID(5), 'diamond': RIGID(6),
 'paper': SOFT(.6, .02, .3), 'moulded-pulp': RIGID(3), 'chipboard': RIGID(18), 'wood-fibre-board': RIGID(25), 'hemp-board': RIGID(30), 'coir-board': RIGID(20),
 'carbon-fibre': RIGID(3), 'glass-fibre': RIGID(3), 'basalt-fibre': RIGID(3), 'flax-composite': RIGID(4), 'bamboo-composite': RIGID(12), 'fibre-filled-plastic': RIGID(4),
 'aramid': SOFT(.2, None, .7), 'glass-wool': SOFT(.7, .02, .2), 'basalt-felt': SOFT(.75, .025, .15), 'wool-pile': SOFT(.3, .003, .6), 'fur': SOFT(.3, .003, .6),
 'knit': SOFT(.06, None, .9), 'jute': SOFT(.25, .002, .6),
 'yarn-natural': SOFT(.2, None, .7), 'yarn-coir': SOFT(.3, .002, .6), 'yarn-light': SOFT(.15, None, .8), 'silk': SOFT(.1, None, .8), 'grass-weave': SOFT(.6, .02, .3),
 'suede': SOFT(.4, .004, .5), 'exotic-leather': SOFT(.55, .01, .4), 'mycelium-leather': SOFT(.5, .006, .5), 'pinatex': SOFT(.55, .01, .4),
 'mycelium': RIGID(20), 'starch': RIGID(5), 'lignin': RIGID(4), 'seaweed': SOFT(.5, .008, .4),
 'natural-rubber': SOFT(.55, .01, .4), 'synthetic-rubber': SOFT(.55, .01, .4), 'silicone': SOFT(.45, .006, .5), 'tpe': SOFT(.5, .008, .4),
 'eps': RIGID(30), 'epp': RIGID(30), 'pla-foam': RIGID(30), 'starch-foam': RIGID(30), 'rigid-pu': RIGID(30), 'pet-foam': RIGID(30), 'aluminium-foam': RIGID(15), 'aerogel': RIGID(15),
 'tpu-beads': SOFT(.8, .03, .15), 'open-foam-yellow': SOFT(.8, .03, .15), 'open-foam-grey': SOFT(.8, .03, .15), 'latex-foam': SOFT(.75, .025, .2), 'neoprene': SOFT(.7, .02, .2),
 'film': SOFT(.02, None, 1), 'translucent': RIGID(4),
 'platinum': RIGID(2), 'tin': RIGID(2), 'silicon': RIGID(1),
}
GENFLAT = {   # generated flat maps for batch-2 images without a scan
 'tech-ceramic': ('plain', {'rough': .45, 'freq': 120, 'amp': .3}), 'glass-ceramic': ('plain', {'rough': .04, 'freq': 80, 'amp': .05}),
 'starch': ('plain', {'rough': .7, 'freq': 90, 'amp': .6, 'mottle': .06}), 'lignin': ('plain', {'rough': .45, 'freq': 90, 'amp': .4, 'mottle': .08}),
 'seaweed': ('plain', {'rough': .4, 'freq': 50, 'amp': .5, 'mottle': .1}),
 'natural-rubber': ('plain', {'rough': .65, 'freq': 140, 'amp': .3}), 'synthetic-rubber': ('plain', {'rough': .75, 'freq': 140, 'amp': .3}),
 'silicone': ('plain', {'rough': .55, 'freq': 140, 'amp': .2}), 'tpe': ('plain', {'rough': .6, 'freq': 140, 'amp': .2}),
 'eps': ('beads', {'n': 900, 'rough': .8}), 'epp': ('beads', {'n': 900, 'rough': .7}), 'pla-foam': ('beads', {'n': 800, 'rough': .75}),
 'starch-foam': ('beads', {'n': 160, 'rough': .9, 'var': .15}), 'tpu-beads': ('beads', {'n': 500, 'rough': .55, 'var': .03}),
 'neoprene': ('cells', {'n': 2500, 'rough': .8}),
}
SPLIT_MAPS = {'plastic': {'gloss': .06, 'matte': .52}, 'aluminium': {'src': 'aluminium', 'gloss': .05, 'gray': True}, 'stainless': {'src': 'stainless', 'gloss': .03, 'gray': True}}
DROP = {'rotY', 'rotX', 'castShadow', 'contactOpacity', 'shadowOpacity', 'anisotropy', 'anisotropyRotation', 'attenuationColor', 'attenuationDistance', 'envIntensity'}

def job(k):
    if k in B1:
        src, tiles, params, form = B1[k]
    else:
        s, tiles, po, params, ex = J[k]
        params = {a: b for a, b in params.items() if a not in DROP}
        form = F2[k]
        if s.startswith('tex:'): src = k
        elif s.startswith('gen:'): src = k if k in GENFLAT else None; tiles = .75
        elif s.startswith('split:'): src = 'split:' + s[6:]; tiles = .75; params = {**METAL, 'color': params.get('color')}
        else: src = None
        if params.get('env') == 'studio': params['env'] = 'soft'
        if ex.get('glass') or (src is None and params.get('transmission')):
            params = {**params, 'noMap': True, 'backdrop': True, 'thickness': .15}
        if k == 'film': params = {'noMap': True, 'opacity': .28, 'roughness': .04, 'clearcoat': 1, 'clearcoatRoughness': .03, 'color': '#e8eef0'}
    p = dict(params)
    if src is None: p['noMap'] = True
    p['tiles'] = tiles or .75
    if form[0] == 'rigid': p.update({'stiff': 1, 'thickMM': form[1]})
    else:
        p['stiff'] = form[1]
        if form[2] is not None: p['shape'] = form[2]
        if form[3] is not None: p['sag'] = form[3]
    slug = src.replace('split:', 'split-') if src else k
    return slug, p

def run(*a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode: print(r.stdout[-300:], r.stderr[-600:]); raise SystemExit(f'failed: {a[:3]}')
    return r.stdout

if __name__ == '__main__':
    keys = sys.argv[1:] or sorted(f[:-4] for f in os.listdir('..') if f.endswith('.jpg'))
    for k, (kind, opts) in GENFLAT.items():
        if k in keys and not os.path.exists(f'src/{k}/Color.jpg'): run('python3', '-I', 'gen_flat.py', kind, k, json.dumps(opts))
    for name, opts in SPLIT_MAPS.items():
        if not os.path.exists(f'src/split-{name}/Color.jpg'): run('python3', '-I', 'gen_flat.py', 'split', f'split-{name}', json.dumps(opts))
    jobs, glass = [], []
    for k in keys:
        slug, p = job(k)
        out = 'sw-' + k
        jobs.append({'slug': slug, 'out': out, 'params': p})
        if p.get('backdrop'):
            glass.append(out); jobs.append({'slug': slug, 'out': out + '-mask', 'params': {**p, 'transmission': 0, 'backdrop': False}})
    for i in range(0, len(jobs), 10):
        print(run('node', 'runsw.js', json.dumps(jobs[i:i + 10])).count('rendered'), 'rendered', i + 10, '/', len(jobs), flush=True)
    for k in keys:
        out = 'sw-' + k; src = f'outsw/{out}.png'
        if out in glass: run('python3', '-I', 'glass_merge.py', out, 'outsw'); src = f'outsw/{out}-final.png'
        run('python3', '-I', 'compose.py', src, f'comp/{out}.jpg', '640')
    print('done', len(keys))
