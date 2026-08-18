# Cronômetro em Python

Um cronômetro simples escrito em Python puro (sem dependências externas).
O projeto tem duas versões:

- **`cronometro_gui.py`** — versão com janela gráfica (tkinter). Basta dar duplo clique ou rodar com `python cronometro_gui.py` para abrir o app.
- **`cronometro.py`** — versão de terminal (linha de comando).

## Funcionalidades
- Iniciar / pausar a contagem
- Marcar voltas (laps)
- Zerar o cronômetro
- Histórico de voltas visível na tela

## Como usar

Versão gráfica (recomendada):
```bash
python cronometro_gui.py
```

Versão de terminal:
```bash
python cronometro.py
```
Durante a execução no terminal: `ENTER` marca volta, `p` pausa/retoma, `q` encerra.

## Requisitos
- Python 3.8 ou superior (usa apenas a biblioteca padrão — `tkinter` já vem incluso na maioria das instalações do Python)

## Licença
Todos os direitos reservados. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
