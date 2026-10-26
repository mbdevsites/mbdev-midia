import sys, pathlib, asyncio, subprocess
from playwright.async_api import async_playwright
S=pathlib.Path("/tmp/claude-0/-home-claude/bcb47e16-b548-5c1b-88da-de6f355698a0/scratchpad"); R=S/"render"; F=R/"node_modules/@fontsource"
FF=f"@font-face{{font-family:'Fraunces';font-style:italic;font-weight:100 900;src:url('file://{R}/node_modules/@fontsource-variable/fraunces/files/fraunces-latin-full-italic.woff2')}}\n"
for fam,pkg,w in [("Outfit","outfit",500),("Outfit","outfit",600),("Outfit","outfit",700),("Inter","inter",400),("Inter","inter",500)]:
    FF+=f"@font-face{{font-family:'{fam}';font-weight:{w};src:url('file://{F}/{pkg}/files/{pkg}-latin-{w}-normal.woff2')}}\n"
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
    p=S/"reels"/(pathlib.Path(out).stem+".html"); p.write_text(html)
    async with async_playwright() as pw:
        b=await pw.chromium.launch(); pg=await b.new_page(viewport={"width":1080,"height":1920})
        await pg.goto(f"file://{p}"); await pg.evaluate("document.fonts.ready"); await pg.wait_for_timeout(400)
        await pg.evaluate("document.getAnimations().forEach(a=>a.pause())")
        for t,name in stills:
            await pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={t*1000})")
            await pg.screenshot(path=str(S/"reels"/name))
        ff=subprocess.Popen(["ffmpeg","-y","-loglevel","error","-f","image2pipe","-framerate",str(fps),"-i","-","-f","lavfi","-i","anullsrc=r=44100:cl=stereo","-shortest","-c:v","libx264","-preset","medium","-crf","18","-pix_fmt","yuv420p","-c:a","aac","-b:a","128k","-movflags","+faststart",str(out)],stdin=subprocess.PIPE)
        n=int(dur*fps)
        for i in range(n):
            await pg.evaluate(f"document.getAnimations().forEach(a=>a.currentTime={i*1000/fps})")
            ff.stdin.write(await pg.screenshot(type="jpeg",quality=95))
        ff.stdin.close(); ff.wait(); await b.close()
