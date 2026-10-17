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

async def main(which):
    for name in which:
        html,dur=globals()["reel"+name]()
        await render(html,OUT/f"reel{name}.mp4",dur,stills=[(t,f"reel{name}_{t}.png") for t in (2.0,7.0,dur-0.5)])
if __name__=='__main__': OUT.mkdir(parents=True,exist_ok=True); asyncio.run(main(sys.argv[2:]))
