"""
Cronômetro simples em Python (terminal).

Comandos durante a execução:
    ENTER       -> marca uma volta (lap)
    p + ENTER   -> pausa/retoma
    q + ENTER   -> encerra e mostra o resumo

Autor: (adicione seu nome aqui)
"""

import time
from datetime import timedelta


def formata_tempo(segundos: float) -> str:
    """Converte segundos em HH:MM:SS.cc"""
    td = timedelta(seconds=segundos)
    horas, resto = divmod(td.seconds, 3600)
    minutos, segs = divmod(resto, 60)
    centesimos = int((segundos - int(segundos)) * 100)
    return f"{horas:02}:{minutos:02}:{segs:02}.{centesimos:02}"


def cronometro():
    print("=== Cronômetro ===")
    print("ENTER = volta | p+ENTER = pausar/retomar | q+ENTER = sair\n")

    inicio = time.perf_counter()
    tempo_pausado_total = 0.0
    pausado = False
    momento_pausa = None
    voltas = []

    try:
        while True:
            comando = input()

            if comando.lower() == "q":
                break

            elif comando.lower() == "p":
                if not pausado:
                    pausado = True
                    momento_pausa = time.perf_counter()
                    print(">> Pausado")
                else:
                    pausado = False
                    tempo_pausado_total += time.perf_counter() - momento_pausa
                    print(">> Retomado")

            else:
                if pausado:
                    print(">> Cronômetro pausado, retome com 'p' antes de marcar volta.")
                    continue
                agora = time.perf_counter() - inicio - tempo_pausado_total
                voltas.append(agora)
                print(f"Volta {len(voltas)}: {formata_tempo(agora)}")

    except KeyboardInterrupt:
        pass

    if pausado:
        tempo_pausado_total += time.perf_counter() - momento_pausa

    tempo_final = time.perf_counter() - inicio - tempo_pausado_total

    print("\n=== Resumo ===")
    for i, v in enumerate(voltas, start=1):
        print(f"Volta {i}: {formata_tempo(v)}")
    print(f"Tempo total: {formata_tempo(tempo_final)}")


if __name__ == "__main__":
    cronometro()
