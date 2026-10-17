"""Biblioteca de Reels animados MBDev (HTML + Web Animations -> MP4 1080x1920 via Playwright e ffmpeg).
Veja exemplos_reels.py. Imagens de celular ficam em assets/<nome>.jpg (750x1430)."""
import sys, pathlib, asyncio, subprocess
from playwright.async_api import async_playwright
from fonts import css
T=pathlib.Path(__file__).resolve().parent; ASSETS=T/"assets"
FF=css()
BASE="""
*{box-sizing:border-box}html,body{margin:0;width:1080px;height:1920px;overflow:hidden}
.stage{position:relative;width:1080px;height:1920px;overflow:hidden;font-family:Inter,sans-serif}
.abs{position:absolute}
.acc{font-family:Fraunces,Georgia,serif;font-style:italic;font-weight:600;font-variation-settings:'opsz' 9}
.tag{font-family:Outfit;font-weight:600;font-size:28px;letter-spacing:7px}
.h{font-family:Outfit;font-weight:700;letter-spacing:-3px;line-height:1.04;margin:0}
.line{display:block}
.phone{border-radius:70px;padding:18px;overflow:hidden}
.screen{width:100%;height:100%;border-radius:54px;overflow:hidden;position:relative}
.screen img{width:100%;display:block;transform-origin:top center}
.chip{font-family:Outfit;font-weight:600;font-size:36px;padding:24px 34px;border-radius:999px;display:flex;align-items:center;gap:16px;white-space:nowrap;box-shadow:0 18px 50px rgba(0,0,0,.28)}
.dot{width:16px;height:16px;border-radius:8px;background:#6D1220;flex:none}
@keyframes rise{from{opacity:0;transform:translateY(50px)}to{opacity:1;transform:none}}
@keyframes fade{from{opacity:0}to{opacity:1}}
@keyframes fadeout{from{opacity:1}to{opacity:0}}
@keyframes pop{0%{opacity:0;transform:scale(.7)}70%{opacity:1;transform:scale(1.04)}100%{opacity:1;transform:scale(1)}}
@keyframes wipe{from{transform:translateY(100%)}to{transform:none}}
"""
def page(body,css=""):
    return f"<!doctype html><html><head><meta charset=utf-8><style>{FF}{BASE}{css}</style></head><body><div class=stage>{body}</div></body></html>"
async def render(html,out,dur,fps=30,stills=()):
    (T/"_tmp").mkdir(exist_ok=True); p=T/"_tmp"/(pathlib.Path(out).stem+".html"); p.write_text(html)
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.goto(f"file://{p}"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(400)
        await pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        for t,name in stills:
            await pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={t*1000})")
            await pg.screenshot(path=str(pathlib.Path(out).parent/name))
        ff=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(fps),"-i","-","-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest","-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p","-c:a","aac","-b:a","128k","-movflags","+faststart",str(out)],stdin=subprocess.PIPE)
        n=int(dur*fps)
        for i in range(n):
            await pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={i*1000/fps})")
            ff.stdin.write(await pg.screenshot(type="jpeg",quality=95))
        ff.stdin.close(); ff.wait(); await b.close()

E="cubic-bezier(.2,.8,.2,1)"
def A(*xs): return "animation:"+",".join(f"{n} {d}s {e or E} {t}s {'forwards' if n in ('outL','fadeout') and i>0 else 'both'}" for i,(n,d,t,e) in enumerate([(x+(None,))[:4] for x in xs]))+";"
LOGO_W=f"file://{ASSETS}/logo-branco.png"; LOGO_B=f"file://{ASSETS}/logo-bordo.png"
PLAY='<svg width="22" height="24" viewBox="0 0 20 22"><path d="M2 2L18 11L2 20Z" fill="#FFFFFF"/></svg>'

def tag(text,color,t=0.1,top=200):
    return f'<div class="abs" style="left:90px;top:{top}px;display:flex;align-items:center;gap:18px;{A(("fade",.6,t))}"><div style="width:64px;height:64px;border-radius:32px;background:#6D1220;display:flex;align-items:center;justify-content:center">{PLAY}</div><div class="tag" style="color:{color}">{text}</div></div>'

def headline(lines,color,top,size=100,t0=.25,step=.22,extra=""):
    ls="".join(f'<span class="line" style="{A(("rise",.8,t0+i*step))}">{l}</span>' for i,l in enumerate(lines))
    return f'<h1 class="h abs" style="left:90px;right:90px;top:{top}px;font-size:{size}px;color:{color};{extra}">{ls}</h1>'

def phone(img,left,top,w,frame,anim,rot=0,pan=(1.0,1.06,0,-7,2.0,8.0)):
    h=round((w-36)*1430/750+36)
    s0,s1,y0,y1,pt,pd=pan
    css_id=f"p{abs(hash(img+str(left)))%10000}"
    kf=f"@keyframes {css_id}{{from{{transform:scale({s0}) translateY({y0}%)}}to{{transform:scale({s1}) translateY({y1}%)}}}}"
    return kf, f'<div class="abs" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);{anim}"><div class="phone" style="width:100%;height:100%;background:{frame};box-shadow:0 40px 90px rgba(0,0,0,.35),0 0 0 3px #2A2E38"><div class="screen"><img src="file://{ASSETS}/{img}.jpg" style="animation:{css_id} {pd}s cubic-bezier(.45,0,.35,1) {pt}s both"></div></div></div>'

def chip(text,pos,t,bg="#FFFFFF",fg="#080C14"):
    return f'<div class="abs chip" style="{pos};background:{bg};color:{fg};{A(("pop",.6,t))}"><span class="dot"></span>{text}</div>'

def endcard(t,title,sub="Peça seu orçamento · link na bio"):
    return f'''<div class="abs" style="inset:0;background:#6D1220;{A(("wipe",.7,t))}">
<div class="abs" style="left:90px;right:90px;top:620px;display:flex;flex-direction:column;align-items:center;text-align:center;gap:44px">
<img src="{LOGO_W}" style="height:190px;{A(("rise",.7,t+.45))}">
<h2 class="h" style="font-size:84px;color:#fff;{A(("rise",.7,t+.65))}">{title}</h2>
<div style="font-family:Outfit;font-weight:600;font-size:38px;color:#E9DCD8;{A(("rise",.7,t+.85))}">{sub}</div>
<div style="font-family:Inter;font-size:32px;color:#E9DCD8;opacity:.85;{A(("fade",.7,t+1.05))}">@mbdevsites · mbdev.com.br</div>
</div></div>'''

