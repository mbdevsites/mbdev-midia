import carrossel, pathlib, sys
from carrossel import *
carrossel.G=pathlib.Path(sys.argv[1]); carrossel.G.mkdir(parents=True,exist_ok=True)
# SEGUNDA · Site x Instagram (light)
T="SITE OU INSTAGRAM?"; th="light"; a=TH[th]["acc"]
cover("S1a1","Seg · slide 1",th,T,"1/6",f"Já tenho Instagram. Preciso de {acc('site?',a)}","A resposta curta é sim. A explicação está nos próximos slides.")
numbered("S1a2","Seg · slide 2",th,T,"2/6","01","O Instagram é alugado. O site é seu.","O algoritmo muda, o alcance cai e a conta pode ser bloqueada. No site, quem decide é você.")
numbered("S1a3","Seg · slide 3",th,T,"3/6","02","O Google não mostra o seu feed.","Quem busca “psicóloga online” ou “barbearia perto de mim” encontra sites e o Google Maps, não posts.")
numbered("S1a4","Seg · slide 4",th,T,"4/6","03","Site passa credibilidade.","Antes de comprar, o cliente pesquisa. Um endereço próprio, como seunegocio.com.br, mostra que a empresa é séria.")
numbered("S1a5","Seg · slide 5",th,T,"5/6","04","Um completa o outro.","O Instagram aproxima e o site convence. Use os dois juntos: o link do site na bio leva quem já gostou de você a virar cliente.")
cta("S1a6","Seg · slide 6",th,T,"6/6",f"Seu Instagram merece um site à {acc('altura.',a)}","Conte nos comentários: hoje o link da sua bio leva para onde?","Peça seu orçamento pelo link da bio")

# QUARTA · Google Maps (white)
T="GOOGLE E NEGÓCIO LOCAL"; th="white"; a=TH[th]["acc"]
cover("S1c1","Qua · slide 1",th,T,"1/5",f"Seu negócio aparece no {acc('Google Maps?',a)}","3 checagens rápidas para fazer hoje, direto do celular.")
numbered("S1c2","Qua · slide 2",th,T,"2/5","01","Pesquise como um cliente","Abra o Google Maps e busque o seu serviço com a sua cidade, como “pediatra em Curitiba”. Você aparece entre os primeiros?")
numbered("S1c3","Qua · slide 3",th,T,"3/5","02","Confira se o perfil é seu","Se aparecer a opção “Reivindicar esta empresa”, o perfil existe, mas ainda não está no seu controle.")
numbered("S1c4","Qua · slide 4",th,T,"4/5","03","Revise as informações","Horário, telefone, endereço, link do site e fotos. Informação errada faz o cliente desistir antes de chegar.")
cta("S1c5","Qua · slide 5",th,T,"5/5",f"Não apareceu? A gente {acc('resolve.',a)}","Criamos e otimizamos o seu perfil no Google Business para você ser encontrado por quem procura.","Fale com a gente pelo link da bio")

# SEXTA · Quanto custa manter (bordo)
T="CUSTOS DE UM SITE"; th="bordo"; a=TH[th]["acc"]
cover("S1e1","Sex · slide 1",th,T,"1/6",f"Quanto custa manter um site {acc('no ar?',a)}","O que você paga depois que o site fica pronto, sem letras miúdas.")
numbered("S1e2","Sex · slide 2",th,T,"2/6","01","Domínio","É o endereço do site, como seunegocio.com.br. Um .com.br custa R$ 40 por ano no Registro.br.")
numbered("S1e3","Sex · slide 3",th,T,"3/6","02","Hospedagem","É onde o site fica guardado e funcionando. Planos para WordPress costumam ficar entre R$ 15 e R$ 70 por mês.")
numbered("S1e4","Sex · slide 4",th,T,"4/6","03","Manutenção","Atualizações, cópias de segurança e proteção. Você pode cuidar disso ou deixar com um plano de suporte.")
numbered("S1e5","Sex · slide 5",th,T,"5/6","04","E-mail profissional","Opcional, como contato@seunegocio.com.br. Muitos planos de hospedagem já incluem.")
cta("S1e6","Sex · slide 6",th,T,"6/6",f"Sem surpresas no {acc('orçamento.',a)}","Antes de começar, explicamos cada custo e o que está incluso no seu projeto.","Peça seu orçamento pelo link da bio")
print("ok")
