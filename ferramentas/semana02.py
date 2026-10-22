"""Semana 2 (26 a 30/10/2026): carrosséis de segunda, quarta e sexta.
Uso: python3 semana02.py <pasta_saida>"""
import carrossel, pathlib, sys
from carrossel import *
carrossel.G=pathlib.Path(sys.argv[1]); carrossel.G.mkdir(parents=True,exist_ok=True)
G=carrossel.G

def custom(name,title,th,tag,page,inner,right=None):
    t=TH[th]
    (G/f"{name}.dc.html").write_text(wrap(title,t,head(t,tag,page)+inner,right if right is not None else swipe(t)))

# SEGUNDA · 5 sinais (light)
T="SEU SITE ESTÁ BEM?"; th="light"; a=TH[th]["acc"]
cover("S2a1","Seg · slide 1",th,T,"1/7",f"5 sinais de que seu site está perdendo {acc('clientes.',a)}","Confira um por um. O quarto pouca gente percebe.")
numbered("S2a2","Seg · slide 2",th,T,"2/7","01","Demora para abrir.","Mais da metade das visitas pelo celular é abandonada quando a página leva mais de 3 segundos para carregar, segundo o Google.")
numbered("S2a3","Seg · slide 3",th,T,"3/7","02","Fica estranho no celular.","Texto pequeno, botões apertados, precisa dar zoom. Um site responsivo se adapta sozinho a qualquer tamanho de tela.")
numbered("S2a4","Seg · slide 4",th,T,"4/7","03","O contato está escondido.","Se o cliente precisa procurar o telefone, ele desiste. Um botão de WhatsApp sempre à vista resolve.")
numbered("S2a5","Seg · slide 5",th,T,"5/7","04","Aparece “Não seguro” no navegador.","O Chrome mostra esse aviso em sites sem HTTPS, a proteção que aparece como um cadeado ao lado do endereço. Ninguém quer deixar seus dados ali.")
numbered("S2a6","Seg · slide 6",th,T,"6/7","05","Informações desatualizadas.","Horário antigo, serviço que você não oferece mais, “© 2019” no rodapé. O cliente fica na dúvida se a empresa ainda existe.")
cta("S2a7","Seg · slide 7",th,T,"7/7",f"Reconheceu algum {acc('sinal?',a)}","Conte nos comentários qual deles você encontrou no seu site. A gente responde com o caminho para resolver.","Salve para revisar com calma")

# QUARTA · Avaliações no Google (white)
T="GOOGLE E NEGÓCIO LOCAL"; th="white"; t=TH[th]; a=t["acc"]
cover("S2c1","Qua · slide 1",th,T,"1/7",f"Como pedir avaliações no Google sem {acc('constranger.',a)}","4 jeitos naturais de pedir e um erro que você precisa evitar.")
numbered("S2c2","Qua · slide 2",th,T,"2/7","01","Peça na hora certa.","Logo depois de um elogio ou de um serviço bem feito. É quando o cliente está mais disposto a ajudar.")
numbered("S2c3","Qua · slide 3",th,T,"3/7","02","Mande o link direto.","No seu Perfil da Empresa no Google, a opção de pedir avaliações gera um link e um QR code. Um toque e o cliente já cai na tela certa.")
bubble=f'''<div style="display: flex; flex-direction: column; gap: 36px"><div style="font-family: Outfit, sans-serif; font-weight: 700; font-size: 200px; line-height: 0.85; letter-spacing: -8px; color: {a}">03</div><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 84px; line-height: 1.04; letter-spacing: -2.5px; text-wrap: balance">Use uma mensagem pessoal.</h2><div style="align-self: flex-start; max-width: 820px; background: {t["card"]}; border: 2px solid {t["line"]}; border-radius: 36px 36px 36px 8px; padding: 36px 40px; font-size: 32px; line-height: 1.45; color: #080C14">Oi, Ana! Que bom que você gostou do atendimento. Se puder contar como foi no Google, ajuda muita gente a nos encontrar. É só tocar aqui: [link]</div><p style="margin: 0; font-size: 30px; line-height: 1.45; color: {t["sub"]}">Copie, troque o nome e mande pelo WhatsApp.</p></div>'''
custom("S2c4","Qua · slide 4",th,T,"4/7",bubble)
numbered("S2c5","Qua · slide 5",th,T,"5/7","04","Responda todas as avaliações.","Agradeça pelo nome nas positivas. Nas negativas, responda com calma e ofereça uma solução. Quem lê repara no cuidado.")
numbered("S2c6","Qua · slide 6",th,T,"6/7","!","Nunca ofereça nada em troca.","Desconto ou brinde em troca de avaliação é proibido pelas regras do Google. As avaliações podem ser removidas.")
cta("S2c7","Qua · slide 7",th,T,"7/7",f"Avaliação boa traz cliente {acc('novo.',a)}","Salve este post e mande para alguém que tem um negócio local.","Ajuda com o Google? Link na bio")

# SEXTA · Mito x verdade + análise gratuita (bordo)
T="MITO OU VERDADE?"; th="bordo"; t=TH[th]; a=t["acc"]
cover("S2e1","Sex · slide 1",th,T,"1/6",f"Site é caro e {acc('demora?',a)}","3 frases que ouvimos toda semana, e o que acontece de verdade.")
def pill(txt,bg,fg): return f'<div style="align-self: flex-start; font-family: Outfit, sans-serif; font-weight: 700; font-size: 26px; letter-spacing: 5px; padding: 12px 26px; border-radius: 999px; background: {bg}; color: {fg}">{txt}</div>'
def mito(name,title,page,frase,h2,body):
    inner=f'''<div style="display: flex; flex-direction: column; gap: 30px">{pill("MITO","transparent;border:2px solid rgba(233,220,216,0.6)",a)}<div style="font-family: Outfit, sans-serif; font-weight: 600; font-size: 60px; line-height: 1.1; color: {a}; opacity: 0.75; text-decoration: line-through; text-decoration-thickness: 4px">{frase}</div><div style="height: 2px; background: {t["line"]}; margin: 18px 0"></div>{pill("VERDADE","#FFFFFF","#6D1220")}<h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 84px; line-height: 1.04; letter-spacing: -2.5px; text-wrap: balance">{h2}</h2><p style="margin: 0; font-size: 34px; line-height: 1.45; color: {t["sub"]}; max-width: 860px">{body}</p></div>'''
    custom(name,title,th,T,page,inner)
mito("S2e2","Sex · slide 2","2/6","“Site é caro.”",f"Caro é não ser {acc('encontrado.',a)}","Cada cliente que procura no Google e acha o concorrente é uma venda perdida. O projeto é sob medida, com orçamento pensado para o seu momento.")
mito("S2e3","Sex · slide 3","3/6","“Demora meses para ficar pronto.”",f"Com etapas claras, o projeto {acc('anda.',a)}","O prazo é combinado já no orçamento, e você acompanha cada fase, do planejamento ao site no ar.")
mito("S2e4","Sex · slide 4","4/6","“Depois de pronto, não consigo mexer.”",f"Em WordPress, você mesmo {acc('atualiza.',a)}","WordPress é a plataforma em que criamos os sites: textos e fotos se trocam sem programar. E na entrega você recebe orientação de uso.")
chips="".join(f'<div style="background: {t["card"]}; border-radius: 24px; padding: 28px 32px; font-family: Outfit, sans-serif; font-weight: 600; font-size: 36px; color: #FFFFFF">{x}</div>' for x in ["Velocidade","Uso no celular","Google","Conversão"])
offer=f'''<div style="display: flex; flex-direction: column; gap: 40px">{pill("CONVITE","#FFFFFF","#6D1220")}<h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 96px; line-height: 1.02; letter-spacing: -3px; text-wrap: balance">Análise {acc('gratuita',a)} do seu site.</h2><div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px">{chips}</div><p style="margin: 0; font-size: 34px; line-height: 1.45; color: {t["sub"]}; max-width: 880px">Você manda o link e recebe de 3 a 5 melhorias. Ainda não tem site? Analisamos como o seu negócio aparece hoje na busca.</p></div>'''
custom("S2e5","Sex · slide 5",th,T,"5/6",offer)
cta("S2e6","Sex · slide 6",th,T,"6/6",f"Comente {acc('ANÁLISE',a)} aqui embaixo.","A gente te chama no direct. Se preferir, fale direto pelo link da bio. Sem compromisso.","Quero minha análise gratuita")
print("ok")
