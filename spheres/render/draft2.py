"""Second batch of draft spheres (30 Oct): everything the first batch didn't cover.
usage: python3 draft2.py [key ...]   (no keys = all). Needs the http server on :8765 (README).
Each job: key -> (source, tiles, prep options, render params, extra)
  source 'tex:<name>'  ambientCG scan (colour + normal from PatrickJnr/cc0-texture-pack, decoded
                      to /home/claude/dl/candpng and nrmpng; fetched if missing)
  source 'gen:<kind>' procedural (gen.py), 'split:<key>' metal split of an existing bake,
  'none' (no maps).
  extra: glass=True -> rendered with the in-scene backdrop and merged (glass_merge.py).
"""
import sys, os, json, subprocess
DL = '/home/claude/dl'; C, N = f'{DL}/candpng', f'{DL}/nrmpng'
PACK = 'https://raw.githubusercontent.com/PatrickJnr/cc0-texture-pack/4e163649e258c323da822a52263bc48c5a3f4a9c/'
VRF = '/home/claude/vrf/Source2Viewer-CLI'
SPLIT = {'metalness': 1, 'bumpScale': 0.15, 'env': 'soft', 'rotY': 0, 'rotX': 0}
CLEAR = {'roughness': 0.0, 'ior': 1.5, 'env': 'studio', 'envIntensity': 1.6, 'shadowOpacity': 0.07, 'contactOpacity': 0.4, 'thickness': 6, 'transmission': 1}
WOOD = {'bumpScale': 1.0, 'clearcoat': 0.12, 'clearcoatRoughness': 0.5}
W = lambda t, sat=1, tint=None, tiles=0.22: (f'tex:{t}', tiles, {'rough': 0.65, 'rough_var': 0.2, 'sat': sat, **({'tint': tint} if tint else {})}, WOOD, {})
J = {
 # --- solid woods
 'ash': W('wood022', .9), 'balsa': W('wood021'), 'beech': W('wood056', .85), 'birch': W('wood001'),
 'chestnut': W('wood003'), 'elm': W('wood026'), 'cherry': W('wood005'), 'maple': W('wood002'),
 'poplar': W('wood061'), 'sycamore': W('wood068', .8), 'teak': W('wood063'), 'walnut': W('wood066'),
 'wenge': W('wood051'), 'cedar': W('wood015', .85),
 # --- stone
 'marble': ('tex:marble019', .25, {'rough': .18, 'rough_var': .05}, {'bumpScale': .2, 'clearcoat': .6, 'clearcoatRoughness': .1}, {}),
 'granite': ('tex:rock030', .4, {'rough': .35, 'rough_var': .1}, {'bumpScale': .3, 'clearcoat': .5, 'clearcoatRoughness': .15}, {}),
 'gabbro': ('tex:rock035', .4, {'rough': .3, 'rough_var': .1}, {'bumpScale': .3, 'clearcoat': .5, 'clearcoatRoughness': .15}, {}),
 'basalt': ('tex:rock002', .35, {'rough': .85, 'rough_var': .1}, {'bumpScale': 1.2}, {}),
 'slate': ('tex:rock022', .3, {'rough': .8, 'rough_var': .15}, {'bumpScale': 1.5}, {}),
 'sandstone': ('tex:rock004', .35, {'rough': .95, 'rough_var': .05, 'hue_to': [204, 178, 134]}, {'bumpScale': 1.5}, {}),
 'limestone': ('tex:marble015', .25, {'rough': .8, 'rough_var': .1}, {'bumpScale': .8}, {}),
 'quartz': ('tex:marble021', .25, {'rough': .2, 'rough_var': .05}, {'bumpScale': .2, 'clearcoat': .6, 'clearcoatRoughness': .1}, {}),
 'gypsum': ('tex:plaster002', .3, {'rough': .95, 'rough_var': .05, 'bright': 1.04}, {'bumpScale': 1.0}, {}),
 'lime': ('tex:plaster003', .3, {'rough': .95, 'rough_var': .05, 'tint': [1.02, 1, .96]}, {'bumpScale': 1.2}, {}),
 'clay': ('tex:clay002', .3, {'rough': .9, 'rough_var': .1}, {'bumpScale': 1.0}, {}),
 'brick': ('tex:clay003', .3, {'rough': .95, 'rough_var': .1, 'sat': .85}, {'bumpScale': 1.6}, {}),
 'polymer-concrete': ('tex:terrazzo004', .5, {'rough': .4, 'rough_var': .1}, {'bumpScale': .3, 'clearcoat': .4, 'clearcoatRoughness': .2}, {}),
 'solid-surface': ('tex:terrazzo001', .6, {'rough': .3, 'rough_var': .05}, {'bumpScale': .1, 'clearcoat': .5, 'clearcoatRoughness': .15}, {}),
 # --- ceramics
 'porcelain': ('tex:porcelain001', .3, {'rough': .05, 'rough_var': .02}, {'bumpScale': .05, 'clearcoat': 1, 'clearcoatRoughness': .03}, {}),
 'tech-ceramic': ('gen:plain', 0, {'rough': .45, 'freq': 120, 'amp': .3}, {'color': '#ece6da', 'bumpScale': .2}, {}),
 'glass-ceramic': ('gen:plain', 0, {'rough': .04, 'freq': 80, 'amp': .05}, {'color': '#141416', 'bumpScale': .02, 'clearcoat': 1, 'clearcoatRoughness': .02, 'env': 'soft'}, {}),
 'diamond': ('none', 0, {}, {**CLEAR, 'ior': 2.42, 'attenuationColor': '#f4f6f8', 'attenuationDistance': 30}, {'glass': True}),
 # --- paper, boards
 'paper': ('tex:paper004', .4, {'rough': .9, 'rough_var': .05}, {'bumpScale': .8}, {}),
 'moulded-pulp': ('tex:cardboard004', .4, {'rough': 1, 'rough_var': .05, 'hue_to': [170, 162, 150]}, {'bumpScale': 2.5}, {'pulp': True}),
 'chipboard': ('tex:chipboard001', .35, {'rough': .85, 'rough_var': .1}, {'bumpScale': 1.2}, {}),
 'wood-fibre-board': ('tex:fabric043', .8, {'rough': 1, 'rough_var': .05, 'hue_to': [128, 96, 66]}, {'bumpScale': 1.2, 'sheen': .6, 'sheenColor': '#a08060'}, {}),
 'hemp-board': ('tex:fabric043', .8, {'rough': 1, 'rough_var': .05, 'hue_to': [176, 158, 118]}, {'bumpScale': 1.4, 'sheen': .6, 'sheenColor': '#cbbd96'}, {}),
 'coir-board': ('tex:carpet013', .6, {'rough': 1, 'rough_var': .05, 'hue_to': [112, 74, 44]}, {'bumpScale': 2.0}, {}),
 # --- composites
 'carbon-fibre': ('tex:fabric004', 2.4, {'rough': .35, 'rough_var': .3, 'gray': True, 'bright': .9}, {'bumpScale': .6, 'clearcoat': .8, 'clearcoatRoughness': .08}, {}),
 'glass-fibre': ('tex:fabric011', 2.2, {'rough': .3, 'rough_var': .1, 'hue_to': [196, 204, 186]}, {'bumpScale': .4, 'clearcoat': 1, 'clearcoatRoughness': .05}, {}),
 'basalt-fibre': ('tex:fabric011', 2.2, {'rough': .3, 'rough_var': .1, 'hue_to': [92, 78, 62]}, {'bumpScale': .4, 'clearcoat': 1, 'clearcoatRoughness': .05, 'env': 'soft'}, {}),
 'flax-composite': ('tex:fabric043', .5, {'rough': .3, 'rough_var': .1, 'hue_to': [160, 128, 80]}, {'bumpScale': .3, 'clearcoat': 1, 'clearcoatRoughness': .06}, {}),
 'bamboo-composite': ('tex:wood058', .25, {'rough': .4, 'rough_var': .15, 'tint': [1.05, .98, .8]}, {'bumpScale': .6, 'clearcoat': .7, 'clearcoatRoughness': .1}, {}),
 'fibre-filled-plastic': ('tex:fabric043', 2.0, {'rough': .55, 'rough_var': .05, 'hue_to': [170, 150, 118]}, {'bumpScale': .25}, {}),
 'aramid': ('tex:fabric011', 2.2, {'rough': .35, 'rough_var': .1, 'hue_to': [214, 176, 64]}, {'bumpScale': .5, 'sheen': .5, 'sheenColor': '#f0d070'}, {}),
 # --- felts, piles, knit, weave, yarns
 'glass-wool': ('tex:fabric043', .6, {'rough': 1, 'rough_var': .03, 'hue_to': [214, 184, 96]}, {'bumpScale': 1.6, 'sheen': .8, 'sheenColor': '#f0dc9a'}, {}),
 'basalt-felt': ('tex:fabric043', .8, {'rough': 1, 'rough_var': .03, 'hue_to': [104, 92, 80]}, {'bumpScale': 1.2, 'sheen': .7, 'sheenColor': '#a09080'}, {}),
 'wool-pile': ('tex:carpet013', .7, {'rough': 1, 'rough_var': .03, 'hue_to': [214, 204, 186]}, {'bumpScale': 1.4, 'sheen': 1, 'sheenColor': '#f2ead8', 'sheenRoughness': .5}, {}),
 'fur': ('tex:carpet013', .45, {'rough': 1, 'rough_var': .03, 'hue_to': [120, 98, 80]}, {'bumpScale': 2.4, 'sheen': 1, 'sheenColor': '#c0a890', 'sheenRoughness': .45}, {}),
 'knit': ('tex:fabric019', .5, {'rough': .9, 'rough_var': .05, 'hue_to': [150, 152, 156]}, {'bumpScale': 2.0, 'sheen': .6, 'sheenColor': '#d0d4d8'}, {}),
 'jute': ('tex:fabric027', .6, {'rough': 1, 'rough_var': .05, 'hue_to': [168, 134, 84]}, {'bumpScale': 2.5}, {}),
 'yarn-natural': ('tex:rope001', .9, {'rough': .95, 'rough_var': .05}, {'bumpScale': 2.0}, {}),
 'yarn-coir': ('tex:rope001', .9, {'rough': .95, 'rough_var': .05, 'hue_to': [116, 76, 44]}, {'bumpScale': 2.4}, {}),
 'yarn-light': ('tex:rope001', .9, {'rough': .9, 'rough_var': .05, 'hue_to': [212, 204, 184]}, {'bumpScale': 1.8, 'sheen': .4, 'sheenColor': '#f0e8d8'}, {}),
 'silk': ('tex:rope001', 1.2, {'rough': .35, 'rough_var': .05, 'hue_to': [232, 222, 200]}, {'bumpScale': 1.0, 'sheen': 1, 'sheenColor': '#fff6e6', 'sheenRoughness': .25}, {}),
 'grass-weave': ('tex:wicker005', .5, {'rough': .8, 'rough_var': .1, 'hue_to': [150, 134, 92]}, {'bumpScale': 1.6}, {}),
 # --- leathers
 'suede': ('tex:leather028', .35, {'rough': .95, 'rough_var': .05, 'hue_to': [150, 112, 78]}, {'bumpScale': 1.0, 'sheen': .6, 'sheenColor': '#c09a78'}, {}),
 'exotic-leather': ('tex:leather008', .6, {'rough': .45, 'rough_var': .1, 'hue_to': [90, 70, 52]}, {'bumpScale': 2.0, 'clearcoat': .3, 'clearcoatRoughness': .3}, {}),
 'mycelium-leather': ('tex:leather030', .35, {'rough': .7, 'rough_var': .1, 'hue_to': [122, 100, 84]}, {'bumpScale': 1.2}, {}),
 'pinatex': ('tex:leather003', .4, {'rough': .75, 'rough_var': .15, 'hue_to': [150, 118, 82]}, {'bumpScale': 1.6}, {}),
 # --- bio-composites
 'mycelium': ('tex:fabric043', .35, {'rough': 1, 'rough_var': .03, 'hue_to': [226, 216, 196]}, {'bumpScale': 2.6, 'sheen': 1, 'sheenColor': '#ffffff', 'sheenRoughness': .6}, {}),
 'starch': ('gen:plain', 0, {'rough': .7, 'freq': 90, 'amp': .6, 'mottle': .06}, {'color': '#e2d4b4', 'bumpScale': .4}, {}),
 'lignin': ('gen:plain', 0, {'rough': .45, 'freq': 90, 'amp': .4, 'mottle': .08}, {'color': '#5a3d26', 'bumpScale': .3}, {}),
 'seaweed': ('gen:plain', 0, {'rough': .4, 'freq': 50, 'amp': .5, 'mottle': .1}, {'color': '#c9c08a', 'transmission': .7, 'thickness': 1.5, 'attenuationColor': '#9a8a3c', 'attenuationDistance': 1.2, 'bumpScale': .4}, {}),
 # --- rubbers
 'natural-rubber': ('gen:plain', 0, {'rough': .65, 'freq': 140, 'amp': .3}, {'color': '#8a5a2c', 'bumpScale': .15}, {}),
 'synthetic-rubber': ('gen:plain', 0, {'rough': .75, 'freq': 140, 'amp': .3}, {'color': '#2a2a2b', 'bumpScale': .15}, {}),
 'silicone': ('gen:plain', 0, {'rough': .55, 'freq': 140, 'amp': .2}, {'color': '#a9b6bd', 'bumpScale': .1, 'sheen': .4, 'sheenColor': '#ffffff'}, {}),
 'tpe': ('gen:plain', 0, {'rough': .6, 'freq': 140, 'amp': .2}, {'color': '#4c4f54', 'bumpScale': .1}, {}),
 # --- foams
 'eps': ('gen:beads', 0, {'n': 2600, 'seam': .006, 'rough': .8}, {'color': '#f4f4f1', 'bumpScale': 2.2}, {}),
 'epp': ('gen:beads', 0, {'n': 2600, 'seam': .006, 'rough': .7}, {'color': '#4a4b4d', 'bumpScale': 2.2}, {}),
 'pla-foam': ('gen:beads', 0, {'n': 2200, 'seam': .006, 'rough': .75}, {'color': '#ece8dc', 'bumpScale': 2.2}, {}),
 'starch-foam': ('gen:beads', 0, {'n': 500, 'seam': .015, 'rough': .9, 'var': .15}, {'color': '#e8dcbc', 'bumpScale': 3.0}, {}),
 'tpu-beads': ('gen:beads', 0, {'n': 1400, 'seam': .008, 'rough': .55, 'var': .03}, {'color': '#f2f2f0', 'bumpScale': 2.6}, {}),
 'rigid-pu': ('tex:sponge001', 1.0, {'rough': .9, 'rough_var': .05, 'hue_to': [222, 200, 140]}, {'bumpScale': .8}, {}),
 'pet-foam': ('tex:sponge001', 1.0, {'rough': .9, 'rough_var': .05, 'hue_to': [214, 206, 186]}, {'bumpScale': .8}, {}),
 'aluminium-foam': ('tex:foam002', .5, {'rough': .5, 'rough_var': .2, 'gray': True}, {'metalness': 1, 'bumpScale': 3.5, 'env': 'soft', 'color': '#e8e9ea'}, {}),
 'aerogel': ('none', 0, {}, {**CLEAR, 'roughness': .25, 'ior': 1.05, 'attenuationColor': '#9fc0e8', 'attenuationDistance': 2.5, 'thickness': 3}, {'glass': True}),
 'open-foam-yellow': ('tex:sponge001', .5, {'rough': 1, 'rough_var': .05, 'hue_to': [226, 196, 96]}, {'bumpScale': 3.0}, {}),
 'open-foam-grey': ('tex:sponge001', .7, {'rough': 1, 'rough_var': .05, 'hue_to': [128, 130, 132]}, {'bumpScale': 2.0}, {}),
 'latex-foam': ('tex:sponge001', .6, {'rough': .9, 'rough_var': .05, 'hue_to': [232, 222, 196]}, {'bumpScale': 2.0}, {}),
 'neoprene': ('gen:cells', 0, {'n': 6000, 'seam': .002, 'rough': .8}, {'color': '#262627', 'bumpScale': .5}, {}),
 # --- films, translucent
 'film': ('gen:crumple', 0, {'rough': .05}, {**CLEAR, 'thickness': .3, 'ior': 1.45, 'bumpScale': 4.0, 'attenuationColor': '#f6f8f8', 'attenuationDistance': 20}, {'glass': True}),
 'translucent': ('gen:plain', 0, {'rough': .45, 'freq': 120, 'amp': .2}, {**CLEAR, 'roughness': .45, 'thickness': 2, 'bumpScale': .1, 'attenuationColor': '#e9ecee', 'attenuationDistance': 3}, {'glass': True}),
 # --- other metals
 'platinum': ('split:aluminium', 0, {}, {**SPLIT, 'color': '#e9e6e1'}, {}),
 'tin': ('split:aluminium', 0, {}, {**SPLIT, 'color': '#d3d3cf'}, {}),
 'silicon': ('split:stainless', 0, {}, {**SPLIT, 'color': '#7c8594'}, {}),
}

def run(*a):
    r = subprocess.run(a, capture_output=True, text=True)
    if r.returncode: print(r.stdout[-400:], r.stderr[-800:]); raise SystemExit(f'failed: {a[:3]}')
    return r.stdout

def ensure(tex):
    for kind, d in (('color', C), ('normal', N)):
        png = f'{d}/{tex}.png'
        if os.path.exists(png): continue
        path = next(l.strip() for l in open(f'{DL}/../tex/patrick.txt') if l.startswith('textures/') and f'/{tex}_{kind}_' in l)
        os.makedirs(f'/tmp/vt/{kind}', exist_ok=True); vt = f'/tmp/vt/{kind}/{tex}.vtex_c'
        run('curl', '-sSL', '-o', vt, PACK + path); run(VRF, '-i', vt, '-d', '-o', png)
        if not os.path.exists(png): raise SystemExit(f'decode failed {tex} {kind}')

if __name__ == '__main__':
    keys = sys.argv[1:] or list(J)
    jobs, glass = [], []
    for k in keys:
        src, tiles, po, params, ex = J[k]
        if os.environ.get('SKIP_BAKED') and os.path.exists(f'baked/{k}/color.jpg') and not src.startswith(('none', 'split')):
            pass
        elif src.startswith('tex:'):
            t = src[4:]; ensure(t)
            run('python3', '-I', 'prep.py', f'{C}/{t}.png', f'{N}/{t}.png', f'src/{k}', json.dumps(po))
            run('python3', '-I', 'bake.py', f'src/{k}', f'baked/{k}', str(tiles))
        elif src.startswith('gen:'):
            run('python3', '-I', 'gen.py', src[4:], k, json.dumps(po))
        elif src.startswith('split:'):
            os.makedirs(f'baked/{k}', exist_ok=True); run('cp', '-r', f'baked/{src[6:]}-split/.', f'baked/{k}/')
        else:
            os.makedirs(f'baked/{k}', exist_ok=True)
        if ex.get('glass'):
            glass.append(k); jobs.append({'slug': k, 'params': {**params, 'backdrop': True}})
            os.makedirs(f'baked/{k}-mask', exist_ok=True)
            for f in os.listdir(f'baked/{k}'): run('cp', f'baked/{k}/{f}', f'baked/{k}-mask/{f}')
            jobs.append({'slug': k + '-mask', 'params': {**params, 'transmission': 0}})
        else:
            jobs.append({'slug': k, 'params': params})
        print('prepared', k, flush=True)
    for i in range(0, len(jobs), 12):
        print(run('node', 'run2.js', json.dumps(jobs[i:i + 12])).count('rendered'), 'rendered', flush=True)
    os.makedirs('comp', exist_ok=True)
    for k in keys:
        src = f'out2/{k}.png'
        if k in glass:
            run('python3', '-I', 'glass_merge.py', k); src = f'out2/{k}-final.png'
        run('python3', '-I', 'compose.py', src, f'comp/{k}.jpg', '640')
    print('done', len(keys))
