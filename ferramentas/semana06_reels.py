"""Semana 6: Reel de terça (portfólio barbearia: as 3 perguntas da primeira tela) e Reel de quinta (bastidores só com texto: como eu escolho as cores de um site).
Uso: PYTHONPATH=ferramentas python3 semana06_reels.py <pasta_saida> S6b S6d"""
import sys, asyncio, pathlib
from reel import *
OUT=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(".")
BOR,BEG,BEC,PRE,LN="#6D1220","#E9DCD8","#F5EFED","#080C14","#D9C9C4"
def ACC(w,c=BEG): return f'<span class="acc" style="color:{c}">{w}</span>'
def H(sz,c="#FFFFFF"): return f"font-family:Outfit;font-weight:700;font-size:{sz}px;letter-spacing:-3px;line-height:1.04;color:{c}"
P="font-family:Inter;font-size:42px;line-height:1.4;color:#C9C3C6"
def scene(t0,t1,inner,style="inset:0"):
    out=(("fadeout",.3,t1),) if t1 else ()
    return f'<div class="abs" style="{style};{A(("fade",.01,t0),*out)}">{inner}</div>'
def R(t,html,extra=""): return f'<div style="{A(("rise",.55,t))}{extra}">{html}</div>'

def reelS6b():
    css=f".stage{{background:{PRE}}}"
    body=tag("PORTFÓLIO · BARBEARIA",BEG)
    body+=scene(0,2.7,f'<div class="abs" style="left:90px;right:90px;top:620px">'+R(.1,f'<div style="{H(118)}">O cliente abriu o seu site. O que ele vê {ACC("primeiro?")}</div>')+R(.8,"Ele decide em poucos segundos se fica ou se volta para o Google.",P+";font-size:46px;margin-top:44px")+'</div>')
    kf,ph=phone("barbearia",290,700,500,"#1A1D24",A(("rise",.8,2.9)),pan=(1.0,1.0,0,0,0,1))
    css+=kf
    lab=f'<div class="abs" style="left:90px;right:90px;top:300px">'+R(2.9,f'<div style="{H(84)}">A primeira tela responde {ACC("3 perguntas.")}</div>')+'</div>'
    chips=chip("1 · O que você faz?","left:50px;top:900px",4.3)+chip("2 · É para mim?","right:50px;top:1180px",5.8)+chip("3 · Como eu marco?","left:50px;top:1460px",7.3)
    body+=scene(2.8,10.4,lab+ph+chips)
    body+=f'<div class="abs" style="inset:0;background:{BOR};{A(("wipe",.6,10.5),("fadeout",.3,13.4))}"><div class="abs" style="left:90px;right:90px;top:640px">'+R(10.9,f'<div style="{H(100)}">Se precisar rolar para entender, ele pode {ACC("ir embora.")}</div>')+'</div></div>'
    body+=endcard(13.5,'A sua primeira tela responde <span class="acc" style="color:#E9DCD8">as 3?</span>',"Comente TELA · a gente te responde")
    return page(body,css),16.5

def reelS6d():
    css=f".stage{{background:{BEC}}}@keyframes grow{{from{{transform:scaleY(0)}}to{{transform:none}}}}"
    FG="#080C14"; PS="font-family:Inter;font-size:42px;line-height:1.4;color:#3A3C44;margin-top:36px"
    def lab(t,txt): return R(t,f'<div class="tag" style="color:{BOR}">{txt}</div>')
    body=tag("BASTIDORES · EM PRIMEIRA PESSOA",BOR)
    body+=scene(0,3.0,f'<div class="abs" style="left:90px;right:90px;top:640px">'+R(.1,f'<div style="{H(118,FG)}">Antes de abrir o computador, eu faço {ACC("uma pergunta.",BOR)}</div>')+'</div>')
    body+=scene(3.1,6.4,f'<div class="abs" style="left:90px;right:90px;top:620px">'+lab(3.2,"01 · A SENSAÇÃO")+R(3.4,f'<div style="{H(104,FG)};margin-top:30px">Como o seu cliente deve se {ACC("sentir?",BOR)}</div>')+R(4.2,"Acolhido, seguro, animado? A cor começa aí, não no meu gosto.",PS)+'</div>')
    sw=lambda cols,t: '<div style="display:flex;gap:24px;margin-top:50px">'+"".join(f'<div style="flex:1;height:220px;border-radius:28px;background:{c};{"border:3px solid "+LN+";" if c in ("#FFFFFF",BEC) else ""}transform-origin:bottom;{A(("grow",.5,t+i*.18))}"></div>' for i,c in enumerate(cols))+'</div>'
    body+=scene(6.5,9.9,f'<div class="abs" style="left:90px;right:90px;top:560px">'+lab(6.6,"02 · O QUE JÁ É SEU")+R(6.8,f'<div style="{H(100,FG)};margin-top:30px">Logo, fachada, uniforme: eu parto do que você {ACC("já tem.",BOR)}</div>')+sw(["#1F3A5F","#C8A96A","#FFFFFF","#E4E7EC"],7.6)+'</div>')
    test=f'<div style="display:flex;flex-direction:column;gap:22px;margin-top:50px">'+R(10.9,f'<div style="background:#C8A96A;color:#FFFFFF;font-family:Outfit;font-weight:600;font-size:46px;border-radius:24px;padding:30px 36px;display:flex;justify-content:space-between">Agendar horário<span style="font-family:Inter;font-size:32px;opacity:.9">difícil de ler</span></div>')+R(11.5,f'<div style="background:#1F3A5F;color:#FFFFFF;font-family:Outfit;font-weight:600;font-size:46px;border-radius:24px;padding:30px 36px;display:flex;justify-content:space-between">Agendar horário<span style="font-family:Inter;font-size:32px;color:{BEG}">fácil de ler</span></div>')+'</div>'
    body+=scene(10.0,13.6,f'<div class="abs" style="left:90px;right:90px;top:560px">'+lab(10.1,"03 · O TESTE DA LEITURA")+R(10.3,f'<div style="{H(100,FG)};margin-top:30px">Toda cor passa por um teste: dá para {ACC("ler?",BOR)}</div>')+test+'</div>')
    body+=endcard(13.7,'Cor bonita é a que <span class="acc" style="color:#E9DCD8">funciona.</span>',"Quer um site com a sua cara? Link na bio")
    return page(body,css),16.7

async def main(which):
    for name in which:
        html,dur=globals()["reel"+name]()
        await render(html,OUT/f"reel{name}.mp4",dur,stills=[(x,f"reel{name}_{x}.png") for x in (1.5,2.5,5.0,8.5,12.0,15.5)])
if __name__=='__main__': OUT.mkdir(parents=True,exist_ok=True); asyncio.run(main(sys.argv[2:]))
