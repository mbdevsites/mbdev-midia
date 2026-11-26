"""Semana 7: Reel de terça (portfólio pediatria, simulação: 21h, febre, a mãe procura no celular) e Reel de quinta (bastidores só com texto: 3 coisas que eu não coloco no site de nenhum cliente).
Uso: PYTHONPATH=ferramentas python3 semana07_reels.py <pasta_saida> S7b S7d"""
import sys, asyncio, pathlib
from reel import *
OUT=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(".")
BOR,BEG,BEC,PRE,LN="#6D1220","#E9DCD8","#F5EFED","#080C14","#D9C9C4"
def ACC(w,c=BEG): return f'<span class="acc" style="color:{c}">{w}</span>'
def H(sz,c="#FFFFFF"): return f"font-family:Outfit;font-weight:700;font-size:{sz}px;letter-spacing:-3px;line-height:1.04;color:{c}"
P="font-family:Inter;font-size:44px;line-height:1.4;color:#C9C3C6"
def scene(t0,t1,inner,style="inset:0"):
    out=(("fadeout",.3,t1),) if t1 else ()
    return f'<div class="abs" style="{style};{A(("fade",.01,t0),*out)}">{inner}</div>'
def R(t,html,extra=""): return f'<div style="{A(("rise",.55,t))}{extra}">{html}</div>'

def reelS7b():
    css=f".stage{{background:{PRE}}}"
    body=tag("PORTFÓLIO · SIMULAÇÃO",BEG)
    body+=scene(0,3.0,f'<div class="abs" style="left:90px;right:90px;top:600px">'+R(.1,f'<div style="{H(124)}">21h. O filho com febre. A mãe pega o {ACC("celular.")}</div>')+R(.9,"Ela abre o site da primeira pediatra que aparece na busca.",P+";margin-top:44px")+'</div>')
    kf,ph=phone("pediatra",290,700,500,"#1A1D24",A(("rise",.8,3.1)),pan=(1.0,1.0,0,0,0,1))
    css+=kf
    lab=f'<div class="abs" style="left:90px;right:90px;top:300px">'+R(3.1,f'<div style="{H(84)}">Em poucos segundos, ela {ACC("encontra:")}</div>')+'</div>'
    chips=chip("Telefone e horário no topo","left:50px;top:820px",4.3)+chip("Do nascimento à adolescência","right:40px;top:1160px",5.7)+chip("Agendar consulta em um toque","left:40px;top:1480px",7.1)
    body+=scene(3.0,10.2,lab+ph+chips)
    body+=f'<div class="abs" style="inset:0;background:{BOR};{A(("wipe",.6,10.3),("fadeout",.3,13.4))}"><div class="abs" style="left:90px;right:90px;top:640px">'+R(10.7,f'<div style="{H(104)}">Consulta marcada para amanhã cedo. Sem esperar ninguém {ACC("atender.")}</div>')+'</div></div>'
    body+=endcard(13.5,'O seu site responde <span class="acc" style="color:#E9DCD8">assim?</span>',"Comente SITE · a gente te responde")
    return page(body,css),16.5

def reelS7d():
    css=f".stage{{background:{BEC}}}@keyframes slide{{0%,28%{{transform:translateX(0)}}33%,61%{{transform:translateX(-33.333%)}}66%,94%{{transform:translateX(-66.666%)}}100%{{transform:translateX(0)}}}}@keyframes shake{{0%,100%{{transform:rotate(0)}}25%{{transform:rotate(-8deg)}}75%{{transform:rotate(8deg)}}}}"
    FG=PRE; PS="font-family:Inter;font-size:42px;line-height:1.4;color:#3A3C44;margin-top:36px"
    def lab(t,txt): return R(t,f'<div class="tag" style="color:{BOR}">{txt}</div>')
    body=tag("BASTIDORES · EM PRIMEIRA PESSOA",BOR)
    body+=scene(0,3.0,f'<div class="abs" style="left:90px;right:90px;top:640px">'+R(.1,f'<div style="{H(124,FG)}">3 coisas que eu não coloco no site de {ACC("nenhum",BOR)} cliente.</div>')+'</div>')
    spk=f'<div style="margin-top:60px;width:220px;height:220px;border-radius:40px;background:#fff;border:3px solid {LN};display:flex;align-items:center;justify-content:center;{A(("pop",.5,4.2))}"><svg width="130" height="130" viewBox="0 0 24 24" style="animation:shake .25s linear 4.8s 6"><path d="M4 9h4l5-4v14l-5-4H4z" fill="{BOR}"/><path d="M16 9l5 6M21 9l-5 6" stroke="{BOR}" stroke-width="2" stroke-linecap="round"/></svg></div>'
    body+=scene(3.1,6.6,f'<div class="abs" style="left:90px;right:90px;top:560px">'+lab(3.2,"01 · MÚSICA QUE TOCA SOZINHA")+R(3.4,f'<div style="{H(100,FG)};margin-top:30px">Ninguém quer o celular {ACC("tocando",BOR)} na sala de espera.</div>')+spk+R(5.0,"Quem abre o seu site no ônibus ou no consultório fecha na hora.",PS)+'</div>')
    img=f'<div style="margin-top:56px;display:flex;gap:28px;align-items:flex-end;{A(("rise",.5,7.6))}"><div style="width:300px;height:200px;border-radius:24px;background:linear-gradient(135deg,#C9B6B0,#8E6F69);display:flex;align-items:center;justify-content:center;font-family:Outfit;font-weight:700;font-size:20px;color:#fff;text-align:center;padding:16px">PROMOÇÃO DE NATAL · AGENDE JÁ PELO SITE</div><div style="font-family:Inter;font-size:34px;color:#3A3C44;max-width:520px">texto pequeno, preso dentro da foto</div></div>'
    body+=scene(6.7,10.2,f'<div class="abs" style="left:90px;right:90px;top:560px">'+lab(6.8,"02 · TEXTO DENTRO DA FOTO")+R(7.0,f'<div style="{H(100,FG)};margin-top:30px">Texto em imagem não {ACC("aumenta",BOR)} no celular.</div>')+img+R(8.4,"Não dá para copiar, e o Google lê com mais dificuldade. Texto de verdade vai em texto.",PS)+'</div>')
    bn="".join(f'<div style="flex:none;width:900px;height:220px;background:{c};display:flex;align-items:center;padding:0 50px;font-family:Outfit;font-weight:700;font-size:52px;color:#fff">{w}</div>' for c,w in ((BOR,"Agende sua aval..."),("#3A3C44","Conheça nossa equ..."),("#8E6F69","Promoção válida at...")))
    ban=f'<div style="margin-top:56px;width:900px;height:220px;border-radius:28px;overflow:hidden;{A(("rise",.5,11.2))}"><div style="display:flex;width:2700px;animation:slide 2.4s linear 11.4s 2">{bn}</div></div>'
    body+=scene(10.3,13.8,f'<div class="abs" style="left:90px;right:90px;top:560px">'+lab(10.4,"03 · BANNER QUE PASSA SOZINHO")+R(10.6,f'<div style="{H(100,FG)};margin-top:30px">Se passa sozinho, ninguém {ACC("termina",BOR)} de ler.</div>')+ban+R(12.0,"Uma mensagem forte e parada vale mais que cinco fugindo da tela.",PS)+'</div>')
    body+=endcard(13.9,'Cada detalhe é pensado para o seu <span class="acc" style="color:#E9DCD8">cliente.</span>',"Quer um site assim? Link na bio")
    return page(body,css),16.9

async def main(which):
    for name in which:
        html,dur=globals()["reel"+name]()
        await render(html,OUT/f"reel{name}.mp4",dur,stills=[(x,f"reel{name}_{x}.png") for x in (1.5,2.5,5.0,8.5,12.0,15.5)])
if __name__=='__main__': OUT.mkdir(parents=True,exist_ok=True); asyncio.run(main(sys.argv[2:]))
