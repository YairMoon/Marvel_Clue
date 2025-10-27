import tkinter as tk
from civil_war_clue import CivilWarGUIv3  # importa la clase del juego

INTRO_TEXTO = (
    "⚠️ ACCESO DE SEGURIDAD NIVEL OMEGA ⚠️\n"
    "--------------------------------------------\n"
    "Este archivo está clasificado por S.H.I.E.L.D. bajo el protocolo CIVIL WAR.\n"
    "La información contenida en este sistema no existe en registros públicos.\n\n"
    "Solo personal con autorización de nivel OMEGA puede acceder a los casos aquí descritos.\n"
    "Cualquier intento de manipulación, copia o divulgación no autorizada\n"
    "será rastreado y sancionado conforme al artículo 19B del Acta de Seguridad Superhumana.\n\n"
    ">> Iniciando conexión con la base de datos...\n"
    ">> Validando credenciales del agente...\n"
    ">> Nivel de acceso confirmado.\n"
    ">> Cargando archivos clasificados...\n\n"
    "Bienvenido, agente.\n"
    "Tu misión: reconstruir la verdad detrás de la Guerra Civil de los Vengadores.\n"
    "Solo la evidencia y tu razonamiento determinarán la historia oficial."
)

class PantallaIntro:
    def __init__(self, root):
        self.root = root
        self.root.title("S.H.I.E.L.D. // Acceso Clasificado")
        self.root.configure(bg="#0b0c10")

        frame = tk.Frame(root, bg="#0b0c10", padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        titulo = tk.Label(
            frame,
            text="S.H.I.E.L.D. // PROTOCOLO CIVIL WAR",
            fg="#c3073f",
            bg="#0b0c10",
            font=("Helvetica", 16, "bold"),
            justify="center"
        )
        titulo.pack(pady=(0,10))

        sub = tk.Label(
            frame,
            text="ARCHIVO CLASIFICADO - NIVEL OMEGA",
            fg="#45a29e",
            bg="#0b0c10",
            font=("Helvetica", 10, "bold"),
            justify="center"
        )
        sub.pack(pady=(0,20))

        # Caja con scroll
        text_box_frame = tk.Frame(frame, bg="#0b0c10")
        text_box_frame.pack()

        text_scroll = tk.Scrollbar(text_box_frame)
        text_scroll.pack(side="right", fill="y")

        self.text_box = tk.Text(
            text_box_frame,
            width=80,
            height=18,
            bg="#1f2833",
            fg="#c5c6c7",
            wrap="word",
            font=("Consolas", 10),
            bd=2,
            relief="ridge",
            yscrollcommand=text_scroll.set
        )
        self.text_box.pack(side="left")
        text_scroll.config(command=self.text_box.yview)

        self.text_box.insert("1.0", INTRO_TEXTO)
        self.text_box.config(state="disabled")

        # Botón continuar
        self.btn = tk.Button(
            frame,
            text="CONTINUAR",
            bg="#c3073f",
            fg="white",
            font=("Helvetica", 10, "bold"),
            padx=15,
            pady=8,
            bd=0,
            command=self.iniciar_juego
        )
        self.btn.pack(pady=20)

        aviso = tk.Label(
            frame,
            text="ADVERTENCIA: Proceder confirma responsabilidad legal.",
            fg="#c5c6c7",
            bg="#0b0c10",
            font=("Consolas", 8),
            justify="center"
        )
        aviso.pack()

    def iniciar_juego(self):
        # Cerrar intro
        self.root.destroy()
        # Abrir juego real
        lanzar_juego()

def lanzar_juego():
    game_root = tk.Tk()
    game_root.title("MARVEL CIVIL WAR - Archivo Activo")
    app = CivilWarGUIv3(game_root)
    game_root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    # En Windows puedes descomentar esta línea si quieres que la intro abra maximizada:
    # root.state('zoomed')
    PantallaIntro(root)
    root.mainloop()
