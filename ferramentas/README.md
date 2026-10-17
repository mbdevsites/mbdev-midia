# Ferramentas de criação MBDev

Preparação (uma vez por sessão):

    cd ferramentas && npm i && pip install playwright --break-system-packages   # Chromium já vem instalado no ambiente

## Identidade
- Bordô #6D1220 (cor do logo), bege #E9DCD8, bege claro #F5EFED, quase preto #080C14, linhas #D9C9C4.
- Títulos Outfit 700; textos Inter 400; uma palavra de destaque por título em Fraunces itálico 600 (opsz 9); números grandes em Outfit 700.
- Logo real (assets/logo-bordo.png ou logo-branco.png) no rodapé, 116 px de altura.
- Sem rosto da fundadora. Posicionamento nacional (100% online); nunca usar "Blumenau" como chamada.

## Carrosséis e posts (1080x1350)
`carrossel.py` tem três modelos: `cover`, `numbered`, `cta`, nos temas `light`, `white` e `bordo`. Eles escrevem arquivos `.dc.html` no mesmo formato do canvas de design (artboards). Exemplo completo: `exemplo_semana01.py`.

    python3 exemplo_semana01.py _tmp/s1          # gera os .dc.html
    python3 render.py _tmp/s1 _tmp/png S1a1 S1a2  # renderiza em PNG

No canvas, as imagens usam `/_blob/<id>`; `render.py` troca pelos arquivos de `assets/`.

## Reels animados (MP4 1080x1920, sem som)
`reel.py` tem as peças: `tag`, `headline`, `phone` (celular com print do site, rolagem suave), `chip`, `endcard`. Exemplos em `exemplos_reels.py` (reel3 portfólio, reel6 clínica, reel8 barbearia, reelS1b advocacia).

    python3 exemplos_reels.py _tmp/reels S1b

Prints de sites para o celular: `assets/<nome>.jpg` em 750x1430.

## Publicação
1. Copiar as mídias aprovadas para `semana-NN/` e dar push.
2. Na Metricool (blogId 7454948, fuso America/Sao_Paulo), criar cada post com `media` = link raw, `providers` instagram + facebook, 19h de segunda a sexta. Reels: `instagramData.type = REEL`, `facebookData.type = REEL`, `videoCoverMilliseconds` = 2500.
