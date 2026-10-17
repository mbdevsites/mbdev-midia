"""Modelos de slides 1080x1350 no formato .dc.html do canvas (capa, numerado, chamada final). Temas: light, white, bordo."""
import pathlib
G=pathlib.Path(".")  # defina carrossel.G = pasta de saida antes de chamar
def carrossel_G(): return G
TH={
 "light":dict(bg="#F5EFED",fg="#080C14",acc="#6D1220",sub="#3A3C44",pg="#5A5C66",logo="76cc8fa3bab7fb73f9e41b3cd87b6e79",line="#D9C9C4",btnbg="#6D1220",btnfg="#FFFFFF",card="#FFFFFF"),
 "white":dict(bg="#FFFFFF",fg="#080C14",acc="#6D1220",sub="#3A3C44",pg="#5A5C66",logo="76cc8fa3bab7fb73f9e41b3cd87b6e79",line="#D9C9C4",btnbg="#6D1220",btnfg="#FFFFFF",card="#F5EFED"),
 "bordo":dict(bg="#6D1220",fg="#FFFFFF",acc="#E9DCD8",sub="#E9DCD8",pg="#E9DCD8",logo="47b8413524343c6a05eb2274c485f012",line="rgba(233,220,216,0.35)",btnbg="#FFFFFF",btnfg="#6D1220",card="rgba(255,255,255,0.08)"),
}
FONT='<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400..800&amp;family=Fraunces:ital,opsz,wght@1,9..144,500..700&amp;family=Inter:wght@400;500;600&amp;family=Outfit:wght@400;500;600;700;800&amp;display=swap">'
def acc(t,c): return f'<span style="font-family: Fraunces, Georgia, serif; font-style: italic; font-weight: 600; font-variation-settings: \'opsz\' 9; color: {c}">{t}</span>'
def wrap(title,t,inner,footer_right):
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<title>{title}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
{FONT}
<style>
body{{margin:0}}
</style>
</helmet>
<div style="width: 1080px; height: 1350px; box-sizing: border-box; padding: 88px; background: {t['bg']}; color: {t['fg']}; display: flex; flex-direction: column; justify-content: space-between; font-family: Inter, sans-serif">
{inner}
<div style="display: flex; justify-content: space-between; align-items: flex-end">
<img src="/_blob/{t['logo']}" alt="MBDev" style="height: 116px; width: auto; display: block">
{footer_right}
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
renderVals() {{ return {{}}; }}
}}
</script>
</body>
</html>
'''
def head(t,tag,page): return f'<div style="display: flex; justify-content: space-between; align-items: center"><div style="font-family: Outfit, sans-serif; font-weight: 600; font-size: 24px; letter-spacing: 6px; color: {t["acc"]}">{tag}</div><div style="font-size: 24px; color: {t["pg"]}">{page}</div></div>'
def swipe(t,txt="Arraste"): return f'<div style="display: flex; align-items: center; gap: 14px; font-family: Outfit, sans-serif; font-weight: 600; font-size: 26px; color: {t["acc"] if t["bg"]!="#6D1220" else "#FFFFFF"}">{txt} <svg width="40" height="20" viewBox="0 0 40 20" aria-hidden="true"><path d="M0 10H36M28 2L36 10L28 18" fill="none" stroke="{t["acc"] if t["bg"]!="#6D1220" else "#FFFFFF"}" stroke-width="2.5"/></svg></div>'
def handle(t): return f'<div style="font-family: Outfit, sans-serif; font-weight: 600; font-size: 26px; color: {t["acc"]}">@mbdevsites</div>'
def cover(name,title,th,tag,page,h1,sub):
    t=TH[th]
    inner=head(t,tag,page)+f'<div style="display: flex; flex-direction: column; gap: 40px"><h1 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 112px; line-height: 1.02; letter-spacing: -4px; text-wrap: balance">{h1}</h1><p style="margin: 0; font-size: 36px; line-height: 1.4; color: {t["sub"]}; max-width: 860px">{sub}</p></div>'
    (carrossel_G()/f"{name}.dc.html").write_text(wrap(title,t,inner,swipe(t)))
def numbered(name,title,th,tag,page,num,h2,body):
    t=TH[th]
    inner=head(t,tag,page)+f'<div style="display: flex; flex-direction: column; gap: 40px"><div style="font-family: Outfit, sans-serif; font-weight: 700; font-size: 200px; line-height: 0.85; letter-spacing: -8px; color: {t["acc"]}">{num}</div><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 84px; line-height: 1.04; letter-spacing: -2.5px; text-wrap: balance">{h2}</h2><p style="margin: 0; font-size: 34px; line-height: 1.45; color: {t["sub"]}; max-width: 860px">{body}</p></div>'
    (carrossel_G()/f"{name}.dc.html").write_text(wrap(title,t,inner,swipe(t)))
def cta(name,title,th,tag,page,h2,body,btn):
    t=TH[th]
    inner=head(t,tag,page)+f'<div style="display: flex; flex-direction: column; gap: 44px"><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 96px; line-height: 1.04; letter-spacing: -2.5px; text-wrap: balance">{h2}</h2><p style="margin: 0; font-size: 34px; line-height: 1.45; color: {t["sub"]}; max-width: 860px">{body}</p><div style="align-self: flex-start; background: {t["btnbg"]}; color: {t["btnfg"]}; font-family: Outfit, sans-serif; font-weight: 600; font-size: 32px; border-radius: 999px; padding: 26px 48px">{btn}</div></div>'
    (carrossel_G()/f"{name}.dc.html").write_text(wrap(title,t,inner,handle(t)))

