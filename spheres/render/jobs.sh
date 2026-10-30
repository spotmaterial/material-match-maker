# key  source  tiles  prep-options   (textures: ambientCG CC0 via PatrickJnr/cc0-texture-pack)
C=/home/claude/dl/candpng; N=/home/claude/dl/nrmpng
p(){ python3 -I prep.py $C/$2.png $N/$2.png src/$1 "$4" && python3 -I bake.py src/$1 baked/$1 $3; }
p oak            wood058    0.22 '{"rough":0.62,"rough_var":0.2,"tint":[0.96,0.99,0.9],"sat":0.9}'
p oak-b          wood003    0.22 '{"rough":0.62,"rough_var":0.2,"sat":0.85}'
p softwood       wood019    0.22 '{"rough":0.7,"rough_var":0.2}'
p softwood-b     wood014    0.22 '{"rough":0.7,"rough_var":0.2}'
p plywood-face   wood017    0.25 '{"rough":0.7,"rough_var":0.15}'
p plywood-cross  wood017    0.25 '{"rough":0.75,"rough_var":0.15,"rot90":true,"bright":0.74,"sat":1.15}'
p cork           cork001    0.9 '{"rough":0.9,"rough_var":0.1,"hue_to":[158,112,72]}'
p wool-felt      fabric043  0.6 '{"rough":1.0,"rough_var":0.05,"sat":0.5,"bright":0.92}'
p pet-felt       fabric034  0.5 '{"rough":1.0,"rough_var":0.05,"gray":true,"bright":0.78}'
p woven-synthetic fabric039 0.45 '{"rough":0.85,"rough_var":0.1}'
p woven-natural  fabric036  0.45 '{"rough":0.95,"rough_var":0.05,"hue_to":[196,184,160]}'
p leather        leather028 0.35 '{"rough":0.55,"rough_var":0.25}'
p concrete       concrete006 0.2 '{"rough":0.9,"rough_var":0.1}'
p aluminium      metal011   0.2 '{"rough":0.35,"rough_var":0.15,"gray":true,"bright":1.05}'
p stainless      metal010   0.2 '{"rough":0.22,"rough_var":0.1,"gray":true,"bright":0.95}'
