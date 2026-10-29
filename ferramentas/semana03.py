"""Semana 3 (02 a 06/11/2026): carrosséis de segunda, quarta e sexta.
Uso: python3 semana03.py <pasta_saida>"""
import carrossel, pathlib, sys
from carrossel import *
carrossel.G=pathlib.Path(sys.argv[1]); carrossel.G.mkdir(parents=True,exist_ok=True)
G=carrossel.G

def custom(name,title,th,tag,page,inner,right=None):
    t=TH[th]
    (G/f"{name}.dc.html").write_text(wrap(title,t,head(t,tag,page)+inner,right if right is not None else swipe(t)))

def check_svg(c,fg):
    return f'<svg width="56" height="56" viewBox="0 0 56 56" aria-hidden="true" style="flex: none"><rect x="2" y="2" width="52" height="52" rx="14" fill="{c}"/><path d="M15 29l9 9 17-19" fill="none" stroke="{fg}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def checklist(name,title,th,tag,page,kicker,h2,items):
    t=TH[th]; a=t["acc"]
    box=check_svg(t["btnbg"],t["btnfg"])
    rows="".join(f'<div style="display: flex; gap: 32px; align-items: flex-start; padding: 30px 0; border-top: 2px solid {t["line"]}{"; border-bottom: 2px solid "+t["line"] if i==len(items)-1 else ""}">{box}<div style="display: flex; flex-direction: column; gap: 8px"><div style="font-family: Outfit, sans-serif; font-weight: 600; font-size: 44px; line-height: 1.15">{h}</div><div style="font-size: 29px; line-height: 1.4; color: {t["sub"]}">{b}</div></div></div>' for i,(h,b) in enumerate(items))
    inner=f'<div style="display: flex; flex-direction: column; gap: 30px"><div style="font-family: Outfit, sans-serif; font-weight: 700; font-size: 30px; letter-spacing: 4px; color: {a}">{kicker}</div><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 80px; line-height: 1.04; letter-spacing: -2.5px; text-wrap: balance">{h2}</h2><div style="display: flex; flex-direction: column">{rows}</div></div>'
    custom(name,title,th,tag,page,inner)

# SEGUNDA · SEO em uma frase e 3 ajustes simples (light)
T="SEO SEM COMPLICAÇÃO"; th="light"; t=TH[th]; a=t["acc"]
cover("S3a1","Seg · slide 1",th,T,"1/6",f"SEO em uma frase (e 3 ajustes que você faz {acc('hoje.',a)})","Sem termos difíceis. Salve para fazer com calma.")
frase=f'''<div style="display: flex; flex-direction: column; gap: 40px"><div style="font-family: Outfit, sans-serif; font-weight: 700; font-size: 30px; letter-spacing: 4px; color: {a}">SEO, EM UMA FRASE</div><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 88px; line-height: 1.06; letter-spacing: -2.5px; text-wrap: balance">É ajudar o Google a entender o seu site e mostrar você para quem {acc('procura.',a)}</h2><p style="margin: 0; font-size: 34px; line-height: 1.45; color: {t["sub"]}; max-width: 860px">A sigla vem do inglês: otimização para mecanismos de busca. Na prática, são ajustes simples feitos com constância.</p></div>'''
custom("S3a2","Seg · slide 2",th,T,"2/6",frase)
numbered("S3a3","Seg · slide 3",th,T,"3/6","01","Dê um título claro a cada página.","É o texto em destaque que aparece no resultado do Google. Diga o que você faz e para quem, como “Nutricionista esportiva online | Ana Souza”, e não só “Início”.")
numbered("S3a4","Seg · slide 4",th,T,"4/6","02","Escreva com as palavras do seu cliente.","Ele digita “dentista para criança”, não “odontopediatria”. Use os termos que ele usa nos títulos e nos textos do site.")
numbered("S3a5","Seg · slide 5",th,T,"5/6","03","Avise o Google que o site existe.","Cadastre o site no Google Search Console, ferramenta gratuita do Google, e envie o mapa do site (sitemap), a lista de páginas que você quer que ele encontre.")
cta("S3a6","Seg · slide 6",th,T,"6/6",f"Qual ajuste você vai fazer {acc('primeiro?',a)}","Conte nos comentários. Se travar em algum passo, pergunte lá que a gente explica.","Salve para fazer com calma")

# QUARTA · Checklist do Perfil da Empresa no Google (white)
T="GOOGLE E NEGÓCIO LOCAL"; th="white"; t=TH[th]; a=t["acc"]
cover("S3c1","Qua · slide 1",th,T,"1/7",f"Checklist do Perfil da Empresa no {acc('Google.',a)}","5 itens para conferir com o seu perfil aberto ao lado.")
numbered("S3c2","Qua · slide 2",th,T,"2/7","01","A categoria principal certa.","É ela que diz ao Google em quais buscas você aparece. Escolha a mais específica: “Barbearia” funciona melhor do que “Salão de beleza”, se é isso que você é.")
numbered("S3c3","Qua · slide 3",th,T,"3/7","02","Horários sempre em dia, até nos feriados.","Use a opção de horário especial. Vêm aí 15/11, 20/11 e as festas de fim de ano: o cliente quer saber se você abre antes de sair de casa.")
numbered("S3c4","Qua · slide 4",th,T,"4/7","03","Fotos reais e recentes.","Fachada, ambiente, equipe e trabalhos prontos. Fotos de verdade passam mais confiança do que imagens de banco.")
numbered("S3c5","Qua · slide 5",th,T,"5/7","04","Uma descrição que vende.","Você tem até 750 caracteres para contar o que faz, para quem e o que te diferencia. Escreva para pessoas, sem repetir palavras-chave.")
numbered("S3c6","Qua · slide 6",th,T,"6/7","05","Contato e site em um toque.","Telefone, WhatsApp e o link do seu site preenchidos e conferidos. Um link quebrado aqui é cliente que desiste.")
cta("S3c7","Qua · slide 7",th,T,"7/7",f"Quantos itens você já {acc('tem?',a)}","Conte nos comentários de 0 a 5. Quer ajuda para completar o seu perfil? Comente GOOGLE.","Salve para conferir depois")

# SEXTA · Checklist do site que vende + análise gratuita (bordo)
T="CHECKLIST PARA SALVAR"; th="bordo"; t=TH[th]; a=t["acc"]
cover("S3e1","Sex · slide 1",th,T,"1/6",f"O checklist do site que {acc('vende.',a)}","9 itens. Marque quantos o seu site já tem.")
checklist("S3e2","Sex · slide 2",th,T,"2/6","PARTE 1",f"Primeira {acc('impressão',a)}",[("Em 5 segundos dá para entender o que você faz.","Quem chega precisa saber na hora se está no lugar certo."),("Abre rápido no celular.","É ali que a maioria dos clientes vai te encontrar."),("Um botão principal sempre à vista.","Pedir orçamento, agendar ou comprar: uma ação clara.")])
checklist("S3e3","Sex · slide 3",th,T,"3/6","PARTE 2",acc("Confiança",a),[("Fotos reais do seu trabalho.","Nada substitui mostrar o que você faz de verdade."),("Depoimentos ou avaliações.","A opinião de outro cliente convence mais do que a sua."),("Cadeado de segurança.","O HTTPS, que protege os dados de quem visita.")])
checklist("S3e4","Sex · slide 4",th,T,"4/6","PARTE 3",f"Fácil de {acc('chamar',a)}",[("WhatsApp em um toque.","Sem precisar copiar número nem procurar o contato."),("Onde e quando você atende.","Endereço ou área de atendimento, e horários."),("Tudo atualizado.","Serviços, preços e informações que valem hoje.")])
chips="".join(f'<div style="background: {t["card"]}; border-radius: 24px; padding: 28px 32px; font-family: Outfit, sans-serif; font-weight: 600; font-size: 36px; color: #FFFFFF">{x}</div>' for x in ["Velocidade","Uso no celular","Google","Conversão"])
def pill(txt,bg,fg): return f'<div style="align-self: flex-start; font-family: Outfit, sans-serif; font-weight: 700; font-size: 26px; letter-spacing: 5px; padding: 12px 26px; border-radius: 999px; background: {bg}; color: {fg}">{txt}</div>'
offer=f'''<div style="display: flex; flex-direction: column; gap: 40px">{pill("MARCOU MENOS DE 9?","#FFFFFF","#6D1220")}<h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 96px; line-height: 1.02; letter-spacing: -3px; text-wrap: balance">A gente analisa o seu site de {acc('graça.',a)}</h2><div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 20px">{chips}</div><p style="margin: 0; font-size: 34px; line-height: 1.45; color: {t["sub"]}; max-width: 880px">Você manda o link e recebe de 3 a 5 melhorias. Ainda não tem site? Analisamos como o seu negócio aparece hoje na busca.</p></div>'''
custom("S3e5","Sex · slide 5",th,T,"5/6",offer)
cta("S3e6","Sex · slide 6",th,T,"6/6",f"Comente {acc('ANÁLISE',a)} aqui embaixo.","A gente te chama no direct. Se preferir, fale direto pelo link da bio. Sem compromisso.","Quero minha análise gratuita")
print("ok")
