import pathlib
T=pathlib.Path(__file__).resolve().parent; F=T/"node_modules/@fontsource"
def css():
    ff=f"@font-face{{font-family:'Fraunces';font-style:italic;font-weight:100 900;src:url('file://{T}/node_modules/@fontsource-variable/fraunces/files/fraunces-latin-full-italic.woff2')}}\n"
    for fam,pkg,w,st in [("Bodoni Moda","bodoni-moda",400,"normal"),("Bodoni Moda","bodoni-moda",500,"normal"),("Outfit","outfit",500,"normal"),("Outfit","outfit",600,"normal"),("Outfit","outfit",700,"normal"),("Inter","inter",400,"normal"),("Inter","inter",500,"normal"),("Inter","inter",600,"normal")]:
        ff+=f"@font-face{{font-family:'{fam}';font-weight:{w};font-style:{st};src:url('file://{F}/{pkg}/files/{pkg}-latin-{w}-{st}.woff2')}}\n"
    return ff
