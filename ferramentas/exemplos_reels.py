import sys, asyncio, pathlib
from reel import *
OUT=pathlib.Path(sys.argv[1]) if len(sys.argv)>1 else pathlib.Path(".")
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

async def main(which):
    for name in which:
        html,dur=globals()["reel"+name]()
        await render(html,OUT/f"reel{name}.mp4",dur,stills=[(t,f"reel{name}_{t}.png") for t in (2.0,7.0,dur-0.5)])
if __name__=='__main__': OUT.mkdir(parents=True,exist_ok=True); asyncio.run(main(sys.argv[2:]))
