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
 'pulp-grey': ('fabric043', {'rough': 1, 'rough_var': .05, 'hue_to': [204, 204, 200]}),
 'myco-midgrey': ('plaster002', {'rough': .9, 'rough_var': .05, 'hue_to': [138, 138, 135]}),
 'bamboo-honey': ('wood017', {'rough': .6, 'rough_var': .15, 'hue_to': [212, 172, 112]}),
 'hemp-streaks': ('wood022', {'rough': .55, 'rough_var': .2, 'hue_to': [186, 166, 134]}),
 'glass-marble': ('marble012', {'rough': .04, 'rough_var': .02, 'hue_to': [38, 104, 108]}),
 'felt-darkgrey': ('fabric034', {'rough': 1, 'rough_var': .03, 'hue_to': [84, 85, 88]}),
 'pina-gold': ('fabric043', {'rough': .35, 'rough_var': .15, 'hue_to': [200, 160, 70]}),
 'mylo-camel': ('leather028', {'rough': .85, 'rough_var': .05, 'hue_to': [196, 152, 98]}),
 'paper-white': ('paper003', {'rough': .55, 'rough_var': .05, 'hue_to': [226, 222, 212]}),
 'roving-cream': ('carpet013', {'rough': 1, 'rough_var': .03, 'hue_to': [232, 222, 198]}),
 'myco-white': ('sponge001', {'rough': 1, 'rough_var': .05, 'hue_to': [240, 236, 224]}),
}
RIGID = lambda mm: {'stiff': 1, 'thickMM': mm}
SOFT = lambda st, shape=None, sag=None: {'stiff': st, **({'shape': shape} if shape is not None else {}), **({'sag': sag} if sag is not None else {})}

# code: (label, generator or src, generator opts, tiles, render params)
INN = {
 # light grey moulded pulp acoustic panel, fine dense chevron relief
 'INN-0028': ('Baux acoustic pulp', ('relief', {'base': 'pulp-grey', 'pattern': 'chevron', 'rows': 5, 'lines': 2, 'amp': 1.2, 'depth': .9, 'ao': .22}), 1.5,
              {**RIGID(25), 'bumpScale': 5, 'roughness': 1}),
 # mid-grey mycelium tile, fine smooth-topped diagonal ribs
 'INN-0195': ('Mogu mycelium acoustic panels', ('relief', {'base': 'myco-midgrey', 'pattern': 'ribs', 'rows': 1, 'lines': 7, 'depth': .9, 'ao': .25}), .75,
              {**RIGID(30), 'bumpScale': 7}),
 # recycled textile nonwoven board: dark grey heathered felt
 'INN-0172': ('Kvadrat Really recycled textiles', ('src', 'felt-darkgrey'), 1.0, {**RIGID(12), 'bumpScale': .6, 'sheen': .5, 'sheenColor': '#9a9aa0'}),
 # recycled glass-ceramic: glossy, coloured glass with molten marbling
 'INN-0182': ('Magna Glaskeramik', ('src', 'glass-marble'), .35, {**RIGID(20), 'bumpScale': .05, 'clearcoat': 1, 'clearcoatRoughness': .03, 'env': 'soft'}),
 # recycled HIPS: light grey with grey flecks and a few coarse chips, matte
 'INN-0274': ('Smile Plastics Heron', ('flecks', {'base': [222, 222, 220], 'n': 3200, 'size': .005, 'fibre': 1, 'rough': .6,
              'colors': [[120, 120, 122, 4], [160, 160, 160, 3], [70, 70, 72, 1], [245, 245, 242, 2]]}), .75, {**RIGID(12), 'bumpScale': .4}),
 # compressed hemp fibre: pale tan, long fibrous streaks
 'INN-0146': ('HempWood', ('src', 'hemp-streaks'), .3, {**RIGID(16), 'bumpScale': 1.2, 'clearcoat': .2, 'clearcoatRoughness': .35}),
 # bamboo panels: edge-grain strips, honey and caramelised tones, nodes
 'INN-0245': ('Plyboo bamboo panels', ('strips', {'base': 'bamboo-honey', 'strips': 9, 'nodes': 1, 'var': .45}), .75,
              {**RIGID(19), 'bumpScale': .6, 'plies': 5, 'clearcoat': .2, 'clearcoatRoughness': .3}),
 # pineapple-leaf nonwoven with metallic gold finish: fibre network, sheen
 'INN-0242': ('Pinatex', ('src', 'pina-gold'), .5, {**SOFT(.5, .008, .45), 'bumpScale': 1.4, 'metalness': .55, 'env': 'soft'}),
 # mycelium leather: smooth camel, suede-like, soft drape
 'INN-0202': ('Mylo mushroom leather', ('src', 'mylo-camel'), .5, {**SOFT(.35, .004, .6), 'bumpScale': .35, 'sheen': .8, 'sheenColor': '#e0b888', 'sheenRoughness': .6}),
 # starch + fibre moulded packaging: warm beige, grainy matte
 'INN-0233': ('PaperFoam', ('flecks', {'base': [206, 186, 152], 'n': 7000, 'size': .0028, 'fibre': 1.5, 'rough': .85, 'mottle': .1,
              'colors': [[176, 150, 112, 4], [226, 210, 180, 3], [150, 124, 90, 1]]}), .75, {**RIGID(4), 'bumpScale': 1.6}),
 # bio-composite packaging: black with light speckles, satin
 'INN-0286': ('Sulapac', ('flecks', {'base': [28, 28, 30], 'n': 4500, 'size': .0035, 'fibre': 1, 'rough': .35, 'mottle': .05,
              'colors': [[222, 214, 196, 5], [170, 160, 140, 3], [250, 248, 240, 2]]}), .75, {**RIGID(4), 'bumpScale': .35, 'clearcoat': .5, 'clearcoatRoughness': .2}),
 # mycelium composite: white, porous, rough
 'INN-0200': ('Ecovative MycoComposite', ('src', 'myco-white'), .6, {**RIGID(30), 'bumpScale': 3.5, 'sheen': .8, 'sheenColor': '#ffffff'}),
 # seaweed-coated paperboard packaging: white, satin, semi-stiff
 'INN-0216': ('Notpla seaweed coating', ('src', 'paper-white'), .5, {**SOFT(.6, .015, .35), 'bumpScale': .8, 'rotY': -.6, 'clearcoat': .4, 'clearcoatRoughness': .3}),
 # hemp fibre / tow: thick cream roving, very soft
 'INN-0031': ('Bear Fiber hemp fibre', ('src', 'roving-cream'), .35, {**SOFT(.1, None, .85), 'bumpScale': 2.6, 'sheen': .6, 'sheenColor': '#fff6e4', 'sheenRoughness': .6}),
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
