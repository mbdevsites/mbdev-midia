import sys, asyncio
sys.path.insert(0,"/tmp/claude-0/-home-claude/bcb47e16-b548-5c1b-88da-de6f355698a0/scratchpad/reels")
from engine import page, render, S
R=S/"render"; OUT=S/"reels"
E="cubic-bezier(.2,.8,.2,1)"
def A(*xs): return "animation:"+",".join(f"{n} {d}s {e or E} {t}s {'forwards' if n in ('outL','fadeout') and i>0 else 'both'}" for i,(n,d,t,e) in enumerate([(x+(None,))[:4] for x in xs]))+";"
LOGO_W=f"file://{S}/logo/logo-branco.png"; LOGO_B=f"file://{S}/logo/logo-bordo.png"
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
    return kf, f'<div class="abs" style="left:{left}px;top:{top}px;width:{w}px;height:{h}px;transform:rotate({rot}deg);{anim}"><div class="phone" style="width:100%;height:100%;background:{frame};box-shadow:0 40px 90px rgba(0,0,0,.35),0 0 0 3px #2A2E38"><div class="screen"><img src="file://{R}/{img}.jpg" style="animation:{css_id} {pd}s cubic-bezier(.45,0,.35,1) {pt}s both"></div></div></div>'

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

def reel8():
    kf,ph=phone("barbearia",300,700,500,"#1A1D24",A(("rise",1.0,.9)),rot=4)
    body=tag("PROJETO · BARBEARIA","#E9DCD8")+headline(["Um corte premium","pede um site",'<span class="acc" style="color:#E9DCD8">à altura.</span>'],"#fff",300,96)+ph
    body+=chip("Agendamento em um toque","left:60px;top:880px",3.0)
    body+=chip("WhatsApp direto","right:60px;top:1210px",4.4)
    body+=chip("Experiência premium","left:60px;top:1470px",5.8)
    body+=endcard(9.4,'Seu negócio também merece um site <span class="acc" style="color:#E9DCD8">à altura.</span>')
    return page(body,kf+".stage{background:#080C14}"),12.5

def reel6():
    kf,ph=phone("pediatra",90,700,500,"#080C14",A(("rise",1.0,.9)),rot=-4)
    body=tag("PROJETO · CLÍNICA PEDIÁTRICA","#6D1220")+headline(["A confiança começa",'<span class="acc" style="color:#6D1220">antes</span> da primeira','consulta.'],"#080C14",300,96)+ph
    body+=chip("Acolhedor para as famílias","right:60px;top:980px",3.0)
    body+=chip("Agendamento pelo WhatsApp","right:60px;top:1200px",4.4)
    body+=chip("Perfeito no celular","right:60px;top:1420px",5.8)
    body+=endcard(9.4,'Seu paciente também procura <span class="acc" style="color:#E9DCD8">antes</span> de marcar.')
    return page(body,kf+".stage{background:#E9DCD8}"),12.5

def reel3():
    segs=[("barbearia","Barbearia premium","Agendamento em um toque."),("pediatra","Clínica pediátrica","Acolhimento que gera confiança."),("croche","Curso de crochê","Landing page feita para vender."),("advocacia","Escritório de advocacia","Autoridade desde a primeira tela.")]
    css=".stage{background:#080C14}@keyframes inR{from{opacity:0;transform:translateX(420px) rotate(8deg)}to{opacity:1;transform:none}}@keyframes outL{from{opacity:1;transform:none}to{opacity:0;transform:translateX(-420px) rotate(-8deg)}}"
    body=tag("PORTFÓLIO","#E9DCD8")
    body+=f'<div class="abs" style="left:0;right:0;top:0;bottom:0;{A(("fadeout",.4,1.9))}">'+headline(["4 negócios diferentes.",'O mesmo <span class="acc" style="color:#E9DCD8">cuidado.</span>'],"#fff",700,92,extra="text-align:center")+'</div>'
    T0,D=2.2,2.3
    for i,(img,name,line) in enumerate(segs):
        t=T0+i*D; last=i==len(segs)-1
        out=() if last else (("outL",.5,t+D-.35,"cubic-bezier(.6,0,.8,.4)"),)
        kf,ph=phone(img,290,640,500,"#1A1D24",A(("inR",.6,t),*out),pan=(1.0,1.08,0,-6,t,D+.4))
        css+=kf
        fade=A(("rise",.6,t+.1),*(() if last else (("fadeout",.3,t+D-.35),)))
        body+=f'<div class="abs" style="left:90px;right:90px;top:330px;{fade}"><div class="tag" style="color:#E9DCD8;opacity:.8">0{i+1} / 04</div><div class="h" style="font-size:80px;color:#fff;margin-top:22px">{name}</div><div style="font-family:Inter;font-size:38px;color:#E9DCD8;margin-top:16px">{line}</div></div>'
        body+=ph
    body+=endcard(T0+4*D+.3,'O próximo projeto<br>pode ser o <span class="acc" style="color:#E9DCD8">seu.</span>')
    return page(body,css),T0+4*D+3.3

def reelS1b():
    kf,ph=phone("advocacia",300,700,500,"#1A1D24",A(("rise",1.0,.9)))
    body=tag("PROJETO · ADVOCACIA","#E9DCD8")+headline(["Quem procura advogado",'procura <span class="acc" style="color:#E9DCD8">confiança.</span>'],"#fff",300,96)+ph
    body+=chip("Autoridade na primeira tela","left:60px;top:900px",3.0)
    body+=chip("Contato em um toque","right:60px;top:1210px",4.4)
    body+=chip("Visual sóbrio e profissional","left:60px;top:1470px",5.8)
    body+=endcard(9.4,'Seu escritório também merece ser <span class="acc" style="color:#E9DCD8">encontrado.</span>')
    return page(body,kf+".stage{background:#080C14}"),12.5

def reelS1d():
    BG,FG,AC,SUB="#F5EFED","#080C14","#6D1220","#3A3C44"
    def scene(t0,t1,inner,top=720):
        out=(("fadeout",.4,t1),) if t1 else ()
        return f'<div class="abs" style="left:90px;right:90px;top:{top}px;{A(("fade",.01,t0),*out)}">{inner}</div>'
    def R(t,html,extra=""): return f'<div style="{A(("rise",.7,t))}{extra}">{html}</div>'
    H=lambda sz: f"font-family:Outfit;font-weight:700;font-size:{sz}px;letter-spacing:-3px;line-height:1.04;color:{FG}"
    P=f"font-family:Inter;font-size:40px;line-height:1.4;color:{SUB};margin-top:36px"
    body=tag("BASTIDORES · QUEM SOMOS",AC)
    body+=scene(0,3.1,R(.2,f'<div style="{H(150)}">Prazer,<br><span class="acc" style="color:{AC}">MBDev.</span></div>')+R(.8,"Criamos sites em WordPress para negócios que querem ser encontrados.",P))
    body+=scene(3.5,7.0,R(3.6,f'<div class="tag" style="color:{AC}">NOSSO OBJETIVO</div>')+R(3.9,f'<div style="{H(100)};margin-top:30px">Fazer a tecnologia e o design trabalharem a favor do seu <span class="acc" style="color:{AC}">negócio.</span></div>'))
    items="".join(R(7.8+i*.45,f'<div style="{H(110)};padding:18px 0;border-bottom:3px solid #D9C9C4">{w}</div>') for i,w in enumerate(["Rápidos.","Responsivos.","Fáceis de gerenciar."]))
    body+=scene(7.4,11.4,R(7.5,f'<div class="tag" style="color:{AC}">SITES QUE SÃO</div>')+f'<div style="margin-top:20px">{items}</div>'+R(9.4,"Você atualiza textos e fotos sem precisar programar.",P),top=640)
    steps=[("01","Entender o seu negócio"),("02","Planejar a estrutura"),("03","Design e desenvolvimento"),("04","Lançamento com SEO e orientação")]
    st="".join(R(12.2+i*.5,f'<div style="display:flex;gap:30px;align-items:baseline;padding:26px 0;border-top:3px solid #D9C9C4"><span style="font-family:Outfit;font-weight:700;font-size:56px;color:{AC}">{n}</span><span style="font-family:Outfit;font-weight:600;font-size:56px;color:{FG}">{x}</span></div>') for i,(n,x) in enumerate(steps))
    body+=scene(11.8,15.8,R(11.9,f'<div class="tag" style="color:{AC}">COMO TRABALHAMOS</div>')+f'<div style="margin-top:24px">{st}</div>'+R(14.2,"Você acompanha cada etapa e pode sugerir ajustes.",P),top=640)
    vals="".join(R(16.4+i*.45,f'<div style="{H(96)};margin-bottom:22px">{v}</div>') for i,v in enumerate(['Atenção aos <span class="acc" style="color:#6D1220">detalhes.</span>','Comunicação <span class="acc" style="color:#6D1220">transparente.</span>','Compromisso com a <span class="acc" style="color:#6D1220">qualidade.</span>']))
    body+=scene(16.2,None,vals,top=760)
    body+=endcard(19.4,'Seu negócio merece ser <span class="acc" style="color:#E9DCD8">encontrado.</span>')
    return page(body,f".stage{{background:{BG}}}"),22.5

def reelS2b():
    kf,ph=phone("croche",290,720,500,"#1A1D24",A(("rise",1.0,.7)))
    body=tag("PROJETO · CURSO ONLINE","#E9DCD8")+headline(["Uma página.","Um objetivo:",'<span class="acc" style="color:#E9DCD8">vender.</span>'],"#fff",300,100,t0=.15,step=.18)+ph
    body+=chip("Contagem regressiva que gera urgência","left:50px;top:900px",2.8)
    body+=chip("Uma única ação: comprar","right:50px;top:1220px",4.2)
    body+=chip("Perfeita no celular","left:50px;top:1480px",5.6)
    body+=endcard(9.4,'Seu próximo lançamento merece uma página que <span class="acc" style="color:#E9DCD8">vende.</span>',"Fale com a gente · link na bio")
    return page(body,kf+".stage{background:#080C14}"),12.5

def reelS2d():
    BG,FG,AC,SUB,LN="#F5EFED","#080C14","#6D1220","#3A3C44","#D9C9C4"
    css=f".stage{{background:{BG}}}@keyframes grow{{from{{transform:scaleX(0)}}to{{transform:scaleX(1)}}}}"
    def scene(t0,t1,inner,top=560):
        out=(("fadeout",.35,t1),) if t1 else ()
        return f'<div class="abs" style="left:90px;right:90px;top:{top}px;{A(("fade",.01,t0),*out)}">{inner}</div>'
    def Rv(t,html,extra=""): return f'<div style="{A(("rise",.6,t))}{extra}">{html}</div>'
    H=lambda sz: f"font-family:Outfit;font-weight:700;font-size:{sz}px;letter-spacing:-3px;line-height:1.04;color:{FG}"
    P=f"font-family:Inter;font-size:40px;line-height:1.4;color:{SUB};margin-top:30px"
    def step(t,n,name,title,sub,visual):
        return Rv(t,f'<div class="tag" style="color:{AC}">PASSO {n} · {name}</div>')+Rv(t+.2,f'<div style="{H(104)};margin-top:26px">{title}</div>')+Rv(t+.45,sub,P)+f'<div style="margin-top:70px">{visual}</div>'
    body=tag("BASTIDORES · UM DIA DE TRABALHO",AC)
    body+=scene(0,2.7,Rv(.1,f'<div style="{H(132)};white-space:nowrap">Um dia criando<br>um <span class="acc" style="color:{AC}">site.</span></div>')+Rv(.5,"Do rascunho ao ar, em poucos passos.",P),top=720)
    # 1 briefing: checklist
    chk="".join(Rv(4.0+i*.35,f'<div style="display:flex;gap:24px;align-items:center;padding:22px 0;border-top:3px solid {LN};font-family:Outfit;font-weight:600;font-size:50px;color:{FG}"><span style="width:44px;height:44px;border-radius:12px;background:{AC};color:#fff;font-size:30px;display:flex;align-items:center;justify-content:center">✓</span>{x}</div>') for i,x in enumerate(["Quem é o seu cliente","O que você oferece","Qual ação ele deve tomar"]))
    body+=scene(3.0,6.6,step(3.1,"01","BRIEFING",'Entender o <span class="acc" style="color:#6D1220">negócio.</span>',"Antes de qualquer tela, a conversa.",chk))
    # 2 estrutura: wireframe
    box=lambda t,h,w="100%",bg="#E9DCD8": f'<div style="height:{h}px;width:{w};background:{bg};border-radius:18px;margin-bottom:18px;{A(("pop",.45,t))}"></div>'
    wf=f'<div style="background:#fff;border:3px solid {LN};border-radius:30px;padding:30px;width:640px">'+box(7.6,60)+box(7.85,200,bg="#D9C9C4")+'<div style="display:flex;gap:18px">'+box(8.1,140,"33%")+box(8.25,140,"33%")+box(8.4,140,"33%")+'</div>'+box(8.65,70,"55%",AC)+'</div>'
    body+=scene(6.9,10.6,step(7.0,"02","ESTRUTURA",'Planejar o <span class="acc" style="color:#6D1220">caminho.</span>',"Cada página leva o visitante até o contato.",wf))
    # 3 design: swatches + fonts
    sw="".join(f'<div style="width:130px;height:130px;border-radius:65px;background:{c};border:3px solid {LN};{A(("pop",.45,11.6+i*.2))}"></div>' for i,c in enumerate(["#6D1220","#080C14","#E9DCD8","#FFFFFF"]))
    dz=f'<div style="display:flex;gap:28px">{sw}</div>'+Rv(12.6,f'<div style="display:flex;gap:50px;align-items:baseline;margin-top:50px"><span style="font-family:Outfit;font-weight:700;font-size:110px;color:{FG}">Aa</span><span class="acc" style="font-size:110px;color:{AC}">Aa</span></div>')
    body+=scene(10.9,14.6,step(11.0,"03","DESIGN",'A cara da sua <span class="acc" style="color:#6D1220">marca.</span>',"Cores, fontes e imagens que combinam com você.",dz))
    # 4 desenvolvimento: progress bars
    bars="".join(Rv(15.5+i*.3,f'<div style="font-family:Outfit;font-weight:600;font-size:44px;color:{FG};margin-top:28px">{x}</div><div style="height:22px;background:#E9DCD8;border-radius:11px;margin-top:14px;overflow:hidden"><div style="height:100%;width:100%;background:{AC};transform-origin:left;{A(("grow",1.1,15.7+i*.3))}"></div></div>') for i,x in enumerate(["Velocidade","Responsividade","SEO"]))
    body+=scene(14.9,18.6,step(15.0,"04","DESENVOLVIMENTO",'Tudo em <span class="acc" style="color:#6D1220">WordPress.</span>',"Rápido, responsivo e fácil de atualizar.",bars))
    # 5 no ar
    dev="".join(f'<div style="border:6px solid {FG};border-radius:{r}px;width:{w}px;height:{h}px;background:#fff;{A(("pop",.5,19.6+i*.25))}"></div>' for i,(w,h,r) in enumerate([(160,300,34),(260,350,30),(440,290,20)]))
    body+=scene(18.9,None,step(19.0,"05","NO AR",'Testado em todo <span class="acc" style="color:#6D1220">dispositivo.</span>',"Celular, tablet e computador. E você recebe orientação de uso.",f'<div style="display:flex;gap:30px;align-items:flex-end">{dev}</div>'))
    body+=endcard(22.6,'Quer ver o seu site <span class="acc" style="color:#E9DCD8">nascer?</span>',"Peça seu orçamento · link na bio")
    return page(body,css),25.6

async def main(which):
    for name in which:
        html,dur=globals()["reel"+name]()
        await render(html,OUT/f"reel{name}.mp4",dur,stills=[(t,f"reel{name}_{t}.png") for t in (2.0,7.0,dur-0.5)])
asyncio.run(main(sys.argv[1:]))
