"""Semana 5 v2: Reel 'O site responde antes do WhatsApp' (doceria fictícia; perguntas no chat sem resposta x FAQ no site).
Uso: PYTHONPATH=ferramentas python3 semana05b_reels.py <pasta_saida> S5f"""
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

def reelS5f():
    css=f""".stage{{background:{PRE}}}
@keyframes bub{{0%{{opacity:0;transform:translateY(30px) scale(.9)}}100%{{opacity:1;transform:none}}}}
@keyframes open{{from{{max-height:0;opacity:0}}to{{max-height:160px;opacity:1}}}}
@keyframes rot{{to{{transform:rotate(45deg)}}}}
@keyframes pulse{{0%,100%{{opacity:1}}50%{{opacity:.35}}}}
@keyframes tap{{0%,100%{{transform:scale(1)}}50%{{transform:scale(.94)}}}}
@keyframes clk{{0%{{content:''}}}}"""
    W,Hh,L,T=620,1180,230,560
    def shell(inner,t0):
        return f'<div class="abs" style="left:{L}px;top:{T}px;width:{W}px;height:{Hh}px;{A(("rise",.6,t0))}"><div style="width:100%;height:100%;border-radius:70px;padding:18px;background:#1A1D24;box-shadow:0 0 0 3px #2A2E38,0 40px 120px rgba(109,18,32,.45)"><div style="width:100%;height:100%;border-radius:54px;overflow:hidden;background:#FFFFFF;position:relative">{inner}</div></div></div>'
    # chat
    head=f'<div style="height:130px;display:flex;align-items:flex-end;gap:18px;padding:0 30px 22px;background:#F1ECEA;border-bottom:2px solid {LN}"><div style="width:62px;height:62px;border-radius:31px;background:{BEG};display:flex;align-items:center;justify-content:center;font-family:Outfit;font-weight:700;font-size:28px;color:{BOR}">DL</div><div><div style="font-family:Outfit;font-weight:700;font-size:32px;color:{PRE}">Doceria Lume</div><div style="font-family:Inter;font-size:22px;color:#5A5C66">visto por último hoje às 18h</div></div></div>'
    msgs=[("Oi! Vocês fazem bolo para 30 pessoas?","21:04",3.6),("Qual o prazo para encomendar?","21:05",4.3),("Entregam no meu bairro?","21:05",5.0),("Aceita Pix?","21:06",5.7)]
    bl=""
    for txt,h,t in msgs:
        bl+=f'<div style="align-self:flex-end;max-width:470px;background:#E9DCD8;border-radius:26px 26px 6px 26px;padding:22px 26px;font-family:Inter;font-size:32px;line-height:1.35;color:{PRE};animation:bub .35s ease {t}s both">{txt}<div style="font-family:Inter;font-size:19px;color:#5A5C66;text-align:right;margin-top:6px">{h} ✓✓</div></div>'
    wait=f'<div style="align-self:center;margin-top:16px;background:#F9E3E1;color:#B3261E;font-family:Outfit;font-weight:600;font-size:26px;border-radius:999px;padding:14px 26px;{A(("pop",.5,6.6))}"><span style="display:inline-block;animation:pulse 1s ease 7.1s 3">Sem resposta há 2 horas</span></div>'
    chat=head+f'<div style="padding:30px 26px;display:flex;flex-direction:column;gap:18px">{bl}{wait}</div>'
    # site com FAQ
    shead=f'<div style="height:130px;display:flex;align-items:flex-end;justify-content:space-between;padding:0 34px 24px;border-bottom:2px solid {LN}"><div style="font-family:Outfit;font-weight:700;font-size:34px;color:{PRE}">Doceria Lume</div><div style="font-family:Inter;font-weight:600;font-size:22px;color:{BOR}">Encomendar</div></div>'
    faq=[("Para quantas pessoas?","Bolos de 10 a 60 fatias. Veja os tamanhos na página de cardápio.",10.3),("Qual o prazo?","Encomendas com 3 dias de antecedência.",11.2),("Vocês entregam?","Sim. A taxa aparece ao digitar o seu CEP.",12.1),("Como posso pagar?","Pix ou cartão, direto no pedido.",13.0)]
    fq=""
    for q,a,t in faq:
        fq+=f'<div style="border:2px solid {LN};border-radius:22px;padding:22px 26px;animation:tap .3s ease {t-.15}s both"><div style="display:flex;justify-content:space-between;align-items:center;font-family:Outfit;font-weight:600;font-size:34px;color:{PRE}">{q}<span style="font-size:40px;color:{BOR};display:inline-block;animation:rot .3s ease {t}s both">+</span></div><div style="overflow:hidden;font-family:Inter;font-size:28px;line-height:1.4;color:#3A3C44;animation:open .45s ease {t}s both"><div style="padding-top:12px">{a}</div></div></div>'
    btn=f'<div style="margin-top:6px;background:{BOR};color:#fff;font-family:Outfit;font-weight:600;font-size:30px;border-radius:999px;padding:24px 0;text-align:center;{A(("pop",.5,14.0))}">Fazer minha encomenda</div>'
    site=shead+f'<div style="padding:30px 30px;display:flex;flex-direction:column;gap:16px"><div style="font-family:Outfit;font-weight:600;font-size:22px;letter-spacing:4px;color:{BOR}">PERGUNTAS FREQUENTES</div>{fq}{btn}</div>'
    body=tag("ATENDIMENTO · SIMULAÇÃO",BEG)
    body+=scene(0,2.9,f'<div class="abs" style="left:90px;right:90px;top:600px">'+R(.1,f'<div style="{H(124)}">“Oi, quanto {ACC("custa?")}”</div>')+R(.8,"Quantas vezes por dia você responde isso no WhatsApp?",P+";font-size:50px;margin-top:44px")+'</div>')
    lab=lambda t0,a,b: f'<div class="abs" style="left:90px;right:90px;top:290px">'+R(t0,f'<div style="{H(78)}">{a}</div>')+R(t0+.25,b,P+";font-size:38px;margin-top:16px")+'</div>'
    body+=scene(3.0,8.9,lab(3.1,f'Ele pergunta. E {ACC("espera.")}',"21h, você já fechou. A resposta só sai amanhã.")+shell(chat,3.2))
    body+=scene(9.0,15.6,lab(9.1,f'No site, ela já está {ACC("lá.")}',"Serviços e perguntas frequentes, a qualquer hora.")+shell(site,9.2))
    body+=f'<div class="abs" style="inset:0;background:{BOR};{A(("wipe",.6,15.7),("fadeout",.3,19.6))}"><div class="abs" style="left:90px;right:90px;top:600px">'+R(16.1,f'<div style="{H(104)}">Menos perguntas repetidas para você. Mais cliente {ACC("decidido.")}</div>')+R(17.0,"O WhatsApp continua lá, mas a conversa já chega pronta para fechar.",P+";color:#E9DCD8;margin-top:40px")+'</div></div>'
    body+=endcard(19.8,'Seu site pode responder <span class="acc" style="color:#E9DCD8">por você.</span>',"Comente SITE · a gente te chama")
    return page(body,css),23.0

async def main(which):
    for name in which:
        html,dur=globals()["reel"+name]()
        await render(html,OUT/f"reel{name}.mp4",dur,stills=[(x,f"reel{name}_{x}.png") for x in (1.2,2.5,4.5,7.5,10.5,12.5,14.5,17.5,dur-0.4)])
if __name__=='__main__': OUT.mkdir(parents=True,exist_ok=True); asyncio.run(main(sys.argv[2:]))
