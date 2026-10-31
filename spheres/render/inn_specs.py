"""Swatch specs for the Spotlight innovations (see inn_all.py). code: (general look, rgb, options).
Colour and look from each innovation's description, tags and a glance at its photo (colour only)."""
FL = lambda base, cols, n=2500, size=.004, fibre=1.0, rough=.7, mottle=.05: ('flecks', {'base': base, 'colors': cols, 'n': n, 'size': size, 'fibre': fibre, 'rough': rough, 'mottle': mottle})
GLOSS = {'clearcoat': 1, 'clearcoatRoughness': .05}
SATIN = {'clearcoat': .5, 'clearcoatRoughness': .25}

SPEC = {
 'INN-0001': ('softwood', (200, 180, 148), {}),                                   # acetylated wood, pale
 'INN-0002': ('neoprene', (236, 236, 230), {}),                                   # seaweed foam, white
 'INN-0003': ('knit', (232, 172, 150), {}),                                       # recycled crop fibre knit
 'INN-0004': ('fibre-filled-plastic', (72, 122, 128), {}),                        # PP + plant fibre composite
 'INN-0005': ('plastic', (234, 232, 224), {}),                                    # PHB, natural white
 'INN-0006': ('woven-synthetic', (232, 190, 40), {}),                             # transfer-printed polyester
 'INN-0007': ('mycelium', (232, 216, 192), {'soft': (.6, .02, .3)}),              # mycelium foam sheet
 'INN-0008': ('plastic', (32, 72, 200), {}),                                      # bio-PA
 'INN-0009': ('seaweed', (95, 75, 52), {'mm': 3}),                                # seaweed bioplastic
 'INN-0010': ('cork', (72, 52, 38), {'mm': 30, 'contrast': 1.3}),                 # expanded black cork
 'INN-0011': ('lime', (40, 150, 136), {'mm': 10, 'rgb2': (95, 192, 172), 'mottle': .7, 'p': GLOSS}),   # stucco lustro
 'INN-0012': ('tpe', (32, 32, 34), {}),                                           # bio-TPU
 'INN-0013': ('leather', (180, 112, 62), {}),                                     # apple-waste leather alternative
 'INN-0014': ('lignin', (165, 125, 82), {}),                                      # liquid wood
 'INN-0015': ('moulded-pulp', (192, 152, 104), {'contrast': 1.5, 'rgb2': (150, 110, 70), 'mottle': .6}),   # pressed palm leaf
 'INN-0016': ('tpe', (24, 178, 178), {}),                                         # bio-TPC elastomer
 'INN-0017': ('film', (240, 150, 190), {}),                                       # cassava starch film
 'INN-0018': ('clear-glass', (238, 244, 246), {'mm': 3}),                         # PEF, clear
 'INN-0019': ('leather', (132, 132, 112), {}),                                    # bacterial cellulose
 'INN-0020': ('tpe', (176, 166, 156), {}),                                        # bio-TPE
 'INN-0021': ('moulded-pulp', (226, 206, 166), {}),                               # banana fibre pulp
 'INN-0022': ('paper', None, {'g': FL([238, 228, 205], [[170, 130, 90, 3], [200, 170, 130, 2]], 900, .004, 3, .9)}),   # banana paper
 'INN-0023': ('woven-natural', (214, 122, 96), {}),                               # banana fibre textile
 'INN-0024': ('woven-natural', (238, 232, 215), {}),                              # abaca fabric, natural white
 'INN-0025': ('leather', (190, 122, 42), {'contrast': 1.2}),                      # banana fibre leather
 'INN-0026': ('paper', None, {'g': FL([205, 105, 45], [[230, 150, 80, 3], [150, 60, 20, 2]], 2500, .003, 5, .9), 'soft': (.4, .006, .5)}),   # barkcloth
 'INN-0027': ('eps', (240, 240, 238), {}),                                        # recycled EPS
 'INN-0029': ('hemp-board', (130, 175, 170), {'mm': 25}),                         # wood wool cement, tinted
 'INN-0030': ('flax-composite', (150, 110, 60), {'p': GLOSS}),                    # flax composite
 'INN-0032': ('film', (240, 232, 170), {}),                                       # PLA film
 'INN-0033': ('glass-ceramic', (232, 238, 238), {'rgb2': (120, 196, 228), 'mottle': .6, 'p': GLOSS, 'mm': 20}),   # recycled glass
 'INN-0034': ('concrete', (86, 86, 86), {'contrast': 1.4, 'mm': 20}),             # biocement tile
 'INN-0035': ('hemp-board', (200, 190, 165), {'mm': 30}),                         # hempcrete block
 'INN-0036': ('pla-foam', (200, 234, 210), {}),                                   # expanded PLA
 'INN-0037': ('film', (250, 250, 250), {}),                                       # PHA film
 'INN-0038': ('concrete', (178, 178, 172), {}),                                   # biocement
 'INN-0039': ('concrete', (170, 170, 166), {}),
 'INN-0040': ('plastic', (240, 240, 236), {}),                                    # PBS
 'INN-0041': ('pet-felt', (150, 214, 190), {'soft': (.6, .015, .3)}),             # bulrush fill
 'INN-0042': ('plastic', (150, 76, 46), {}),                                      # olive-stone bioplastic
}

SPEC.update({
 'INN-0043': ('silk', (222, 214, 178), {}),                                       # bio-recycled polyester fabric
 'INN-0044': ('moulded-pulp', (170, 118, 78), {'contrast': 1.5, 'mm': 4}),        # pressed wheat bran
 'INN-0045': ('woven-synthetic', (48, 92, 150), {}),                              # viscose / lyocell fabric
 'INN-0046': ('cork', (62, 46, 34), {'mm': 30, 'contrast': 1.2}),                 # black cork board
 'INN-0047': ('pet-felt', (60, 60, 62), {}),                                      # recycled textile fibre
 'INN-0048': ('copper', (232, 160, 120), {}),                                     # recycled copper
 'INN-0049': ('fur', (190, 190, 180), {'rgb2': (110, 110, 105), 'mottle': .7}),   # protein faux fur
 'INN-0050': ('knit', (30, 44, 82), {}),                                          # protein fibre knit
 'INN-0051': ('ash', (100, 64, 38), {'contrast': 1.2}),                           # thermally modified ash
 'INN-0052': ('wool-felt', (226, 206, 160), {'soft': (.7, .02, .25)}),            # camel hair insulation
 'INN-0053': ('film', (120, 220, 120), {}),                                       # starch film
 'INN-0054': ('leather', (176, 160, 40), {'rgb2': (110, 100, 30), 'mottle': .6}), # bacterial cellulose leather
 'INN-0055': ('glass-wool', (176, 172, 166), {}),                                 # cellulose insulation
 'INN-0056': ('paper', (246, 246, 244), {}),                                      # MFC coating
 'INN-0058': ('woven-synthetic', (176, 104, 82), {}),                             # recycled lyocell
 'INN-0059': ('knit', (90, 140, 220), {}),                                        # recycled polyester knit
 'INN-0060': ('silk', (40, 54, 120), {}),                                         # Circulose fabric
 'INN-0061': ('brick', (186, 122, 112), {}),                                      # clay brick
 'INN-0062': ('coir-board', (196, 150, 90), {'mm': 22}),                          # clay + reed board
 'INN-0063': ('clay', (150, 112, 76), {'mm': 15}),                                # clay plaster
 'INN-0064': ('coir-board', (120, 90, 64), {'mm': 25}),                           # coir + latex moulding
 'INN-0065': ('coir-board', (88, 70, 54), {'mm': 25}),                            # coir + latex sheet
 'INN-0066': ('woven-natural', (150, 96, 170), {}),                               # bacterial dye
 'INN-0067': ('paper', (200, 156, 112), {'p': SATIN}),                            # wax paper
 'INN-0068': ('moulded-pulp', (192, 182, 166), {}),                               # wheat straw pulp
 'INN-0069': ('sandstone', (216, 150, 70), {'mm': 15}),                           # corn waste tile
 'INN-0070': ('yarn-light', (236, 226, 204), {}),                                 # softened hemp / flax
 'INN-0071': ('plywood', (232, 206, 164), {'mm': 30, 'p': {'plies': 5}}),         # CLT
 'INN-0072': ('paper', (70, 82, 108), {}),                                        # crush paper
 'INN-0073': ('knit', (226, 196, 182), {}),                                       # recycled polyester
 'INN-0074': ('lime', (130, 140, 160), {'contrast': 1.6, 'mm': 10}),              # denim stucco
 'INN-0075': ('moulded-pulp', (236, 232, 222), {}),                               # dry moulded fibre
 'INN-0076': ('paper', (200, 172, 124), {'g': ('relief', {'base': 'paper', 'pattern': 'ribs', 'rows': 1, 'lines': 9, 'depth': .9, 'ao': .35}), 'mm': 25}),   # honeycomb
 'INN-0077': ('solid-surface', None, {'g': FL([228, 226, 220], [[160, 110, 80, 3], [60, 60, 62, 3], [200, 170, 120, 2], [120, 120, 118, 2]], 1400, .012, 1, .4)}),   # terrazzo
 'INN-0078': ('woven-synthetic', (30, 168, 176), {}),                             # CO2-dyed polyester
 'INN-0079': ('knit', (150, 82, 70), {}),                                         # agri-waste dye
 'INN-0080': ('paper', (244, 242, 236), {'p': SATIN}),                            # paper film
 'INN-0081': ('translucent', (220, 170, 230), {}),                                # cellulose bioplastic
 'INN-0082': ('wood-fibre-board', (214, 196, 150), {'mm': 18}),                   # straw panel
 'INN-0083': ('lime', None, {'g': FL([196, 186, 168], [[110, 84, 60, 4], [150, 120, 90, 3], [230, 222, 206, 2]], 6000, .004, 1, .9), 'mm': 15}),   # cork + lime render
})

SPEC.update({
 'INN-0084': ('film', (244, 244, 236), {}),                                       # PBAT film
 'INN-0085': ('paper', (220, 230, 150), {'soft': (.25, None, .7), 'rgb2': (240, 244, 200), 'mottle': .7}),   # bacterial cellulose coating
 'INN-0086': ('porcelain', (196, 200, 204), {'p': SATIN}),                        # recycled stoneware
 'INN-0087': ('woven-synthetic', (20, 140, 200), {}),                             # recycled nylon
 'INN-0088': ('plastic', (226, 226, 220), {}),                                    # bio-PA410
 'INN-0089': ('fur', (210, 142, 116), {}),                                        # plant-based faux fur
 'INN-0090': ('fur', (230, 220, 200), {'rgb2': (40, 36, 34), 'mottle': 1, 'mfreq': 4, 'mpow': 4}),   # faux fur, two-tone
 'INN-0091': ('film', (240, 244, 236), {}),                                       # starch bag film
 'INN-0092': ('film', (60, 60, 60), {'p': {'opacity': .75}}),                     # compostable film, dark
 'INN-0093': ('pla-foam', (210, 200, 182), {}),                                   # compostable foam
 'INN-0094': ('oak', (200, 160, 118), {'mm': 8}),                                 # bio-PUR flooring
 'INN-0095': ('coir-board', (110, 96, 80), {'mm': 30}),                           # eelgrass panel
 'INN-0096': ('walnut', None, {'soft': (.55, .01, .4), 'p': SATIN}),              # flax composite veneer
 'INN-0097': ('glass-wool', (160, 160, 158), {}),                                 # newsprint insulation
 'INN-0098': ('woven-synthetic', (150, 136, 140), {}),                            # enzymatic recycled nylon
 'INN-0099': ('mycelium-leather', (44, 44, 46), {'contrast': 1.3}),               # mycelium leather, black
 'INN-0100': ('tpe', (232, 240, 246), {'p': SATIN}),                              # bio-TPU
 'INN-0101': ('chipboard', (200, 182, 150), {'contrast': .5}),                    # MDF
 'INN-0102': ('woven-synthetic', (236, 96, 30), {}),                              # bio-PA66 yarn
 'INN-0103': ('open-foam-yellow', (240, 190, 40), {}),                            # bio-PUR foam
 'INN-0104': ('film', (90, 170, 90), {'p': {'opacity': .55}}),                    # seaweed film
 'INN-0105': ('paper', (236, 200, 190), {'soft': (.8, .03, .15)}),                # coffee cup paper (board)
 'INN-0106': ('solid-surface', None, {'g': FL([70, 84, 104], [[220, 222, 226, 4], [140, 160, 184, 3], [30, 34, 40, 2]], 6000, .006, 1, .8)}),   # textile waste tile
 'INN-0107': ('clay', (110, 70, 50), {'mm': 10}),                                 # food waste material
 'INN-0108': ('woven-synthetic', (50, 90, 150), {}),                              # rPET yarn
 'INN-0109': ('woven-natural', (190, 190, 176), {}),                              # textile waste dye
 'INN-0110': ('chipboard', (214, 186, 140), {'contrast': .5}),                    # recycled MDF
 'INN-0111': ('fibre-filled-plastic', (186, 136, 80), {}),                        # wood fibre filler
 'INN-0112': ('paper', (240, 240, 236), {'soft': (.8, .03, .15)}),                # formable paper
 'INN-0113': ('yarn-light', (246, 246, 244), {}),                                 # cellulose fibre
 'INN-0114': ('paper', (210, 196, 172), {'g': ('relief', {'base': 'paper', 'pattern': 'chevron', 'rows': 6, 'lines': 3, 'amp': 1, 'depth': .9, 'ao': .4}), 'soft': (.4, .01, .5)}),   # paper mesh
 'INN-0115': ('starch-foam', (240, 238, 230), {}),                                # starch loose fill
 'INN-0116': ('woven-natural', (200, 150, 90), {}),                               # food-waste dye
 'INN-0117': ('suede', (20, 150, 200), {}),                                       # mycelium leather/foam
 'INN-0118': ('solid-surface', None, {'g': FL([234, 230, 222], [[150, 100, 66, 4], [200, 160, 120, 3], [40, 70, 110, 1], [90, 60, 40, 2]], 1100, .014, 1, .45)}),   # timber terrazzo
 'INN-0119': ('film', (246, 246, 246), {'p': {'opacity': .6}}),                   # wood-based PP label film
 'INN-0120': ('yarn-natural', (196, 140, 84), {}),                                # naturally coloured cotton
 'INN-0121': ('leather', (220, 180, 40), {}),                                     # mango leather
 'INN-0122': ('chipboard', (168, 128, 88), {'contrast': .4, 'mm': 6}),            # hardboard
 'INN-0123': ('yarn-light', (248, 248, 246), {}),                                 # lab-grown cotton
})

SPEC.update({
 'INN-0124': ('paper', (214, 168, 110), {'g': ('relief', {'base': 'paper', 'pattern': 'chevron', 'rows': 7, 'lines': 3, 'amp': 1, 'depth': .9, 'ao': .4}), 'soft': (.35, .008, .55)}),   # honeycomb wrap
 'INN-0125': ('paper', (200, 170, 126), {'soft': (.75, .03, .2)}),                # kraft + PLA pouch
 'INN-0126': ('softwood', (236, 218, 186), {'mm': 30}),                           # glulam
 'INN-0127': ('paper', None, {'g': FL([214, 160, 50], [[120, 80, 40, 3], [90, 60, 30, 2]], 1500, .002, 2, .85), 'soft': (.8, .03, .15)}),   # beer paper
 'INN-0128': ('paper', (210, 204, 110), {'soft': (.8, .03, .15)}),                # bio cycle paper
 'INN-0129': ('paper', (244, 242, 236), {'soft': (.75, .03, .2)}),                # cotton paper
 'INN-0130': ('wool-pile', (240, 238, 232), {}),                                  # cotton terry
 'INN-0131': ('wood-fibre-board', (176, 164, 120), {'mm': 40}),                   # grass insulation
 'INN-0132': ('leather', (238, 236, 232), {}),                                    # grape leather, white
 'INN-0133': ('paper', (218, 204, 160), {'soft': (.85, .035, .1), 'g': FL([222, 208, 168], [[120, 140, 70, 3], [170, 150, 100, 2]], 1800, .003, 3, .85)}),   # grass paper
 'INN-0134': ('paper', None, {'g': ('relief', {'base': 'hemp-streaks', 'hue_to': [196, 178, 150], 'pattern': 'waves', 'rows': 1, 'lines': 60, 'depth': .3, 'ao': .1}), 'soft': (.5, .01, .45)}),   # banana trunk veneer
 'INN-0135': ('translucent', (230, 70, 160), {}),                                 # recycled acrylic
 'INN-0136': ('starch-foam', (246, 246, 244), {'mm': 30}),                        # starch foam
 'INN-0137': ('woven-natural', (226, 220, 200), {}),                              # banana fibre
 'INN-0138': ('wood-fibre-board', (214, 172, 110), {'mm': 40}),                   # wood fibre insulation
 'INN-0139': ('wool-felt', (210, 204, 190), {'soft': (.7, .02, .25)}),            # sheep wool insulation
 'INN-0140': ('woven-synthetic', (24, 70, 160), {}),                              # regenerated cellulose
 'INN-0141': ('plastic', (84, 62, 50), {'mm': 6, 'g': ('relief', {'base': 'fibre-filled-plastic', 'hue_to': [84, 62, 50], 'pattern': 'waves', 'rows': 1, 'lines': 3, 'depth': .95, 'ao': .25})}),   # corrugated hemp sheet
 'INN-0142': ('yarn-natural', (214, 200, 170), {}),                               # hemp fibre
 'INN-0144': ('hemp-board', (184, 180, 166), {'mm': 30}),                         # hempcrete
 'INN-0145': ('woven-natural', (232, 160, 30), {}),                               # hemp fabric
 'INN-0147': ('wool-felt', (200, 180, 130), {'soft': (.75, .025, .2)}),           # hemp wool batt
 'INN-0148': ('paper', (196, 150, 96), {'g': ('relief', {'base': 'paper', 'pattern': 'chevron', 'rows': 5, 'lines': 2, 'amp': 1, 'depth': .95, 'ao': .45}), 'mm': 25}),   # paper honeycomb
 'INN-0149': ('yarn-light', (244, 240, 232), {}),                                 # nettle fibre
 'INN-0150': ('wood-fibre-board', (220, 206, 170), {'mm': 15}),                   # recycled paper panel
 'INN-0151': ('chipboard', (200, 168, 120), {'mm': 40}),                          # wood fibre insulation
 'INN-0152': ('woven-natural', (60, 90, 140), {}),                                # microbial indigo denim
 'INN-0153': ('aluminium', None, {}),                                             # recycled aluminium
 'INN-0154': ('aluminium', (220, 222, 224), {}),                                  # low carbon aluminium
 'INN-0155': ('woven-synthetic', (80, 96, 50), {}),                               # digital dyeing
 'INN-0156': ('woven-natural', (200, 180, 190), {}),                              # natural dyes
 'INN-0157': ('silk', (40, 90, 190), {}),                                         # recycled cellulose fibre
 'INN-0158': ('plastic', (244, 244, 240), {}),                                    # PLA
 'INN-0159': ('woven-synthetic', (176, 120, 80), {}),                             # Ioncell textile
 'INN-0160': ('hemp-board', (160, 140, 110), {'mm': 30, 'contrast': 1.3}),        # hemp blocks
 'INN-0161': ('brick', None, {'g': FL([110, 140, 170], [[220, 140, 160, 3], [230, 220, 120, 2], [240, 240, 240, 2]], 4000, .006, 1, .9)}),   # recycled brick
 'INN-0162': ('paper', (240, 236, 226), {'soft': (.7, .025, .25), 'p': SATIN}),   # stone paper
 'INN-0163': ('ash', (226, 210, 180), {'mm': 12}),                                # rattan composite
 'INN-0164': ('lime', (120, 150, 170), {'mm': 6}),                                # mineral paint
 'INN-0165': ('paper', (196, 160, 112), {'soft': (.75, .03, .2), 'p': SATIN}),    # seaweed-coated kraft
})

SPEC.update({
 'INN-0166': ('silk', (234, 214, 170), {}),                                       # seaweed fibre fabric
 'INN-0167': ('silk', (246, 246, 246), {}),                                       # PBS fibre
 'INN-0168': ('glass-wool', (196, 160, 110), {}),                                 # glass wool, bio binder
 'INN-0169': ('suede', (214, 150, 160), {}),                                      # recycled synthetic suede
 'INN-0170': ('woven-natural', (170, 156, 136), {}),                              # hemp fabric
 'INN-0171': ('paper', (176, 132, 88), {'soft': (.7, .025, .25)}),                # kraft paper
 'INN-0173': ('film', (246, 246, 246), {'p': {'opacity': .6}}),                   # milk protein film
 'INN-0174': ('plywood', (232, 210, 170), {'mm': 40, 'p': {'plies': 13}}),        # LVL
 'INN-0175': ('leather', (210, 120, 30), {}),                                     # apple waste leather
 'INN-0176': ('clay', (196, 132, 100), {'mm': 6}),                                # clay paint
 'INN-0177': ('brick', (198, 168, 140), {'contrast': .6}),                        # earth block
 'INN-0178': ('lignin', (120, 74, 40), {}),                                       # lignin
 'INN-0179': ('concrete', (170, 160, 140), {}),                                   # LC3 cement
 'INN-0180': ('plastic', (240, 242, 240), {}),                                    # PLA
 'INN-0181': ('cedar', (150, 104, 66), {}),                                       # thermowood
 'INN-0183': ('mycelium-leather', (150, 70, 60), {'rgb2': (110, 100, 96), 'mottle': .6}),   # coconut leather
 'INN-0184': ('plastic', (232, 222, 196), {}),                                    # PHA
 'INN-0185': ('plastic', (100, 140, 120), {'mm': 3, 'g': FL([100, 140, 120], [[70, 110, 90, 3], [140, 176, 156, 3]], 9000, .004, 3, .6, .15)}),   # linoleum, marbled
 'INN-0186': ('chipboard', (120, 84, 56), {'contrast': .4, 'mm': 4}),             # hardboard
 'INN-0187': ('film', (236, 240, 232), {}),                                       # starch film
 'INN-0188': ('plastic', (40, 40, 42), {}),                                       # recycled plastic, black
 'INN-0189': ('chipboard', (236, 200, 60), {'contrast': .4}),                     # acetylated MDF, painted
 'INN-0190': ('pet-felt', (100, 112, 150), {'mm': 40}),                           # recycled cotton insulation
 'INN-0191': ('silk', (220, 120, 20), {}),                                        # protein silk
 'INN-0192': ('woven-synthetic', (60, 170, 40), {}),                              # algae coatings
 'INN-0193': ('plastic', (230, 210, 170), {}),                                    # PHA
 'INN-0194': ('leather', (120, 84, 50), {}),                                      # plant leather, rubber
 'INN-0196': ('cork', (190, 160, 120), {'mm': 6, 'contrast': .6, 'p': SATIN}),    # mycelium flooring
 'INN-0197': ('slate', (50, 52, 60), {'mm': 8, 'p': GLOSS}),                      # recycled glass mosaic
 'INN-0198': ('suede', (190, 120, 40), {}),                                       # fungus skin
 'INN-0199': ('mycelium', (210, 176, 120), {}),                                   # mycelium composite
 'INN-0201': ('mycelium-leather', (200, 170, 130), {}),                           # mycelium leather
 'INN-0203': ('yarn-light', (246, 246, 246), {}),                                 # biodegradable PET fibre
 'INN-0204': ('wool-pile', (240, 236, 226), {}),                                  # traceable wool
 'INN-0205': ('woven-natural', (160, 146, 170), {}),                              # natural dyed fibre
 'INN-0206': ('wool-felt', (238, 232, 216), {'soft': (.7, .02, .25)}),            # natural padding
 'INN-0207': ('film', (150, 100, 70), {'p': {'opacity': .45}}),                   # cellulose film
 'INN-0208': ('plastic', (220, 190, 150), {}),                                    # bio-based plastics
 'INN-0209': ('pet-felt', (246, 246, 244), {'soft': (.35, .006, .55)}),           # PLA nonwoven
 'INN-0210': ('woven-synthetic', (180, 180, 186), {}),                            # bio-PA610 fibre
})

SPEC.update({
 'INN-0211': ('knit', (214, 170, 60), {}),                                        # pineapple leaf fibre textile
 'INN-0212': ('pet-felt', (226, 218, 198), {'soft': (.45, .008, .5)}),            # flax nonwoven
 'INN-0213': ('pet-felt', (220, 212, 190), {'soft': (.35, .006, .55)}),           # hemp nonwoven
 'INN-0214': ('wool-felt', (70, 72, 70), {'soft': (.2, None, .7)}),               # yak wool fabric
 'INN-0215': ('plastic', (176, 104, 50), {}),                                     # seaweed utensils
 'INN-0217': ('plastic', (232, 216, 184), {'mm': 6}),                             # PLA/PHA plastic
 'INN-0218': ('knit', (238, 236, 230), {}),                                       # recycled cellulose fibre
 'INN-0219': ('silk', (226, 224, 214), {}),                                       # microbial lyocell
 'INN-0220': ('plastic', (180, 214, 230), {}),                                    # bio polyesters
 'INN-0221': ('yarn-light', (244, 244, 244), {}),                                 # bio-PA6 fibre
 'INN-0222': ('silk', (150, 160, 220), {}),                                       # citrus fibre silk
 'INN-0223': ('knit', (200, 180, 140), {}),                                       # naturally coloured cotton
 'INN-0224': ('grass-weave', None, {'g': FL([196, 186, 140], [[140, 150, 70, 4], [220, 200, 150, 3], [200, 80, 90, 1], [110, 90, 60, 2]], 9000, .004, 3, .9), 'mm': 4}),   # hay surface
 'INN-0225': ('fibre-filled-plastic', (214, 204, 182), {}),                       # rice husk filler
 'INN-0226': ('solid-surface', None, {'g': FL([200, 194, 186], [[110, 106, 104, 3], [236, 232, 224, 3], [150, 140, 130, 2]], 5000, .004, 1, .8), 'mm': 20}),   # shell composite
 'INN-0227': ('film', (40, 160, 160), {'p': {'opacity': .6}}),                    # algae bioplastic
 'INN-0228': ('fibre-filled-plastic', (196, 150, 90), {'mm': 6}),                 # green waste panels
 'INN-0229': ('stainless', (200, 202, 206), {}),                                  # recycled steel
 'INN-0230': ('moulded-pulp', (222, 206, 170), {}),                               # paddy straw tray
 'INN-0231': ('knit', (220, 80, 110), {}),                                        # fruit fibre blend
 'INN-0232': ('knit', (44, 44, 44), {}),                                          # plant fibre blend
 'INN-0234': ('fibre-filled-plastic', (80, 56, 40), {'mm': 4, 'p': SATIN}),       # paper laminate
 'INN-0235': ('concrete', (170, 170, 168), {'mm': 15}),                           # recycled paper tile
 'INN-0236': ('paper', (244, 244, 242), {'soft': (.3, .006, .6)}),                # wood fibre packaging
 'INN-0237': ('chipboard', (176, 136, 84), {'mm': 40, 'contrast': 1.3}),          # PSL
 'INN-0238': ('tpe', (30, 30, 36), {}),                                           # bio PEBA
 'INN-0239': ('plastic', (120, 60, 140), {}),                                     # amorphous PHA
 'INN-0240': ('woven-natural', (40, 60, 150), {}),                                # microbial pigment
 'INN-0241': ('clear-glass', (226, 236, 240), {}),                                # low-e glass
 'INN-0243': ('yarn-light', (240, 234, 220), {}),                                 # pineapple yarn
 'INN-0244': ('solid-surface', None, {'g': FL([238, 236, 232], [[220, 60, 60, 2], [40, 120, 200, 2], [240, 190, 40, 2], [40, 40, 44, 2]], 700, .008, 1, .5), 'mm': 12}),   # recycled PS terrazzo
 'INN-0246': ('solid-surface', None, {'g': FL([30, 150, 140], [[230, 230, 228, 3], [20, 90, 90, 3], [240, 120, 90, 1]], 2500, .006, 1, .45), 'mm': 12}),   # recycled PS panel
 'INN-0247': ('plastic', (220, 30, 30), {}),                                      # PLA packaging
 'INN-0248': ('plastic', (150, 170, 190), {'mm': 8, 'g': FL([150, 170, 190], [[110, 130, 150, 3], [200, 210, 220, 3]], 7000, .005, 1, .55, .1)}),   # recycled PVC tiles
 'INN-0249': ('clay', (200, 190, 170), {'mm': 15, 'contrast': 1.4}),              # protein bioplastic
 'INN-0250': ('plywood', (230, 214, 186), {'mm': 18}),                            # NAF plywood
 'INN-0251': ('plywood', (236, 214, 176), {'mm': 18}),                            # NAF poplar plywood
 'INN-0252': ('silk', (170, 190, 210), {}),                                       # bio-PA610
 'INN-0253': ('woven-natural', (70, 96, 130), {}),                                # recycled cotton denim
 'INN-0254': ('pet-felt', (60, 60, 62), {'soft': (.45, .008, .5), 'p': {'sheen': .8, 'sheenColor': '#9a9aa0'}}),   # recycled carbon fibre mat
})

SPEC.update({
 'INN-0255': ('wool-felt', (200, 176, 156), {'soft': (.55, .01, .4)}),            # recycled wool padding
 'INN-0256': ('pet-felt', None, {'g': FL([96, 98, 104], [[60, 62, 70, 3], [150, 140, 140, 2], [120, 60, 70, 1], [70, 90, 130, 1]], 9000, .004, 4, .95), 'mm': 40}),   # recycled textile insulation
 'INN-0257': ('woven-natural', (220, 220, 100), {}),                              # recycled textile pigment
 'INN-0258': ('woven-natural', (190, 174, 150), {}),                              # recycled linen/hemp
 'INN-0259': ('paper', None, {'g': FL([210, 206, 194], [[120, 116, 110, 3], [160, 150, 140, 2]], 1500, .002, 4, .85), 'soft': (.8, .03, .15)}),   # textile residue paper
 'INN-0260': ('mycelium-leather', (200, 150, 60), {'rgb2': (150, 100, 40), 'mottle': .5}),   # fine mycelium
 'INN-0261': ('paper', (60, 62, 66), {'soft': (.8, .03, .15)}),                   # leather waste paper
 'INN-0262': ('film', (240, 236, 226), {'p': {'opacity': .45}}),                  # cellulose film
 'INN-0263': ('tpe', (232, 228, 212), {'p': SATIN}),                              # bio-TPE
 'INN-0264': ('solid-surface', None, {'g': FL([110, 120, 140], [[60, 80, 120, 3], [200, 196, 186, 3], [150, 120, 90, 2]], 9000, .004, 4, .9), 'mm': 10}),   # textile + flax panels
 'INN-0265': ('plastic', (240, 240, 240), {}),                                    # bio-PA11
 'INN-0266': ('knit', (30, 60, 160), {}),                                         # degradable elastane
 'INN-0267': ('chipboard', (214, 184, 136), {'contrast': .4, 'mm': 25}),          # NAF MDF
 'INN-0268': ('plastic', (90, 60, 44), {}),                                       # recycled PP
 'INN-0269': ('fur', (170, 130, 96), {}),                                         # cellulose faux fur
 'INN-0270': ('plastic', (220, 40, 50), {}),                                      # seaweed colour additive
 'INN-0271': ('coir-board', (190, 140, 70), {'mm': 40, 'contrast': 1.3}),         # mussel byssus insulation
 'INN-0272': ('paper', (240, 236, 220), {'soft': (.8, .03, .15), 'p': SATIN}),    # barrier coating
 'INN-0273': ('solid-surface', None, {'g': FL([200, 120, 70], [[160, 90, 50, 3], [230, 170, 120, 3]], 9000, .003, 1, .55, .1), 'mm': 12}),   # recycled PET sheet
 'INN-0275': ('woven-natural', (236, 232, 222), {}),                              # recycled cellulose fibre
 'INN-0276': ('yarn-natural', (176, 136, 96), {}),                                # naturally coloured cotton
 'INN-0277': ('clear-glass', (214, 230, 240), {}),                                # low-e glass
 'INN-0278': ('tpe', (60, 70, 80), {}),                                           # bio-PUR
 'INN-0279': ('silk', (130, 140, 220), {}),                                       # degradable PA66
 'INN-0280': ('pet-felt', (110, 130, 160), {'mm': 40}),                           # recycled cotton insulation
 'INN-0281': ('fur', (140, 90, 50), {}),                                          # bio PTT faux fur
 'INN-0282': ('plywood', (200, 150, 110), {'mm': 18}),                            # soy adhesive plywood
 'INN-0283': ('plywood', (232, 208, 176), {'mm': 18}),                            # soy NAF plywood
 'INN-0284': ('knit', (60, 100, 160), {}),                                        # MFC fibre
 'INN-0285': ('wood-fibre-board', (196, 170, 110), {'mm': 40}),                   # wood fibre insulation
 'INN-0287': ('clear-glass', (236, 224, 196), {'mm': 6}),                         # bio-epoxy
 'INN-0288': ('paper', None, {'g': FL([228, 220, 204], [[180, 60, 100, 3], [120, 140, 70, 3], [150, 90, 140, 2], [220, 160, 60, 1]], 700, .008, 2, .9), 'soft': (.75, .03, .2)}),   # petal wall covering
 'INN-0289': ('solid-surface', (220, 216, 210), {'mm': 12, 'rgb2': (70, 66, 64), 'mottle': 1, 'mfreq': 5, 'mpow': 3}),   # marbled rPP
 'INN-0290': ('film', (236, 240, 230), {'p': {'opacity': .5}}),                   # seaweed film
 'INN-0291': ('paper', (240, 236, 226), {'soft': (.45, .008, .5), 'p': {'transmission': .3}}),   # translucent paper
 'INN-0292': ('moulded-pulp', (244, 244, 242), {}),                               # thermoformed paper
 'INN-0293': ('knit', (30, 50, 90), {}),                                          # recycled polyester
 'INN-0294': ('plastic', (236, 180, 90), {}),                                     # biodegradable copolyester
 'INN-0295': ('plastic', (40, 40, 44), {}),                                       # bio-PA profiles
 'INN-0296': ('solid-surface', None, {'g': FL([130, 136, 120], [[80, 90, 80, 3], [190, 190, 180, 3], [60, 60, 56, 2]], 9000, .003, 1, .6), 'mm': 15}),   # recycled Tetra Pak
})

SPEC.update({
 'INN-0297': ('moulded-pulp', (228, 216, 186), {}),                               # bagasse packaging
 'INN-0298': ('silk', (248, 248, 246), {}),                                       # lyocell
 'INN-0299': ('woven-natural', (140, 146, 126), {}),                              # Refibra textile
 'INN-0300': ('plastic', (110, 112, 116), {}),                                    # bio-PE
 'INN-0301': ('neoprene', (40, 42, 48), {}),                                      # limestone neoprene
 'INN-0302': ('fibre-filled-plastic', (150, 110, 70), {}),                        # natural fibre biocomposite
 'INN-0303': ('woven-natural', (226, 200, 170), {}),                              # recycled cotton
 'INN-0304': ('silk', (180, 186, 210), {'rgb2': (90, 96, 130), 'mottle': .8, 'mfreq': 5, 'mpow': 2.5}),   # bacterial dye
 'INN-0305': ('latex-foam', (238, 226, 196), {}),                                 # organic latex foam
 'INN-0306': ('plastic', (244, 244, 244), {'mm': 20, 'g': ('relief', {'base': 'silicone', 'hue_to': [244, 244, 244], 'pattern': 'chevron', 'rows': 8, 'lines': 2, 'amp': 1, 'depth': .6, 'ao': .2})}),   # PP honeycomb
 'INN-0307': ('ash', (150, 96, 56), {'contrast': 1.3, 'mm': 25}),                 # thermowood
 'INN-0308': ('film', (240, 242, 230), {}),                                       # compostable film
 'INN-0309': ('leather', (110, 50, 34), {'p': GLOSS}),                            # chitosan leather
 'INN-0310': ('film', (248, 230, 90), {'p': {'opacity': .55}}),                   # protein packaging film
 'INN-0311': ('hemp-board', (166, 160, 146), {'mm': 30}),                         # hempcrete
 'INN-0312': ('leather', (60, 70, 72), {}),                                       # plant-based leather
 'INN-0313': ('silk', (190, 150, 110), {}),                                       # tussah silk
 'INN-0314': ('pet-felt', (150, 180, 200), {'mm': 40}),                           # denim insulation
 'INN-0315': ('plastic', (230, 226, 218), {}),                                    # PHA from seaweed
 'INN-0316': ('plastic', (232, 190, 40), {}),                                     # bio-PP
 'INN-0317': ('wool-pile', (40, 60, 110), {}),                                    # recycled textile fill
 'INN-0318': ('pet-felt', None, {'g': FL([60, 80, 120], [[30, 40, 70, 3], [120, 150, 180, 2], [100, 120, 70, 1]], 9000, .004, 4, .95), 'mm': 20}),   # compressed textile panel
 'INN-0319': ('knit', (20, 140, 80), {}),                                         # recycled cotton
 'INN-0320': ('wool-pile', (244, 236, 220), {}),                                  # milkweed fibre
 'INN-0321': ('paper', (246, 246, 244), {'soft': (.85, .035, .1), 'p': SATIN}),   # paper + PLA
 'INN-0322': ('chipboard', (214, 190, 150), {'mm': 18}),                          # low-formaldehyde panel
 'INN-0323': ('woven-synthetic', (120, 130, 90), {}),                             # bio-PA textile
 'INN-0324': ('plastic', (180, 30, 30), {}),                                      # bio-based hydrocarbons
 'INN-0325': ('leather', (170, 80, 50), {}),                                      # cultivated leather
 'INN-0326': ('plastic', (200, 230, 226), {}),                                    # PHA
 'INN-0327': ('leather', (190, 120, 60), {}),                                     # tea leaf leather
 'INN-0328': ('brick', (150, 150, 90), {'contrast': 1.3}),                        # waste-based brick
 'INN-0329': ('wood-fibre-board', (214, 186, 120), {'mm': 18, 'contrast': 1.3}),  # wheat straw board
 'INN-0330': ('film', (240, 210, 150), {'p': {'opacity': .55}}),                  # plant protein film
 'INN-0331': ('plastic', (60, 120, 50), {}),                                      # algae bioplastic
 'INN-0332': ('wool-felt', (100, 76, 60), {'soft': (.55, .01, .4)}),              # yak fibre nonwoven
 'INN-0333': ('cedar', (36, 34, 34), {'contrast': 2, 'mm': 20, 'rough_add': .3}), # charred wood
 'INN-0334': ('neoprene', (30, 30, 32), {}),                                      # natural rubber wetsuit foam
 'INN-0335': ('film', (236, 230, 200), {'p': {'opacity': .5}}),                   # seaweed film
 'INN-0336': ('leather', (180, 90, 50), {}),                                      # biofabricated collagen
})

SPEC.update({
 'INN-0337': ('moulded-pulp', (236, 232, 222), {}),                               # PFAS-free moulded paper
 'INN-0057': ('translucent', (232, 216, 170), {'mm': 2}),                         # chitosan film / sheet (no photo)
 'INN-0143': ('wool-felt', (210, 196, 160), {'mm': 30}),                          # hemp fibre pad (no photo)
})
