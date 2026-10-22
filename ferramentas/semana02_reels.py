"""Semana 2: Reel de terça (curso online de crochê) e Reel de quinta em versão animada (um dia criando um site).
Uso: python3 semana02_reels.py <pasta_saida> S2b S2d"""
import sys, asyncio, pathlib
from reel import *
OUT=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(".")

def reelS2b():
    kf,ph=phone("croche",300,700,500,"#1A1D24",A(("rise",1.0,.9)),rot=4)
    body=tag("PROJETO · CURSO ONLINE","#E9DCD8")+headline(["Uma página.","Um objetivo:",'<span class="acc" style="color:#E9DCD8">vender.</span>'],"#fff",300,100)+ph
    body+=chip("Promessa clara no topo","left:60px;top:900px",3.0)
    body+=chip("Contagem regressiva","right:60px;top:1210px",4.4)
    body+=chip("Tudo leva ao botão de compra","left:60px;top:1470px",5.8)
    body+=endcard(9.4,'Vai lançar um curso? Sua página precisa <span class="acc" style="color:#E9DCD8">vender</span> por você.')
    return page(body,kf+".stage{background:#080C14}"),12.5

def reelS2d():
    BG,FG,AC,SUB,LN="#F5EFED","#080C14","#6D1220","#3A3C44","#D9C9C4"
    def scene(t0,t1,inner,top=420):
        out=(("fadeout",.4,t1),) if t1 else ()
        return f'<div class="abs" style="left:90px;right:90px;top:{top}px;{A(("fade",.01,t0),*out)}">{inner}</div>'
    def R(t,html,extra=""): return f'<div style="{A(("rise",.7,t))}{extra}">{html}</div>'
    H=lambda sz: f"font-family:Outfit;font-weight:700;font-size:{sz}px;letter-spacing:-3px;line-height:1.04;color:{FG}"
    P=f"font-family:Inter;font-size:40px;line-height:1.4;color:{SUB};margin-top:30px"
    TAG=lambda x: f'<div class="tag" style="color:{AC}">{x}</div>'
    # rascunho (wireframe tracejado) e versao colorida
    def wire(t,filled):
        b=(lambda c: f"background:{c};border:none") if filled else (lambda c: f"background:transparent;border:4px dashed {AC}")
        blocks=[("height:70px;width:55%",AC if filled else ""),("height:230px",'#E9DCD8'),("height:46px;width:80%",FG),("height:46px;width:60%",'#CDBDB8'),("height:96px;width:50%;border-radius:999px",'#25A55F')]
        inner="".join(f'<div style="{s};{b(c)};border-radius:{"999px" if "999" in s else "18px"};{A(("pop",.5,t+.35*i))}"></div>' for i,(s,c) in enumerate(blocks))
        return f'<div style="margin-top:56px;width:640px;height:760px;background:#FFFFFF;border-radius:40px;padding:48px;display:flex;flex-direction:column;gap:34px;box-shadow:0 30px 70px rgba(8,12,20,.12)">{inner}</div>'
    body=tag("BASTIDORES · UM DIA DE TRABALHO",AC)
    body+=scene(0,3.0,R(.2,f'<div style="{H(130)}">Um dia criando<br>um <span class="acc" style="color:{AC}">site.</span></div>')+R(.8,"Do rascunho ao ar, em poucos passos.",P),top=720)
    body+=scene(3.3,7.6,R(3.4,TAG("01 · NO PAPEL"))+R(3.6,f'<div style="{H(92)};margin-top:26px">Começa no <span class="acc" style="color:{AC}">rascunho.</span></div>')+R(3.9,"Antes de abrir o computador, desenho o que o seu cliente precisa ver primeiro.",P)+wire(4.4,False))
    body+=scene(7.9,12.0,R(8.0,TAG("02 · DESIGN"))+R(8.2,f'<div style="{H(92)};margin-top:26px">Depois, ganha <span class="acc" style="color:{AC}">cor.</span></div>')+R(8.5,"Fontes, cores e fotos que combinam com o seu negócio.",P)+wire(8.9,True))
    kf,ph=phone("pediatra",270,840,540,"#080C14",A(("rise",.9,12.9)),pan=(1.0,1.06,0,-7,13.6,3.2))
    body+=scene(12.3,16.8,R(12.4,TAG("03 · TESTES"))+R(12.6,f'<div style="{H(92)};margin-top:26px">Testo tudo no <span class="acc" style="color:{AC}">celular.</span></div>')+R(12.9,"É ali que o seu cliente vai abrir o site.",P))
    body+=f'<div class="abs" style="inset:0;{A(("fade",.01,12.3),("fadeout",.4,16.8))}">{ph}</div>'
    CK=f'<svg width="56" height="56" viewBox="0 0 56 56" aria-hidden="true"><circle cx="28" cy="28" r="28" fill="{AC}"/><path d="M16 29l8 8 16-17" fill="none" stroke="#fff" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    items="".join(R(17.8+i*.45,f'<div style="display:flex;align-items:center;gap:30px;padding:30px 0;border-top:3px solid {LN}">{CK}<span style="font-family:Outfit;font-weight:600;font-size:64px;color:{FG}">{x}</span></div>') for i,x in enumerate(["Velocidade","Botão do WhatsApp","Pronto para o Google"]))
    body+=scene(17.1,21.0,R(17.2,TAG("04 · AJUSTES FINOS"))+R(17.4,f'<div style="{H(92)};margin-top:26px">Confiro cada <span class="acc" style="color:{AC}">detalhe.</span></div>')+f'<div style="margin-top:40px">{items}</div>',top=560)
    body+=scene(21.3,None,R(21.4,f'<div style="{H(150)}">E o site vai<br>ao <span class="acc" style="color:{AC}">ar.</span></div>'),top=760)
    body+=endcard(23.4,'O próximo site<br>pode ser o <span class="acc" style="color:#E9DCD8">seu.</span>')
    return page(body,kf+f".stage{{background:{BG}}}"),26.5

async def main(which):
    for name in which:
        html,dur=globals()["reel"+name]()
        await render(html,OUT/f"reel{name}.mp4",dur,stills=[(t,f"reel{name}_{t}.png") for t in (2.5,6.0,10.5,15.0,19.5,22.5,dur-0.5)])
if __name__=='__main__': OUT.mkdir(parents=True,exist_ok=True); asyncio.run(main(sys.argv[2:]))
