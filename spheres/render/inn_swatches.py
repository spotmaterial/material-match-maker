"""Sample of Spotlight innovations as generated hanging swatches (Rob, 31 Oct), to test whether
generated images can stand in for the companies' photos (copyright). Looks follow each innovation's
description, tags and public product information; built only from CC0 scans and procedural patterns.
usage: python3 inn_swatches.py [code ...]  -> comp/inn-<code>.jpg
"""
import sys, os, json, subprocess
exec(open('draft2.py').read().split("if __name__")[0])     # ensure(), C, N (scan download + decode)

def run(*a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode: print(r.stdout[-300:], r.stderr[-600:]); raise SystemExit(f'failed: {a[:3]}')
    return r.stdout

# base scans made with prep.py (texture, options)
BASES = {
 'pulp-cream': ('fabric043', {'rough': 1, 'rough_var': .05, 'hue_to': [226, 214, 188]}),
 'myco-grey': ('fabric043', {'rough': 1, 'rough_var': .05, 'hue_to': [168, 163, 154]}),
 'bamboo-honey': ('wood017', {'rough': .6, 'rough_var': .15, 'hue_to': [212, 172, 112]}),
 'hemp-dark': ('wood026', {'rough': .55, 'rough_var': .2, 'hue_to': [112, 80, 52]}),
 'glass-terrazzo': ('terrazzo010', {'rough': .12, 'rough_var': .05}),
 'hemp-weave': ('fabric036', {'rough': .95, 'rough_var': .05, 'hue_to': [188, 172, 138]}),
 'mylo-grain': ('leather030', {'rough': .7, 'rough_var': .1, 'hue_to': [104, 78, 58]}),
}
RIGID = lambda mm: {'stiff': 1, 'thickMM': mm}
SOFT = lambda st, shape=None, sag=None: {'stiff': st, **({'shape': shape} if shape is not None else {}), **({'sag': sag} if sag is not None else {})}

# code: (label, generator or src, generator opts, tiles, render params)
INN = {
 # moulded pulp acoustic panel with chevron relief, wheat-tinted natural pulp
 'INN-0028': ('Baux acoustic pulp', ('relief', {'base': 'pulp-cream', 'pattern': 'chevron', 'rows': 2, 'lines': 3, 'amp': 1.4, 'depth': .9, 'ao': .18}), 1.5,
              {**RIGID(25), 'bumpScale': 6, 'roughness': 1}),
 # mycelium grown on agricultural residue, grey modular acoustic tile with ribs
 'INN-0195': ('Mogu mycelium acoustic panels', ('relief', {'base': 'myco-grey', 'pattern': 'ribs', 'rows': 1, 'lines': 6, 'depth': .85, 'ao': .2}), .75,
              {**RIGID(30), 'bumpScale': 7, 'sheen': .4, 'sheenColor': '#d8d4cc'}),
 # recycled textile fibres re-milled into a nonwoven board: grey base with multicolour fibre flecks
 'INN-0172': ('Kvadrat Really recycled textiles', ('flecks', {'base': [142, 142, 146], 'n': 5000, 'size': .0045, 'fibre': 5, 'rough': .9,
              'colors': [[60, 70, 110, 3], [170, 60, 60, 2], [220, 200, 120, 2], [40, 40, 44, 4], [230, 230, 228, 4], [90, 130, 100, 2]]}), .75,
              {**RIGID(16), 'bumpScale': 1.2}),
 # recycled glass pressed into a glass-ceramic slab: polished, glass fragments in a pale matrix
 'INN-0182': ('Magna Glaskeramik', ('src', 'glass-terrazzo'), .5, {**RIGID(20), 'bumpScale': .1, 'clearcoat': 1, 'clearcoatRoughness': .05, 'env': 'soft'}),
 # recycled HIPS from white goods: white sheet with grey and black flecks
 'INN-0274': ('Smile Plastics Heron', ('flecks', {'base': [236, 236, 232], 'n': 2500, 'size': .006, 'fibre': 1, 'rough': .3,
              'colors': [[30, 30, 32, 5], [120, 120, 122, 3], [180, 180, 178, 2]]}), .75, {**RIGID(12), 'bumpScale': .3, 'clearcoat': .5, 'clearcoatRoughness': .15}),
 # compressed hemp fibre "wood": dark, dense, striated
 'INN-0146': ('HempWood flooring', ('src', 'hemp-dark'), .25, {**RIGID(16), 'bumpScale': .8, 'clearcoat': .3, 'clearcoatRoughness': .25}),
 # bamboo plywood: vertical bamboo strips with nodes, layered edge
 'INN-0245': ('Plyboo bamboo panels', ('strips', {'base': 'bamboo-honey', 'strips': 7, 'nodes': 1, 'var': .14}), .75,
              {**RIGID(19), 'bumpScale': .6, 'plies': 5, 'clearcoat': .2, 'clearcoatRoughness': .3}),
 # pineapple-leaf nonwoven, PU coated: crinkled, earthy, leather-like textile
 'INN-0242': ('Pinatex', ('src', 'pinatex'), .4, {**SOFT(.5, .008, .45), 'bumpScale': 1.8}),
 # mycelium leather: soft, fine grain, warm brown
 'INN-0202': ('Mylo mushroom leather', ('src', 'mylo-grain'), .35, {**SOFT(.42, .005, .5), 'bumpScale': 1.0, 'sheen': .3, 'sheenColor': '#a08070'}),
 # starch + fibre moulded packaging: smooth beige with fine fibre specks, thin moulded wall
 'INN-0233': ('PaperFoam', ('flecks', {'base': [222, 208, 178], 'n': 4000, 'size': .0028, 'fibre': 4, 'rough': .75, 'mottle': .08,
              'colors': [[180, 150, 110, 3], [240, 230, 205, 2], [150, 120, 85, 1]]}), .75, {**RIGID(4), 'bumpScale': 1.2}),
 # wood-particle filled bio-composite packaging: smooth, satin, speckled with wood bits
 'INN-0286': ('Sulapac', ('flecks', {'base': [218, 202, 172], 'n': 3500, 'size': .0045, 'fibre': 1, 'rough': .35, 'mottle': .05,
              'colors': [[130, 92, 54, 4], [96, 66, 38, 3], [175, 138, 92, 2]]}), .75, {**RIGID(3), 'bumpScale': .4, 'clearcoat': .4, 'clearcoatRoughness': .2}),
 # mycelium-bound agricultural waste: white fuzzy skin with hemp hurd chips showing
 'INN-0200': ('Ecovative MycoComposite', ('flecks', {'base': [236, 232, 222], 'n': 900, 'size': .014, 'fibre': 1.3, 'rough': 1, 'mottle': .12,
              'colors': [[196, 172, 130, 4], [170, 140, 100, 2], [215, 200, 170, 3]]}), .75, {**RIGID(30), 'bumpScale': 3, 'sheen': .8, 'sheenColor': '#ffffff'}),
 # seaweed packaging film: thin, translucent, faintly amber-green, very soft
 'INN-0216': ('Notpla seaweed film', None, .75, {**SOFT(.03, None, 1), 'noMap': True, 'opacity': .45, 'roughness': .2, 'color': '#c8c08a', 'clearcoat': .6}),
 # hemp / hemp-cotton woven fabric: natural, slubby weave, soft drape
 'INN-0031': ('Bear Fiber hemp textile', ('src', 'hemp-weave'), .3, {**SOFT(.12, None, .8), 'bumpScale': 2, 'sheen': .3, 'sheenColor': '#e6dcc4'}),
}

if __name__ == '__main__':
    codes = sys.argv[1:] or list(INN)
    for b, (tex, po) in BASES.items():
        if not os.path.exists(f'src/{b}/Color.jpg'):
            ensure(tex); run('python3', '-I', 'prep.py', f'{C}/{tex}.png', f'{N}/{tex}.png', f'src/{b}', json.dumps({**po, 'size': 1024}))
    jobs = []
    for code in codes:
        label, g, tiles, params = INN[code]; slug = f'inn-{code}'
        if g is None: os.makedirs(f'src/{slug}', exist_ok=True)
        elif g[0] == 'src': slug = g[1]
        else: run('python3', '-I', 'gen_inn.py', g[0], slug, json.dumps(g[1]))
        jobs.append({'slug': slug, 'out': f'inn-{code}', 'params': {**params, 'tiles': tiles}})
    for i in range(0, len(jobs), 8):
        print(run('node', 'runsw.js', json.dumps(jobs[i:i + 8])).count('rendered'), 'rendered', flush=True)
    for code in codes:
        run('python3', '-I', 'compose.py', f'outsw/inn-{code}.png', f'comp/inn-{code}.jpg', '640')
    print('done', len(codes))
