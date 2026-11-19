"""Semana 6 (23 a 27/11/2026): carrosséis de segunda (site para quem tem 60+), quarta (Modo IA do Google) e sexta (Black Friday: página de campanha).
Uso: python3 semana06.py <pasta_saida>"""
import carrossel, pathlib, sys
from carrossel import *
carrossel.G=pathlib.Path(sys.argv[1]); carrossel.G.mkdir(parents=True,exist_ok=True)
G=carrossel.G
def A_(w,th): return acc(w,TH[th]["acc"])
def fonte(th,txt): return f'<div style="font-size: 24px; line-height: 1.4; color: {TH[th]["pg"]}">{txt}</div>'
def custom(name,title,th,tag,page,inner,right=None):
    t=TH[th]; (G/f"{name}.dc.html").write_text(wrap(title,t,head(t,tag,page)+inner,right if right is not None else swipe(t)))
def stat(name,title,th,tag,page,num,h2,body,src):
    t=TH[th]
    inner=f'<div style="display: flex; flex-direction: column; gap: 36px"><div style="font-family: Outfit, sans-serif; font-weight: 700; font-size: 250px; line-height: 0.85; letter-spacing: -10px; color: {t["acc"]}">{num}</div><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 80px; line-height: 1.05; letter-spacing: -2.5px; text-wrap: balance">{h2}</h2><p style="margin: 0; font-size: 34px; line-height: 1.45; color: {t["sub"]}; max-width: 860px">{body}</p>{fonte(th,src)}</div>'
    custom(name,title,th,tag,page,inner)

# SEGUNDA · Sua cliente de 60 anos consegue usar o seu site?
T="PARA SALVAR"
cover("S6a1","Seg · slide 1","light",T,"1/7",f"Sua cliente de 60 anos consegue usar o seu {A_('site?','light')}","4 testes rápidos para fazer hoje, no seu celular.")
stat("S6a2","Seg · slide 2","bordo",T,"2/7","74,5%",f"dos brasileiros com 60 anos ou {A_('mais','bordo')} usam a internet.","Muitos escolhem dentista, advogado e restaurante pelo celular. Se o site é difícil, eles desistem e ligam para outro.","Fonte: IBGE, PNAD Contínua TIC 2025, divulgada em 02/07/2026.")
numbered("S6a3","Seg · slide 3","white",T,"3/7","01",f"Dá para ler sem {A_('zoom?','white')}","Abra o site no celular, com o braço esticado. Se você precisar aproximar a tela para ler, ela também vai precisar. Letra grande e contraste forte: texto escuro sobre fundo claro.")
numbered("S6a4","Seg · slide 4","white",T,"4/7","02",f"O botão cabe no {A_('dedo?','white')}","Botões pequenos e colados um no outro viram toque errado. Cada botão precisa ser grande, ter espaço em volta e dizer o que faz, como “Agendar consulta”.")
numbered("S6a5","Seg · slide 5","white",T,"5/7","03",f"Ligar é um {A_('toque','white')} só?","Telefone e WhatsApp precisam ser clicáveis. Quem tem que copiar o número, sair do site e colar no discador muitas vezes desiste no meio do caminho.")
numbered("S6a6","Seg · slide 6","white",T,"6/7","04",f"Nada {A_('pula','white')} na tela?","Janelas que abrem sozinhas (os pop-ups), banners que cobrem o texto e vídeos que tocam sozinhos confundem qualquer pessoa. Para quem tem menos prática, viram uma porta fechada.")
cta("S6a7","Seg · slide 7","bordo",T,"7/7",f"Um site fácil para quem tem 60 é fácil para {A_('todo mundo.','bordo')}","Falhou em algum teste? A gente cria e ajusta sites pensando em quem vai usar. Salve este post e fale com a gente.","Link na bio · WhatsApp")

# QUARTA · Perguntaram para a IA do Google. Sua empresa apareceu?
T="GOOGLE E IA"
cover("S6c1","Qua · slide 1","bordo",T,"1/7",f"Perguntaram para a {A_('IA','bordo')} do Google. Sua empresa apareceu?","O Modo IA já responde em português. Veja o que ajuda o seu negócio a entrar na resposta.")
stat("S6c2","Qua · slide 2","white",T,"2/7","2025",f"O {A_('Modo IA','white')} chegou à busca do Google em português.","Em vez de só uma lista de links, a pessoa conversa: “dentista que atende sábado perto de mim”. A resposta vem resumida, com links em destaque.","Fonte: blog do Google Brasil, 08/09/2025.")
numbered("S6c3","Qua · slide 3","white",T,"3/7","01",f"Escreva o que você {A_('faz,','white')} com palavras.","A IA lê texto. Uma foto bonita com “Bem-vindo” não diz que você é uma clínica de fisioterapia que atende por convênio. O site precisa dizer.")
numbered("S6c4","Qua · slide 4","white",T,"4/7","02",f"Diga {A_('onde','white')} e como atende.","Cidade, bairro, atendimento online, horários. Quem pergunta “perto de mim” ou “que atende online” precisa encontrar isso escrito no seu site.")
numbered("S6c5","Qua · slide 5","white",T,"5/7","03",f"Responda as {A_('dúvidas','white')} antes.","Preço a partir de quanto, prazo, formas de pagamento. Uma página de perguntas frequentes vira resposta pronta para quem pesquisa e para a IA que resume.")
numbered("S6c6","Qua · slide 6","white",T,"6/7","04",f"Os mesmos dados em todo {A_('lugar.','white')}","Telefone, endereço e horário iguais no site, no Perfil da Empresa no Google e no Instagram. Informação diferente em cada canto gera desconfiança, nas pessoas e nas máquinas.")
cta("S6c7","Qua · slide 7","bordo",T,"7/7",f"Ninguém garante lugar na resposta da IA. Mas dá para {A_('ajudar.','bordo')}","Um site claro e completo é a base. Quer saber se o seu está pronto? Comente IA que a gente te responde.","Comente IA")

# SEXTA · Black Friday: sua oferta mora num story que some?
T="BLACK FRIDAY"
cover("S6e1","Sex · slide 1","bordo",T,"1/6",f"Sua oferta mora num story que {A_('some','bordo')} em 24 horas?","Hoje é Black Friday. Veja onde a sua promoção deveria morar.")
numbered("S6e2","Sex · slide 2","white",T,"2/6","24h",f"É o tempo que um {A_('story','white')} fica no ar.","E o post do feed se perde entre outros. Quem viu ontem não acha hoje, e quem chega pelo Google não encontra nada.")
numbered("S6e3","Sex · slide 3","white",T,"3/6","01",f"Uma {A_('página','white')} só para a oferta.","Um endereço que você divulga em todo lugar, com o que está em promoção, o preço e um botão para comprar ou chamar no WhatsApp.")
numbered("S6e4","Sex · slide 4","white",T,"4/6","02",f"Prazo e regras {A_('à vista.','white')}","Até quando vale, para quem vale, como pagar. Quanto menos o cliente precisa perguntar, mais rápido ele decide.")
numbered("S6e5","Sex · slide 5","white",T,"5/6","03",f"Serve para a {A_('próxima','white')} data.","Natal, volta às aulas, Dia das Mães: a mesma página ganha uma oferta nova a cada campanha. Você monta uma vez e reaproveita.")
cta("S6e6","Sex · slide 6","bordo",T,"6/6",f"A próxima campanha pode ter uma página {A_('sua.','bordo')}","A MBDev cria landing pages (páginas com uma ação só) para campanhas de qualquer negócio, em todo o Brasil. Comente PÁGINA que a gente te chama.","Comente PÁGINA")
