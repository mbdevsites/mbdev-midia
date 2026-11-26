"""Semana 7 (30/11 a 04/12/2026): carrosséis de segunda (foto real x banco de imagem), quarta (QR code no balcão) e sexta (site parado em 2023 + análise gratuita).
Uso: python3 semana07.py <pasta_saida>"""
import carrossel, pathlib, sys
from carrossel import *
carrossel.G=pathlib.Path(sys.argv[1]); carrossel.G.mkdir(parents=True,exist_ok=True)
G=carrossel.G
def A_(w,th): return acc(w,TH[th]["acc"])
def custom(name,title,th,tag,page,inner,right=None):
    t=TH[th]; (G/f"{name}.dc.html").write_text(wrap(title,t,head(t,tag,page)+inner,right if right is not None else swipe(t)))

# SEGUNDA · Foto real x banco de imagem
T="PARA SALVAR"
cover("S7a1","Seg · slide 1","light",T,"1/7",f"Seu cliente já viu essa foto em outro {A_('site.','light')}","Foto de banco de imagem tem lugar. Só não no lugar onde ele quer ver você.")
t=TH["white"]
def card(lbl,title,body,bg,fg,sub,border):
    return f'<div style="flex: 1; background: {bg}; border: {border}; border-radius: 32px; padding: 44px 40px; display: flex; flex-direction: column; gap: 22px"><div style="font-family: Outfit, sans-serif; font-weight: 600; font-size: 24px; letter-spacing: 5px; color: {sub}">{lbl}</div><div style="font-family: Outfit, sans-serif; font-weight: 700; font-size: 50px; line-height: 1.05; letter-spacing: -1.5px; color: {fg}">{title}</div><div style="font-size: 30px; line-height: 1.4; color: {sub}">{body}</div></div>'
vs=f'<div style="display: flex; flex-direction: column; gap: 48px"><h2 style="margin: 0; font-family: Outfit, sans-serif; font-weight: 700; font-size: 84px; line-height: 1.04; letter-spacing: -2.5px; text-wrap: balance">Quem procura você quer ver {A_("você.","white")}</h2><div style="display: flex; gap: 28px">'+card("BANCO DE IMAGEM","Bonito e genérico.","Sorriso perfeito, escritório que não existe, a mesma foto em mil sites.","#F5EFED","#5A5C66","#5A5C66","3px solid #D9C9C4")+card("FOTO REAL","Seu e de mais ninguém.","A sua recepção, o seu produto, as suas mãos trabalhando.","#6D1220","#FFFFFF","#E9DCD8","3px solid #6D1220")+'</div></div>'
custom("S7a2","Seg · slide 2","white",T,"2/7",vs)
numbered("S7a3","Seg · slide 3","white",T,"3/7","01",f"Mostre o seu {A_('lugar.','white')}","Fachada, recepção, sala de atendimento. Quem vai até você quer reconhecer a porta na hora em que chegar.")
numbered("S7a4","Seg · slide 4","white",T,"4/7","02",f"Mostre o trabalho {A_('de verdade.','white')}","O prato que sai da sua cozinha, o corte que você fez, o antes e depois. Com autorização do cliente, sempre.")
numbered("S7a5","Seg · slide 5","white",T,"5/7","03",f"Não quer aparecer? {A_('Tudo bem.','white')}","Mãos trabalhando, ferramentas, detalhes do espaço. Foto real não precisa de rosto para passar confiança.")
numbered("S7a6","Seg · slide 6","white",T,"6/7","04",f"O celular {A_('resolve.','white')}","Luz de janela, lente limpa e o celular deitado para as fotos do topo do site. Dez fotos boas valem mais que cem genéricas.")
cta("S7a7","Seg · slide 7","bordo",T,"7/7",f"Banco de imagem é tempero. O prato é a sua {A_('foto.','bordo')}","Na MBDev, o site é montado com as suas fotos, e a gente te orienta sobre o que fotografar. Salve este post para a próxima sessão de fotos.","Salve para depois")

# QUARTA · QR code no balcão
T="NEGÓCIO LOCAL"
cover("S7c1","Qua · slide 1","bordo",T,"1/7",f"O cliente está no seu balcão. Para onde o seu {A_('QR code','bordo')} leva?","Dezembro é mês de loja cheia. Aproveite quem já entrou.")
numbered("S7c2","Qua · slide 2","white",T,"2/7","0",f"{A_('aplicativos','white')} para o cliente instalar.","Na maioria dos celulares, a própria câmera lê o QR code: é só apontar. Um QR no balcão, no cardápio ou na embalagem vira uma ponte entre a loja e a internet.")
numbered("S7c3","Qua · slide 3","white",T,"3/7","01",f"Para a {A_('avaliação','white')} no Google.","No Perfil da Empresa no Google, a opção de pedir avaliações gera um link e um QR code prontos. O cliente satisfeito avalia ainda no balcão.")
numbered("S7c4","Qua · slide 4","white",T,"4/7","02",f"Para o {A_('cardápio','white')} ou catálogo.","Uma página no seu site com produtos e preços. Mudou o preço? Você atualiza a página e não precisa reimprimir nada.")
numbered("S7c5","Qua · slide 5","white",T,"5/7","03",f"Para o {A_('próximo','white')} horário.","Salão, clínica, estúdio: o QR leva para a página de agendamento e o cliente já sai com o retorno marcado.")
numbered("S7c6","Qua · slide 6","white",T,"6/7","04",f"Diga o que {A_('acontece.','white')}","QR code sozinho quase ninguém escaneia. Escreva do lado: “Aponte a câmera e avalie a gente”. E teste em celulares diferentes antes de imprimir.")
cta("S7c7","Qua · slide 7","bordo",T,"7/7",f"O QR é a ponte. O {A_('destino','bordo')} é o seu site.","Cardápio, agendamento ou página de campanha: a MBDev cria o lugar para onde o seu QR code leva. Comente QR que a gente te responde.","Comente QR")

# SEXTA · Seu site ainda está em 2023? + análise gratuita
T="ANÁLISE GRATUITA"
cover("S7e1","Sex · slide 1","bordo",T,"1/6",f"O seu site ainda está em {A_('2023?','bordo')}","4 sinais de que ele parou no tempo. E um jeito gratuito de resolver antes de 2027.")
numbered("S7e2","Sex · slide 2","white",T,"2/6","01",f"O ano no {A_('rodapé.','white')}","“© 2023” lá embaixo faz o cliente pensar: será que essa empresa ainda funciona?")
numbered("S7e3","Sex · slide 3","white",T,"3/6","02",f"Preços e serviços {A_('antigos.','white')}","Se o site mostra um valor e o WhatsApp mostra outro, a conversa já começa com desconfiança.")
numbered("S7e4","Sex · slide 4","white",T,"4/6","03",f"Promoção que já {A_('acabou.','white')}","Banner de Black Friday em dezembro, “inscrições abertas” para uma turma que já começou. O cliente percebe.")
numbered("S7e5","Sex · slide 5","white",T,"5/6","04",f"Botões que levam a {A_('lugar nenhum.','white')}","WhatsApp com número antigo, Instagram desativado, formulário que não chega. Teste cada botão do seu site hoje.")
cta("S7e6","Sex · slide 6","bordo",T,"6/6",f"Entre em 2027 com o site em {A_('dia.','bordo')}","Mande o link no WhatsApp e receba, de graça, de 3 a 5 melhorias práticas: velocidade, celular, Google e contato. Ainda não tem site? A gente analisa como você aparece na busca.","Link na bio · WhatsApp")
