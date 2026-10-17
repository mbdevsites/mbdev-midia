"""Renderiza artboards .dc.html do canvas em PNG.
Uso: python3 render.py <pasta_com_dc_html> <pasta_saida> Nome1 Nome2 ...   (tamanho lido do $preview de cada arquivo)"""
import re, sys, json, pathlib, asyncio
from playwright.async_api import async_playwright
from fonts import css
T=pathlib.Path(__file__).resolve().parent; A=T/"assets"
BLOBS={"76cc8fa3bab7fb73f9e41b3cd87b6e79":"logo-bordo.png","47b8413524343c6a05eb2274c485f012":"logo-branco.png","bc666fb85c7f04034fcbdd1f3a533cd7":"barbearia.jpg","0622824ba4041cc150bb28b187f3df8c":"pediatra.jpg","c14594953aa8d4d840c6b0e9d5b7545c":"croche.jpg","4c2bc108dfa581a9dc64c5f4837abbdb":"advocacia.jpg"}
async def main(src,out,names):
    out.mkdir(parents=True,exist_ok=True); tmp=T/"_tmp"; tmp.mkdir(exist_ok=True)
    async with async_playwright() as pw:
        b=await pw.chromium.launch()
        for n in names:
            s=(src/f"{n}.dc.html").read_text()
            pv=json.loads(re.search(r"data-props='(.*?)'",s).group(1))["$preview"]; w,h=pv["width"],pv["height"]
            body=re.sub(r"<helmet>.*?</helmet>","",re.search(r"<x-dc>(.*)</x-dc>",s,re.S).group(1),flags=re.S)
            for k,v in BLOBS.items(): body=body.replace(f"/_blob/{k}",f"file://{A}/{v}")
            f=tmp/f"{n}.html"; f.write_text(f"<html><head><meta charset='utf-8'><style>{css()}body{{margin:0}}</style></head><body>{body}</body></html>")
            pg=await b.new_page(viewport={"width":w,"height":h}); await pg.goto(f"file://{f}")
            await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(300)
            await pg.screenshot(path=str(out/f"{n}.png")); await pg.close()
        await b.close()
if __name__=="__main__": asyncio.run(main(pathlib.Path(sys.argv[1]),pathlib.Path(sys.argv[2]),sys.argv[3:]))
