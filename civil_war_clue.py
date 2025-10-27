import tkinter as tk
from tkinter import ttk
import random
import textwrap

# ==========================================================
# MARVEL CIVIL WAR - ARCHIVO CLASIFICADO v3
# Cambios clave:
# - La escena y las primeras pistas YA NO revelan el lugar explícito.
# - Se describe el ambiente, no el nombre del sitio.
# - El lugar real solo aparece al final (o cuando ya perdiste).
# ==========================================================

def wrap(texto, width=70):
    return "\n".join(textwrap.wrap(texto, width))


CASES = [
    {
        "culpable": "Iron Man",
        "arma": "Repulsores de Iron Man",
        "lugar": "Laboratorio de Stark Industries",
        "clasificacion": "CLASIFICACIÓN: ALTO SECRETO // ACCESO SOLO DIRECTOR",
        "riesgo": "RIESGO POLÍTICO: Corporativo / Fuga tecnológica",
        "hora_evento": "22:41",
        # IMPORTANTE: descripción ahora evita nombrar el lugar directo
        "resumen_crimen": (
            "Se reportó un incidente en una instalación tecnológica de alta seguridad dedicada a I+D. "
            "El área estaba fuera del alcance del personal regular y estaba protegida por autenticación biométrica. "
            "El objetivo fue neutralizado mediante un pulso de energía concentrado, sin daño colateral visible."
        ),
        "contexto_extra": (
            "Minutos antes del impacto, el sistema interno de cámaras fue pasado manualmente a modo local, "
            "evitando registro automático remoto. Eso solo puede hacerlo alguien con privilegios de propietario. "
            "Las paredes muestran huellas térmicas simétricas, indicando un disparo controlado desde altura, "
            "como si el atacante estuviera flotando o en suspensión asistida."
        ),
        "pistas_base": [
            "No se hallaron casquillos ni fragmentos de munición tradicional.",
            "El patrón térmico en la superficie forma una elipse casi perfecta alrededor del punto de impacto.",
            "El ángulo del haz energético viene desde arriba hacia abajo, no en línea recta frontal.",
        ],
        "pistas_extra": [
            "Lectura energética coincide con armamento de proyección direccional marca Stark.",
            "Se detectaron microfragmentos de aleación titanio-dorado compatibles con blindaje de un exotraje personalizado.",
        ],
        "motivo": (
            "El responsable alega que el blanco iba a filtrar información crítica sobre infraestructura "
            "y operaciones de ciertos Vengadores. Su justificación oficial fue 'contención preventiva', "
            "descrita como fuerza no letal. El reporte médico no confirma esa afirmación."
        ),
        "final_oficial": (
            "INFORME FINAL // S.H.I.E.L.D.\n"
            "Responsable confirmado: Iron Man.\n"
            "Escena real: Laboratorio de Stark Industries.\n"
            "Arma empleada: Repulsores integrados del traje.\n"
            "Conclusión táctica: intervención directa sin autorización externa.\n"
            "Cobertura política: se declarará como 'fallo en pruebas internas' para evitar cargos."
        ),
    },
    {
        "culpable": "Captain America",
        "arma": "Escudo del Capitán América",
        "lugar": "Base de los Vengadores",
        "clasificacion": "CLASIFICACIÓN: INTERNO VENGADORES // NO DIVULGAR",
        "riesgo": "RIESGO POLÍTICO: Violación de protocolos de contención",
        "hora_evento": "03:17",
        "resumen_crimen": (
            "Se detectó un enfrentamiento físico en un entorno de entrenamiento táctico nocturno. "
            "El espacio había sido aislado manualmente de la red general, dejando sensores y grabación en modo privado. "
            "El objetivo sufrió trauma contundente concentrado en zona torácica y clavicular, sin múltiples impactos."
        ),
        "contexto_extra": (
            "Se registraron marcas circulares en el suelo, generadas por un objeto metálico con borde redondeado, "
            "de masa elevada. El ángulo del golpe final fue descendente, a menos de un metro de distancia. "
            "El atacante muestra control total de fuerza física, típico de combate cercano entrenado."
        ),
        "pistas_base": [
            "Las cámaras del recinto fueron desconectadas localmente, no desde la red central.",
            "El golpe final corresponde a un objeto contundente circular de aleación avanzada.",
            "Las fracturas son limpias y están alineadas, indicando un solo impacto preciso, no pelea descontrolada.",
        ],
        "pistas_extra": [
            "Se hallaron rastros microscópicos de vibranio incrustados en el punto de impacto.",
            "El patrón de fuerza coincide con entrenamiento cuerpo a cuerpo de un operador con fuerza sobrehumana disciplinada.",
        ],
        "motivo": (
            "El agresor declaró que estaba impidiendo una detención 'ilegal' contra alguien que consideraba inocente. "
            "Argumentó que la fuerza usada fue 'necesaria' para evitar lo que describió como secuestro encubierto."
        ),
        "final_oficial": (
            "INFORME FINAL // S.H.I.E.L.D.\n"
            "Responsable confirmado: Captain America.\n"
            "Escena real: Base de los Vengadores.\n"
            "Arma empleada: Escudo de vibranio.\n"
            "Conclusión táctica: fuerza aplicada para bloquear captura interna.\n"
            "Versión pública sugerida: 'incidente durante entrenamiento'."
        ),
    },
    {
        "culpable": "Black Widow",
        "arma": "Jeringa con suero experimental",
        "lugar": "Embajada de Wakanda",
        "clasificacion": "CLASIFICACIÓN: ULTRA SECRETO // CONTACTO DIPLOMÁTICO",
        "riesgo": "RIESGO POLÍTICO: Alto / Tensiones con nación extranjera",
        "hora_evento": "19:05",
        "resumen_crimen": (
            "Durante una reunión privada en una sala diplomática altamente custodiada, el objetivo colapsó "
            "casi instantáneamente. No hubo señales auditivas de disparos ni forcejeo intenso. "
            "El deceso ocurrió de manera limpia y silenciosa frente a muy poca gente autorizada."
        ),
        "contexto_extra": (
            "El cuerpo no mostraba daño visible significativo: ni fracturas ni trauma contundente. "
            "Solo se detectó una punción extremadamente fina en la base del cuello, "
            "posteriormente maquillada con precisión quirúrgica. El compuesto hallado en sangre "
            "no está en catálogos médicos comunes ni militares estándar."
        ),
        "pistas_base": [
            "El agresor estuvo lo bastante cerca de la víctima como para hacer contacto físico directo.",
            "Se evidencia manipulación posterior para ocultar la única marca visible.",
            "El químico utilizado no es rastreable a proveedores comerciales conocidos.",
        ],
        "pistas_extra": [
            "Solo un agente con entrenamiento encubierto puede neutralizar así y limpiar la escena en segundos.",
            "El entorno donde ocurrió estaba bajo protección ceremonial extranjera, no bajo jurisdicción directa de S.H.I.E.L.D.",
        ],
        "motivo": (
            "El acto se justificó como contención preventiva para evitar que cierta información detonara "
            "un conflicto público entre una monarquía tecnológicamente avanzada y los Vengadores. "
            "Se manejó como 'neutralización silenciosa para preservar estabilidad'."
        ),
        "final_oficial": (
            "INFORME FINAL // S.H.I.E.L.D.\n"
            "Responsable confirmada: Black Widow.\n"
            "Escena real: Embajada de Wakanda.\n"
            "Arma empleada: Jeringa con suero experimental no rastreable.\n"
            "Conclusión táctica: eliminación quirúrgica presentada oficialmente como 'colapso por estrés'."
        ),
    },
    {
        "culpable": "Black Panther",
        "arma": "Garras de vibranio",
        "lugar": "Aeropuerto de Leipzig",
        "clasificacion": "CLASIFICACIÓN: CONTACTO EXTRANJERO // VIGILANCIA PRIORITARIA",
        "riesgo": "RIESGO POLÍTICO: Venganza personal de figura real",
        "hora_evento": "16:32",
        "resumen_crimen": (
            "En una zona logística activa con presencia civil cercana, un objetivo sufrió cortes profundos, "
            "limpios y rápidos. El blindaje táctico que llevaba fue abierto como si no ofreciera resistencia. "
            "El ataque duró menos de cuatro segundos y no causó destrucción generalizada alrededor."
        ),
        "contexto_extra": (
            "Testigos civiles reportaron una silueta oscura moviéndose a velocidades difíciles de seguir a simple vista. "
            "Las heridas presentan bordes sellados térmicamente, lo que sugiere material exótico cortando "
            "a alta energía cinética. El patrón del ataque parece personal, no disuasivo."
        ),
        "pistas_base": [
            "No hay balística. No hay explosivos.",
            "El corte atraviesa blindaje militar reforzado, sin fracturarlo a golpes: lo 'abre'.",
            "El atacante se movió con precisión quirúrgica, como si tuviera entrenamiento de élite y motivación emocional.",
        ],
        "pistas_extra": [
            "Se detectaron rastros microscópicos de un metal extremadamente raro, altamente absorbente de energía.",
            "La agresión responde a patrones de represalia inmediata, no a una misión formal.",
        ],
        "motivo": (
            "El agresor actuó motivado por represalia directa tras la muerte de un familiar de alto perfil. "
            "No buscaba arresto ni interrogatorio; buscaba justicia personal inmediata."
        ),
        "final_oficial": (
            "INFORME FINAL // S.H.I.E.L.D.\n"
            "Responsable confirmado: Black Panther.\n"
            "Escena real: Aeropuerto de Leipzig.\n"
            "Arma empleada: Garras de vibranio.\n"
            "Conclusión táctica: ejecución personal motivada por venganza.\n"
            "Cobertura propuesta: 'baja colateral en enfrentamiento entre superhumanos'."
        ),
    },
    {
        "culpable": "Winter Soldier",
        "arma": "Arma de energía de HYDRA",
        "lugar": "Instalaciones de HYDRA",
        "clasificacion": "CLASIFICACIÓN: PELIGRO EXTREMO // TECNOLOGÍA ILEGAL",
        "riesgo": "RIESGO POLÍTICO: Reactivación de protocolos HYDRA",
        "hora_evento": "04:09",
        "resumen_crimen": (
            "En una estructura subterránea abandonada, reforzada con placas viejas de contención militar, "
            "se registró una única descarga de alta energía. Toda la actividad humana en la sala terminó "
            "casi al instante. No hay signos de pelea larga: fue un único evento dirigido."
        ),
        "contexto_extra": (
            "El área mostraba equipos analógicos modificados con hardware no estándar, muy parecido a tecnología "
            "clandestina histórica. La escena fue parcialmente limpiada siguiendo protocolos de encubrimiento "
            "propios de una organización ya desmantelada oficialmente."
        ),
        "pistas_base": [
            "Se detectaron marcas de quemadura interna sin metralla ni proyectiles físicos.",
            "Había restos de aparatos asociados a condicionamiento mental de vieja data.",
            "Los registros de potencia no coinciden con tecnología conocida de los Vengadores actuales.",
        ],
        "pistas_extra": [
            "La descarga fue disparada con estabilidad tipo militar avanzada, no como un civil improvisado.",
            "Las huellas tácticas indican un ejecutor entrenado para entrar, activar, y salir sin ruido.",
        ],
        "motivo": (
            "El ejecutor estaba bajo control mental parcial, respondiendo a comandos heredados de una red "
            "considerada inactiva. No actuó por iniciativa propia totalmente consciente."
        ),
        "final_oficial": (
            "INFORME FINAL // S.H.I.E.L.D.\n"
            "Responsable confirmado: Winter Soldier.\n"
            "Escena real: Instalaciones de HYDRA.\n"
            "Arma empleada: Arma de energía de HYDRA (prototipo prohibido).\n"
            "Conclusión táctica: operación ejecutada bajo condicionamiento mental.\n"
            "Clasificación final: destruir copias secundarias."
        ),
    },
]

SUSPECTOS = [
    "Iron Man",
    "Captain America",
    "Black Widow",
    "Black Panther",
    "Winter Soldier",
]

LUGARES = [
    "Base de los Vengadores",
    "Instalaciones de HYDRA",
    "Embajada de Wakanda",
    "Aeropuerto de Leipzig",
    "Laboratorio de Stark Industries",
]

ARMAS = [
    "Escudo del Capitán América",
    "Repulsores de Iron Man",
    "Arma de energía de HYDRA",
    "Jeringa con suero experimental",
    "Garras de vibranio",
]


class CivilWarGUIv3:
    def __init__(self, root):
        self.root = root
        self.root.title("MARVEL CIVIL WAR - ARCHIVO CLASIFICADO v3")

        # Paleta tipo S.H.I.E.L.D.
        self.bg_main = "#0b0c10"
        self.bg_panel = "#1f2833"
        self.acento_verde = "#45a29e"
        self.acento_rojo = "#c3073f"
        self.texto_claro = "#c5c6c7"
        self.texto_blanco = "#ffffff"

        self.root.configure(bg=self.bg_main)

        # Estado
        self.caso_actual = None
        self.intentos_restantes = 3

        # ----- IZQUIERDA -----
        left = tk.Frame(self.root, bg=self.bg_main)
        left.grid(row=0, column=0, padx=20, pady=20, sticky="n")

        tk.Label(
            left,
            text="MARVEL CIVIL WAR\nS.H.I.E.L.D. // ARCHIVO CLASIFICADO",
            fg=self.acento_rojo,
            bg=self.bg_main,
            font=("Helvetica", 14, "bold"),
            justify="center"
        ).pack(pady=(0,8))

        tk.Label(
            left,
            text="Simulador de Análisis Forense Tipo CLUE\n(Responsable / Escena real / Arma)",
            fg=self.acento_verde,
            bg=self.bg_main,
            font=("Helvetica", 9, "bold"),
            justify="center"
        ).pack(pady=(0,12))

        # ESCENA
        tk.Label(left, text="Escena del Incidente:",
                 bg=self.bg_main, fg=self.texto_blanco,
                 font=("Helvetica", 10, "bold")).pack(anchor="w")
        self.txt_escena = tk.Text(
            left, width=70, height=10,
            bg=self.bg_panel, fg=self.texto_claro,
            wrap="word", font=("Consolas", 9),
            bd=2, relief="ridge"
        )
        self.txt_escena.pack(pady=(0,10))

        # PISTAS
        tk.Label(left, text="Pistas Recolectadas:",
                 bg=self.bg_main, fg=self.texto_blanco,
                 font=("Helvetica", 10, "bold")).pack(anchor="w")
        self.txt_pistas = tk.Text(
            left, width=70, height=10,
            bg=self.bg_panel, fg=self.texto_claro,
            wrap="word", font=("Consolas", 9),
            bd=2, relief="ridge"
        )
        self.txt_pistas.pack(pady=(0,10))

        # RESULTADO
        tk.Label(left, text="Informe y Evaluación:",
                 bg=self.bg_main, fg=self.texto_blanco,
                 font=("Helvetica", 10, "bold")).pack(anchor="w")
        self.txt_resultado = tk.Text(
            left, width=70, height=14,
            bg=self.bg_panel, fg=self.texto_claro,
            wrap="word", font=("Consolas", 9),
            bd=2, relief="ridge"
        )
        self.txt_resultado.pack(pady=(0,10))

        # ----- DERECHA -----
        right = tk.Frame(self.root, bg=self.bg_panel, bd=2, relief="ridge")
        right.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        tk.Label(
            right,
            text="Panel de Deducción",
            bg=self.bg_panel,
            fg=self.acento_verde,
            font=("Helvetica", 11, "bold")
        ).pack(pady=(10,5))

        # Sospechoso
        tk.Label(right, text="Sospechoso:",
                 bg=self.bg_panel, fg=self.texto_blanco,
                 font=("Helvetica", 9, "bold")).pack(anchor="w", padx=10)
        self.cb_sospechoso = ttk.Combobox(
            right, values=SUSPECTOS, state="readonly", width=32
        )
        self.cb_sospechoso.pack(padx=10, pady=(0,12))

        # Lugar
        tk.Label(right, text="Lugar (tu sospecha):",
                 bg=self.bg_panel, fg=self.texto_blanco,
                 font=("Helvetica", 9, "bold")).pack(anchor="w", padx=10)
        self.cb_lugar = ttk.Combobox(
            right, values=LUGARES, state="readonly", width=32
        )
        self.cb_lugar.pack(padx=10, pady=(0,12))

        # Arma
        tk.Label(right, text="Arma / Método:",
                 bg=self.bg_panel, fg=self.texto_blanco,
                 font=("Helvetica", 9, "bold")).pack(anchor="w", padx=10)
        self.cb_arma = ttk.Combobox(
            right, values=ARMAS, state="readonly", width=32
        )
        self.cb_arma.pack(padx=10, pady=(0,12))

        # Botones
        btn_style = {
            "font": ("Helvetica", 9, "bold"),
            "width": 28,
            "bd": 0,
            "padx": 6,
            "pady": 6,
        }

        self.btn_nuevo = tk.Button(
            right,
            text="NUEVO CASO / ESCANEAR",
            bg=self.acento_verde,
            fg="black",
            command=self.nuevo_caso,
            **btn_style
        )
        self.btn_nuevo.pack(pady=(10,6))

        self.btn_acusar = tk.Button(
            right,
            text="ACUSAR",
            bg=self.acento_rojo,
            fg="white",
            command=self.acusar,
            **btn_style
        )
        self.btn_acusar.pack(pady=(6,10))

        # Estado
        self.lbl_estado = tk.Label(
            right,
            text="Estado: Esperando caso...",
            bg=self.bg_panel,
            fg=self.texto_claro,
            font=("Consolas", 9),
            justify="left",
            wraplength=230
        )
        self.lbl_estado.pack(padx=10, pady=(10,15))

        # Inicializar textos
        self._reset_ui()

    def _reset_ui(self):
        self.intentos_restantes = 3
        self.caso_actual = None
        self.cb_sospechoso.set("")
        self.cb_lugar.set("")
        self.cb_arma.set("")

        self.txt_escena.delete("1.0", tk.END)
        self.txt_escena.insert(
            tk.END,
            "Presiona 'NUEVO CASO / ESCANEAR' para cargar un incidente clasificado.\n\n"
            "Recibirás descripción del entorno del crimen:\n"
            " • tipo de lugar (seguridad privada, diplomático, subterráneo, etc.)\n"
            " • hora aproximada\n"
            " • condiciones operativas\n\n"
            "PERO el nombre exacto del lugar NO será revelado todavía.\n"
        )

        self.txt_pistas.delete("1.0", tk.END)
        self.txt_pistas.insert(
            tk.END,
            "Aquí verás pistas forenses iniciales.\n"
            "Si fallas una acusación, recibirás pistas más clasificadas.\n"
            "Dispones de 3 intentos máximo antes de revelación forzada.\n"
        )

        self.txt_resultado.delete("1.0", tk.END)
        self.txt_resultado.insert(
            tk.END,
            "Este panel mostrará:\n"
            " • Coincidencias parciales de tu teoría\n"
            " • Intentos restantes\n"
            " • Y al final, el INFORME OFICIAL de S.H.I.E.L.D.\n"
            "   con CULPABLE REAL / LUGAR REAL / ARMA REAL.\n"
        )

        self.lbl_estado.config(text="Estado: Sin caso activo.")

    def nuevo_caso(self):
        self.caso_actual = random.choice(CASES)
        self.intentos_restantes = 3

        self.cb_sospechoso.set("")
        self.cb_lugar.set("")
        self.cb_arma.set("")

        escena_txt = []
        escena_txt.append(self.caso_actual["clasificacion"])
        escena_txt.append(self.caso_actual["riesgo"])
        escena_txt.append(f"HORA DEL EVENTO: {self.caso_actual['hora_evento']}")
        escena_txt.append("")
        escena_txt.append("RESUMEN DEL INCIDENTE:")
        escena_txt.append(wrap(self.caso_actual["resumen_crimen"]))
        escena_txt.append("")
        escena_txt.append("ANÁLISIS DEL ENTORNO:")
        escena_txt.append(
            wrap(self.caso_actual["contexto_extra"])
        )
        escena_txt.append("")
        escena_txt.append(
            "(Nota: el nombre de la ubicación real está clasificado. "
            "Deberás inferirlo.)"
        )

        self.txt_escena.delete("1.0", tk.END)
        self.txt_escena.insert(tk.END, "\n".join(escena_txt))

        self.txt_pistas.delete("1.0", tk.END)
        self.txt_pistas.insert(
            tk.END,
            "PISTAS INICIALES (Nivel Interno):\n\n"
        )
        for i, pista in enumerate(self.caso_actual["pistas_base"], start=1):
            self.txt_pistas.insert(
                tk.END,
                f"[Pista {i}] {wrap(pista)}\n\n"
            )

        self.txt_resultado.delete("1.0", tk.END)
        self.txt_resultado.insert(
            tk.END,
            "Caso activo.\n"
            "Selecciona Sospechoso / Lugar / Arma y pulsa ACUSAR.\n"
            "Intentos restantes: 3\n"
        )

        self.lbl_estado.config(
            text="Estado: Archivo cargado. Ubicación exacta aún clasificada."
        )

    def acusar(self):
        if self.caso_actual is None:
            self.lbl_estado.config(
                text="Estado: No hay caso activo. Usa 'NUEVO CASO / ESCANEAR'."
            )
            return

        if self.intentos_restantes <= 0:
            self.lbl_estado.config(
                text="Estado: Sin intentos. Informe ya revelado."
            )
            return

        elegido_quien = self.cb_sospechoso.get().strip()
        elegido_lugar = self.cb_lugar.get().strip()
        elegido_arma = self.cb_arma.get().strip()

        if not elegido_quien or not elegido_lugar or not elegido_arma:
            self.lbl_estado.config(
                text="Estado: Selecciona Sospechoso / Lugar / Arma antes de acusar."
            )
            return

        match_quien = (elegido_quien.lower() == self.caso_actual["culpable"].lower())
        match_lugar = (elegido_lugar.lower() == self.caso_actual["lugar"].lower())
        match_arma = (elegido_arma.lower() == self.caso_actual["arma"].lower())

        correcto_total = match_quien and match_lugar and match_arma

        self.intentos_restantes -= 1

        salida = []
        salida.append("EVALUACIÓN DE TU HIPÓTESIS:")
        salida.append(f"  Sospechoso: {'COINCIDE' if match_quien else 'NO COINCIDE'}")
        salida.append(f"  Lugar     : {'COINCIDE' if match_lugar else 'NO COINCIDE'}")
        salida.append(f"  Arma      : {'COINCIDE' if match_arma else 'NO COINCIDE'}")
        salida.append("")

        if correcto_total:
            salida.append("VEREDICTO: ✅ Reconstrucción aceptada.")
            salida.append("Tu informe coincide con la versión oficial clasificada.")
            salida.append("")
            self.lbl_estado.config(
                text="Estado: Caso resuelto. Acceso completo concedido."
            )
            self._anexar_informe_oficial(salida, revelar_final=True)
            self.intentos_restantes = 0

        else:
            salida.append("VEREDICTO: ❌ Reconstrucción incompleta.")
            salida.append(
                "Tu versión no puede archivarse como oficial. Falta(s) coincidencia(s)."
            )
            salida.append("")

            if self.intentos_restantes > 0:
                salida.append(f"INTENTOS RESTANTES: {self.intentos_restantes}")
                salida.append("")
                salida.append("Pista de nivel confidencial (acceso escalado):")
                pista_conf = random.choice(self.caso_actual["pistas_extra"])
                salida.append("  → " + wrap(pista_conf))
                salida.append("")
                self.lbl_estado.config(
                    text=f"Estado: Hipótesis rechazada. Intentos restantes: {self.intentos_restantes}."
                )
                self._anexar_informe_oficial(salida, revelar_final=False)

            else:
                salida.append("INTENTOS RESTANTES: 0")
                salida.append("")
                salida.append(
                    "Has agotado los intentos. Se libera el INFORME FINAL para cierre administrativo."
                )
                salida.append("")
                self.lbl_estado.config(
                    text="Estado: Intentos agotados. Informe completo revelado."
                )
                self._anexar_informe_oficial(salida, revelar_final=True)

        self.txt_resultado.delete("1.0", tk.END)
        self.txt_resultado.insert(tk.END, "\n".join(salida))

    def _anexar_informe_oficial(self, salida_list, revelar_final):
        salida_list.append("----------------------------------------")
        salida_list.append("INFORME OFICIAL // S.H.I.E.L.D.")
        salida_list.append("----------------------------------------")
        salida_list.append(self.caso_actual["clasificacion"])
        salida_list.append(self.caso_actual["riesgo"])
        salida_list.append("")

        if revelar_final:
            salida_list.append(f"Culpable confirmado: {self.caso_actual['culpable']}")
            salida_list.append(f"Escena real        : {self.caso_actual['lugar']}")
            salida_list.append(f"Arma empleada      : {self.caso_actual['arma']}")
            salida_list.append("")
            salida_list.append("Motivación táctica:")
            salida_list.append(wrap(self.caso_actual["motivo"]))
            salida_list.append("")
            salida_list.append(wrap(self.caso_actual["final_oficial"]))
            salida_list.append("")
            salida_list.append("[FIN DEL ARCHIVO CLASIFICADO]")
        else:
            salida_list.append(
                "Acceso parcial: La identidad completa del agresor, "
                "detalles exactos de la localización y el arma empleada "
                "permanecen bajo reserva de nivel director."
            )
            salida_list.append(
                "Tu hipótesis no cumple estándar probatorio ni diplomático aún."
            )
            salida_list.append(
                "Mejora tu deducción: revisa las pistas y vuelve a acusar."
            )
            salida_list.append("")


if __name__ == "__main__":
    root = tk.Tk()
    app = CivilWarGUIv3(root)
    root.mainloop()
