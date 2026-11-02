"""Semana 3, versão 2 (pautas novas, 04 e 06/11/2026): notícia do Google na quarta e "Faça a conta" na sexta.
Uso: python3 semana03b.py <pasta_saida>"""
import carrossel, pathlib, sys
from carrossel import *
carrossel.G=pathlib.Path(sys.argv[1]); carrossel.G.mkdir(parents=True,exist_ok=True)
G=carrossel.G

def custom(name,title,th,tag,page,inner,right=None):
    t=TH[th]
    (G/f"{name}.dc.html").write_text(wrap(title,t,head(t,tag,page)+inner,right if right is not None else swipe(t)))

def fonte(t,txt): return f'<div style="font-size: 24px; line-height: 1.4; color: {t["pg"]}">{txt}</div>'

# QUARTA · Notícia: perfil completo no Google (white, modelo de notícia com número gigante)
T="NOTÍCIA DA SEMANA"; th="white"; t=TH[th]; a=t["acc"]
FT=fonte(t,"Fonte: Ajuda do Perfil da Empresa no Google, página “Complete your Business Profile on Google”.")
capa=f'''<div style="display: flex; flex-direction: column; gap: 40px"><div style="align-self: flex-start; font-family: Outfit, sans-serif; font-weight: 700; font-size: 26px; letter-spacing: 5px; padding: 12px 26px; border-radius: 999px; background: {a}; color: #FFFFFF">DADOS DO GOOGLE</div><h1 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 104px; line-height: 1.02; letter-spacing: -4px; text-wrap: balance">Perfil completo no Google atrai mais {acc('clientes.',a)}</h1><p style="margin: 0; font-size: 36px; line-height: 1.4; color: {t["sub"]}; max-width: 860px">Quem diz não somos nós. É o próprio Google.</p>{FT}</div>'''
custom("S3q1","Qua · slide 1",th,T,"1/5",capa)
def big(name,title,page,num,h2,body):
    inner=f'''<div style="display: flex; flex-direction: column; gap: 34px"><div style="font-family: Outfit, sans-serif; font-weight: 700; font-size: 300px; line-height: 0.85; letter-spacing: -14px; color: {a}">{num}</div><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 76px; line-height: 1.06; letter-spacing: -2.5px; text-wrap: balance">{h2}</h2><p style="margin: 0; font-size: 34px; line-height: 1.45; color: {t["sub"]}; max-width: 860px">{body}</p>{FT}</div>'''
    custom(name,title,th,T,page,inner)
big("S3q2","Qua · slide 2","2/5","2,7x",f"mais chance do cliente achar a sua empresa {acc('confiável.',a)}","Antes de ligar ou de ir até você, ele olha o perfil. Informação completa passa seriedade.")
big("S3q3","Qua · slide 3","3/5","70%",f"mais chance do cliente ir até {acc('você.',a)}","E 50% mais chance dele considerar comprar de você.")
chips="".join(f'<div style="background: {t["card"]}; border-radius: 22px; padding: 24px 28px; font-family: Outfit, sans-serif; font-weight: 600; font-size: 34px; color: #080C14">{x}</div>' for x in ["Serviços","Fotos e vídeos","Descrição","Horários e feriados","Link para avaliações","Link de agendamento"])
lista=f'''<div style="display: flex; flex-direction: column; gap: 40px"><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 84px; line-height: 1.04; letter-spacing: -2.5px; text-wrap: balance">O que o Google chama de {acc('completo',a)}</h2><div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px">{chips}</div><p style="margin: 0; font-size: 32px; line-height: 1.45; color: {t["sub"]}">Cada item que falta é uma pergunta que o cliente fica sem resposta.</p></div>'''
custom("S3q4","Qua · slide 4",th,T,"4/5",lista)
cta("S3q5","Qua · slide 5",th,T,"5/5",f"Quer saber o que falta no {acc('seu?',a)}","Comente GOOGLE que a gente te chama e mostra, sem compromisso.","Comente GOOGLE")

# SEXTA · Faça a conta: quanto custa não ter site (light + bordô, modelo de calculadora)
T="FAÇA A CONTA"; th="light"; t=TH[th]; a=t["acc"]
cover("S3s1","Sex · slide 1",th,T,"1/6",f"Quanto custa {acc('não',a)} ter um site?","Pegue papel e caneta. A conta é com os seus números e leva um minuto.")
def campo(rotulo,valor,ex):
    return f'''<div style="display: flex; flex-direction: column; gap: 14px"><div style="font-family: Outfit, sans-serif; font-weight: 600; font-size: 28px; letter-spacing: 3px; color: {a}">{rotulo}</div><div style="border: 4px dashed {a}; border-radius: 28px; padding: 34px 40px; font-family: Outfit, sans-serif; font-weight: 700; font-size: 72px; color: #080C14; background: #FFFFFF">{valor}</div><div style="font-size: 28px; line-height: 1.4; color: {t["pg"]}">{ex}</div></div>'''
def passo(name,title,page,n,h2,body,rotulo,valor,ex):
    inner=f'''<div style="display: flex; flex-direction: column; gap: 36px"><div style="font-family: Outfit, sans-serif; font-weight: 700; font-size: 30px; letter-spacing: 4px; color: {a}">PASSO {n} DE 3</div><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 84px; line-height: 1.04; letter-spacing: -2.5px; text-wrap: balance">{h2}</h2><p style="margin: 0; font-size: 32px; line-height: 1.45; color: {t["sub"]}; max-width: 880px">{body}</p>{campo(rotulo,valor,ex)}</div>'''
    custom(name,title,th,T,page,inner)
passo("S3s2","Sex · slide 2","2/6",1,f"Quanto vale um cliente {acc('novo?',a)}","Some tudo o que ele costuma gastar com você, não só a primeira compra.","VALOR DE UM CLIENTE","R$ ______","Exemplo: uma consulta de R$ 200 que vira mais 2 retornos dá R$ 600.")
passo("S3s3","Sex · slide 3","3/6",2,f"Quantos clientes você deixa {acc('passar?',a)}","Por mês, pense em quem procurou o seu serviço na internet e não te achou, ou achou e não entendeu o que você faz. Seja conservador.","CLIENTES PERDIDOS POR MÊS","______","Exemplo: 2 por mês.")
tb=TH["bordo"]
conta=f'''<div style="display: flex; flex-direction: column; gap: 40px"><div style="font-family: Outfit, sans-serif; font-weight: 700; font-size: 30px; letter-spacing: 4px; color: {tb["acc"]}">PASSO 3 DE 3</div><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 88px; line-height: 1.04; letter-spacing: -2.5px">{acc('Multiplique.',tb["acc"])}</h2><div style="display: flex; flex-direction: column; gap: 10px; font-family: Outfit, sans-serif; font-weight: 700"><div style="font-size: 64px; color: {tb["acc"]}">R$ 600 × 2</div><div style="font-size: 120px; line-height: 1; letter-spacing: -4px; color: #FFFFFF">R$ 1.200 por mês</div><div style="font-size: 52px; color: {tb["acc"]}; margin-top: 16px">R$ 14.400 em um ano</div></div><p style="margin: 0; font-size: 32px; line-height: 1.45; color: {tb["sub"]}; max-width: 880px">Os números do exemplo são ilustrativos. Faça a conta com os seus.</p></div>'''
custom("S3s4","Sex · slide 4","bordo",T,"4/6",conta)
custom("S3s5","Sex · slide 5",th,T,"5/6",f'''<div style="display: flex; flex-direction: column; gap: 40px"><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 96px; line-height: 1.04; letter-spacing: -3px; text-wrap: balance">Agora compare com o investimento em um {acc('site.',a)}</h2><p style="margin: 0; font-size: 36px; line-height: 1.45; color: {t["sub"]}; max-width: 880px">Ele é feito uma vez e trabalha todos os dias, até quando você está atendendo, dormindo ou de folga.</p></div>''')
cta("S3s6","Sex · slide 6",th,T,"6/6",f"Qual foi o seu {acc('resultado?',a)}","Comente SITE que a gente te ajuda a fazer essa conta para o seu negócio.","Comente SITE")
print("ok")
