"""
Cronômetro com interface gráfica (Python + tkinter).

Basta rodar:
    python cronometro_gui.py

Não precisa instalar nada além do Python (tkinter já vem embutido).
"""

import tkinter as tk
from tkinter import ttk


class CronometroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")
        self.root.geometry("420x520")
        self.root.configure(bg="#1e1e2e")
        self.root.resizable(False, False)

        # Estado
        self.rodando = False
        self.tempo_decorrido = 0.0  # em segundos
        self.job_id = None
        self.voltas = []

        self._montar_interface()

    # ---------- Interface ----------
    def _montar_interface(self):
        # Display do tempo
        self.label_tempo = tk.Label(
            self.root,
            text="00:00:00.00",
            font=("Consolas", 40, "bold"),
            fg="#a6e3a1",
            bg="#1e1e2e",
        )
        self.label_tempo.pack(pady=(40, 20))

        # Botões
        frame_botoes = tk.Frame(self.root, bg="#1e1e2e")
        frame_botoes.pack(pady=10)

        self.btn_iniciar = tk.Button(
            frame_botoes, text="Iniciar", width=10, command=self.iniciar_parar,
            bg="#a6e3a1", fg="#1e1e2e", font=("Segoe UI", 11, "bold"),
            relief="flat", cursor="hand2"
        )
        self.btn_iniciar.grid(row=0, column=0, padx=5)

        self.btn_volta = tk.Button(
            frame_botoes, text="Volta", width=10, command=self.marcar_volta,
            bg="#89b4fa", fg="#1e1e2e", font=("Segoe UI", 11, "bold"),
            relief="flat", cursor="hand2"
        )
        self.btn_volta.grid(row=0, column=1, padx=5)

        self.btn_zerar = tk.Button(
            frame_botoes, text="Zerar", width=10, command=self.zerar,
            bg="#f38ba8", fg="#1e1e2e", font=("Segoe UI", 11, "bold"),
            relief="flat", cursor="hand2"
        )
        self.btn_zerar.grid(row=0, column=2, padx=5)

        # Lista de voltas
        tk.Label(
            self.root, text="Voltas", font=("Segoe UI", 12, "bold"),
            fg="#cdd6f4", bg="#1e1e2e"
        ).pack(pady=(25, 5))

        frame_lista = tk.Frame(self.root, bg="#1e1e2e")
        frame_lista.pack(pady=5, fill="both", expand=True, padx=30)

        self.lista_voltas = tk.Listbox(
            frame_lista, font=("Consolas", 11), bg="#313244", fg="#cdd6f4",
            relief="flat", highlightthickness=0, justify="center"
        )
        self.lista_voltas.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(frame_lista, command=self.lista_voltas.yview)
        scrollbar.pack(side="right", fill="y")
        self.lista_voltas.config(yscrollcommand=scrollbar.set)

    # ---------- Lógica ----------
    def formata_tempo(self, segundos: float) -> str:
        horas = int(segundos // 3600)
        minutos = int((segundos % 3600) // 60)
        segs = int(segundos % 60)
        centesimos = int((segundos - int(segundos)) * 100)
        return f"{horas:02}:{minutos:02}:{segs:02}.{centesimos:02}"

    def atualizar(self):
        if self.rodando:
            self.tempo_decorrido += 0.01
            self.label_tempo.config(text=self.formata_tempo(self.tempo_decorrido))
            self.job_id = self.root.after(10, self.atualizar)

    def iniciar_parar(self):
        self.rodando = not self.rodando
        if self.rodando:
            self.btn_iniciar.config(text="Pausar", bg="#f9e2af")
            self.atualizar()
        else:
            self.btn_iniciar.config(text="Iniciar", bg="#a6e3a1")
            if self.job_id:
                self.root.after_cancel(self.job_id)

    def marcar_volta(self):
        if self.rodando:
            self.voltas.append(self.tempo_decorrido)
            texto = f"Volta {len(self.voltas)}  -  {self.formata_tempo(self.tempo_decorrido)}"
            self.lista_voltas.insert(tk.END, texto)
            self.lista_voltas.see(tk.END)

    def zerar(self):
        self.rodando = False
        if self.job_id:
            self.root.after_cancel(self.job_id)
        self.tempo_decorrido = 0.0
        self.voltas.clear()
        self.label_tempo.config(text="00:00:00.00")
        self.btn_iniciar.config(text="Iniciar", bg="#a6e3a1")
        self.lista_voltas.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = CronometroApp(root)
    root.mainloop()
