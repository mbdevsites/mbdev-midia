"""Semana 3: Reel de terça (o site da MBDev, seção por seção) e Reel de quinta em versão animada (dúvidas respondidas na tela do computador).
Uso: python3 semana03_reels.py <pasta_saida> S3b S3d"""
import sys, asyncio, pathlib
from reel import *
OUT=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(".")
BOR,BEG,BEC,PRE,LN="#6D1220","#E9DCD8","#F5EFED","#080C14","#D9C9C4"

def reelS3b():
    """Tour pelas seções do site da MBDev. As telas do celular são ilustrações com o conteúdo real de cada seção
    (serviços, portfólio com prints reais, etapas e contato). Trocar por prints do site quando a fundadora enviar."""
    css=f".stage{{background:{PRE}}}@keyframes inR{{from{{opacity:0;transform:translateX(380px) rotate(6deg)}}to{{opacity:1;transform:none}}}}@keyframes outL{{from{{opacity:1;transform:none}}to{{opacity:0;transform:translateX(-380px) rotate(-6deg)}}}}"
    W,H=520,1000
    def shell(inner):
        return f'<div style="width:{W}px;height:{H}px;border-radius:70px;padding:18px;background:#1A1D24;box-shadow:0 40px 90px rgba(0,0,0,.45),0 0 0 3px #2A2E38"><div style="width:100%;height:100%;border-radius:54px;overflow:hidden;background:#FFFFFF;display:flex;flex-direction:column"><div style="height:110px;flex:none;display:flex;align-items:flex-end;justify-content:space-between;padding:0 36px 20px;border-bottom:2px solid {LN}"><img src="{LOGO_B}" style="height:52px"><div style="display:flex;flex-direction:column;gap:7px"><span style="width:38px;height:4px;background:{PRE};border-radius:2px"></span><span style="width:38px;height:4px;background:{PRE};border-radius:2px"></span><span style="width:38px;height:4px;background:{PRE};border-radius:2px"></span></div></div><div style="flex:1;padding:40px 36px;display:flex;flex-direction:column;gap:22px;overflow:hidden">{inner}</div></div></div>'
    K=lambda x: f'<div style="font-family:Outfit;font-weight:600;font-size:18px;letter-spacing:4px;color:{BOR}">{x}</div>'
    Hh=lambda x,s=44: f'<div style="font-family:Outfit;font-weight:700;font-size:{s}px;line-height:1.05;letter-spacing:-1px;color:{PRE}">{x}</div>'
    bar=lambda w,c="#E4D8D4",h=14: f'<div style="width:{w};height:{h}px;border-radius:7px;background:{c}"></div>'
    btn=lambda x,bg=BOR: f'<div style="align-self:flex-start;background:{bg};color:#fff;font-family:Outfit;font-weight:600;font-size:22px;border-radius:999px;padding:16px 28px">{x}</div>'
    screens=[
      ("01 · INÍCIO","Em segundos, você entende o que <span class=acc style='color:#E9DCD8'>fazemos.</span>",
       K("CRIAÇÃO DE SITES")+Hh('Sites bonitos, rápidos e feitos para virar <span class=acc style="color:#6D1220">cliente.</span>',46)+bar("90%")+bar("70%")+btn("Peça seu orçamento")+f'<div style="flex:1;border-radius:26px;background:{BEG};margin-top:8px"></div>'),
      ("02 · SERVIÇOS","Cada serviço explicado, sem <span class=acc style='color:#E9DCD8'>jargão.</span>",
       K("SERVIÇOS")+"".join(f'<div style="border:2px solid {LN};border-radius:22px;padding:22px 24px;display:flex;flex-direction:column;gap:12px"><div style="font-family:Outfit;font-weight:600;font-size:28px;color:{PRE}">{s}</div>{bar("80%",h=10)}</div>' for s in ["Sites institucionais","Landing pages","Sistemas de agendamento","Google Business"])),
      ("03 · PORTFÓLIO","Projetos reais para você ver antes de <span class=acc style='color:#E9DCD8'>decidir.</span>",
       K("PORTFÓLIO")+Hh("Projetos",40)+'<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">'+"".join(f'<div style="height:300px;border-radius:20px;overflow:hidden;background:{BEC}"><img src="file://{ASSETS}/{i}.jpg" style="width:100%;display:block"></div>' for i in ["barbearia","pediatra","croche","advocacia"])+'</div>'),
      ("04 · COMO FUNCIONA","Do primeiro oi ao site no ar, em 4 <span class=acc style='color:#E9DCD8'>etapas.</span>",
       K("COMO FUNCIONA")+"".join(f'<div style="display:flex;gap:18px;align-items:baseline;padding:20px 0;border-top:2px solid {LN}"><span style="font-family:Outfit;font-weight:700;font-size:26px;color:{BOR}">{n}</span><span style="font-family:Outfit;font-weight:600;font-size:28px;color:{PRE}">{x}</span></div>' for n,x in [("01","Conversa sobre seu negócio"),("02","Planejamento da estrutura"),("03","Design e desenvolvimento"),("04","Site no ar, com suporte")])),
      ("05 · CONTATO","Orçamento pelo WhatsApp, em um <span class=acc style='color:#E9DCD8'>toque.</span>",
       K("CONTATO")+Hh('Vamos conversar sobre o seu <span class=acc style="color:#6D1220">projeto?</span>',44)+bar("85%")+bar("60%")+'<div style="flex:1"></div>'+f'<div style="background:#25A55F;color:#fff;font-family:Outfit;font-weight:600;font-size:28px;border-radius:999px;padding:26px;text-align:center">Chamar no WhatsApp</div>'),
    ]
    body=tag("PORTFÓLIO · NOSSO PRÓPRIO SITE",BEG)
    body+=f'<div class="abs" style="inset:0;{A(("fadeout",.35,2.9))}">'+headline(["O site da MBDev,",'tela por <span class="acc" style="color:#E9DCD8">tela.</span>'],"#fff",760,108,extra="text-align:center")+'</div>'
    T0,D=3.2,2.6
    for i,(lab,line,inner) in enumerate(screens):
        t=T0+i*D; last=i==len(screens)-1
        out=() if last else (("outL",.45,t+D-.35,"cubic-bezier(.6,0,.8,.4)"),)
        body+=f'<div class="abs" style="left:280px;top:700px;{A(("inR",.55,t),*out)}">{shell(inner)}</div>'
        fade=A(("rise",.55,t+.1),*(() if last else (("fadeout",.3,t+D-.35),)))
        body+=f'<div class="abs" style="left:90px;right:90px;top:330px;{fade}"><div class="tag" style="color:#E9DCD8;opacity:.85">{lab}</div><div class="h" style="font-size:76px;color:#fff;margin-top:22px">{line}</div></div>'
    end=T0+len(screens)*D+.2
    body+=endcard(end,'Feito com o mesmo cuidado que o <span class="acc" style="color:#E9DCD8">seu</span> vai ter.',"Veja o site ao vivo · link na bio")
    return page(body,css),end+3.2

def reelS3d():
    """Bastidores sem rosto, versão animada: as dúvidas aparecem digitadas num documento na tela do notebook e as respostas em primeira pessoa."""
    css=f".stage{{background:{BEC}}}@keyframes blink{{0%,49%{{opacity:1}}50%,100%{{opacity:0}}}}"
    def scene(t0,t1,inner,top):
        out=(("fadeout",.35,t1),) if t1 else ()
        return f'<div class="abs" style="left:0;right:0;top:{top}px;{A(("fade",.01,t0),*out)}">{inner}</div>'
    def R(t,html,extra=""): return f'<div style="{A(("rise",.6,t))}{extra}">{html}</div>'
    def typed(t,text,step=.06):
        ws=text.split(" ")
        spans=" ".join(f'<span style="{A(("fade",.05,t+i*step))}">{w}</span>' for i,w in enumerate(ws))
        return spans+f'<span style="display:inline-block;width:5px;height:58px;background:{BOR};margin-left:8px;vertical-align:-8px;animation:blink 1s steps(1) infinite"></span>', t+len(ws)*step
    # notebook
    def laptop(inner):
        return f'''<div style="margin:0 auto;width:960px"><div style="background:#1A1D24;border-radius:34px 34px 0 0;padding:26px 26px 30px"><div style="background:#FFFFFF;border-radius:12px;height:600px;overflow:hidden;display:flex;flex-direction:column"><div style="height:56px;flex:none;background:#F1ECEA;display:flex;align-items:center;gap:12px;padding:0 24px;border-bottom:2px solid {LN}"><span style="width:16px;height:16px;border-radius:8px;background:#E0675B"></span><span style="width:16px;height:16px;border-radius:8px;background:#E8B64C"></span><span style="width:16px;height:16px;border-radius:8px;background:#5CB85C"></span><span style="margin-left:22px;font-family:Inter;font-size:22px;color:#5A5C66">duvidas-frequentes.doc</span></div><div style="flex:1;padding:48px 56px">{inner}</div></div></div><div style="height:34px;background:#2A2E38;border-radius:0 0 40px 40px;margin:0 -50px"></div></div>'''
    TAG=lambda x: f'<div class="tag" style="color:{BOR}">{x}</div>'
    body=tag("BASTIDORES · DÚVIDAS FREQUENTES",BOR)
    body+=scene(0,3.0,f'<div style="padding:0 90px">'+R(.2,f'<div class="h" style="font-size:118px;color:{PRE}">As dúvidas que eu mais <span class="acc" style="color:{BOR}">escuto.</span></div>')+R(.8,"Abri o computador e respondi uma por uma.",f"font-family:Inter;font-size:42px;line-height:1.4;color:#3A3C44;margin-top:34px")+'</div>',700)
    QA=[("Vocês atendem a minha cidade?",'Atendo o Brasil <span class="acc" style="color:#6D1220">inteiro.</span>',"Tudo é feito online, do primeiro oi à entrega do site."),
        ("Depois de pronto, consigo mexer sozinho?",'Consegue, <span class="acc" style="color:#6D1220">sim.</span>',"O site é feito em WordPress e você recebe orientação para trocar textos e fotos sem programar."),
        ("E depois que o site vai ao ar?",'Eu continuo por <span class="acc" style="color:#6D1220">perto.</span>',"O suporte segue depois da entrega. Você não fica sozinho com o site.")]
    t=3.3; D=4.2
    for i,(q,a,sub) in enumerate(QA):
        tq,tend=typed(t+.6,q)
        doc=f'<div style="font-family:Outfit;font-weight:600;font-size:22px;letter-spacing:4px;color:{BOR}">PERGUNTA {i+1} DE {len(QA)}</div><div style="font-family:Outfit;font-weight:700;font-size:56px;line-height:1.15;color:{PRE};margin-top:26px">{tq}</div>'
        ans=R(tend+.3,f'<div class="h" style="font-size:84px;color:{PRE}">{a}</div>')+R(tend+.6,sub,"font-family:Inter;font-size:40px;line-height:1.4;color:#3A3C44;margin-top:24px")
        body+=scene(t,t+D-.35,R(t,laptop(doc))+f'<div style="padding:0 90px;margin-top:80px">{ans}</div>',330)
        t+=D
    body+=scene(t,None,f'<div style="padding:0 90px">'+R(t+.1,f'<div class="h" style="font-size:112px;color:{PRE}">Ficou com outra <span class="acc" style="color:{BOR}">dúvida?</span></div>')+R(t+.6,"Deixe nos comentários. Eu respondo todas.","font-family:Inter;font-size:42px;line-height:1.4;color:#3A3C44;margin-top:34px")+'</div>',720)
    body+=endcard(t+2.6,'Seu site começa com uma <span class="acc" style="color:#E9DCD8">conversa.</span>')
    return page(body,css),t+5.8

async def main(which):
    for name in which:
        html,dur=globals()["reel"+name]()
        await render(html,OUT/f"reel{name}.mp4",dur,stills=[(x,f"reel{name}_{x}.png") for x in (2.5,5.0,7.0,9.5,11.5,14.0,16.0,18.5,dur-0.5) if x<dur])
if __name__=='__main__': OUT.mkdir(parents=True,exist_ok=True); asyncio.run(main(sys.argv[2:]))
