import customtkinter as ctk
from tkinter import messagebox


class FrameColas(ctk.CTkFrame):

    def __init__(self, parent, gestor_citas, ventana_principal):
        super().__init__(parent)

        self.gestor_citas = gestor_citas
        self.ventana_principal = ventana_principal

        self.crear_widgets()

    def crear_widgets(self):

        titulo = ctk.CTkLabel(self, text="Colas de Atención", font=("Arial", 18))
        titulo.pack(pady=10)

        # 🔴 Cola Prioridad
        # Frame contenedor horizontal

        label_prioridad = ctk.CTkLabel(self, text="🔴 Cola Prioridad")
        label_prioridad.pack()

        btn_recuperar = ctk.CTkButton(
            self,
            text="Recuperar último atendido",
            command=self.recuperar_paciente
        )
        btn_recuperar.pack(pady=5)

        self.frame_prioridad = ctk.CTkScrollableFrame(self, height=250)
        self.frame_prioridad.pack(fill="x", padx=10, pady=5)

        # 🟢 Cola FIFO
        label_normal = ctk.CTkLabel(self, text="🟢 Cola de Llegada")
        label_normal.pack(pady=(10, 0))

        self.frame_normal = ctk.CTkScrollableFrame(self, height=250)
        self.frame_normal.pack(fill="x", padx=10, pady=5)

    # ==========================================
    # ACTUALIZAR COLAS
    # ==========================================
    def actualizar(self):

        # Limpiar frames
        for widget in self.frame_prioridad.winfo_children():
            widget.destroy()

        for widget in self.frame_normal.winfo_children():
            widget.destroy()

        pacientes_prioridad = self.gestor_citas.ver_cola_prioridad()
        pacientes_fifo = self.gestor_citas.ver_cola_llegada()

        # ===============================
        # 🔴 MOSTRAR COLA PRIORIDAD
        # ===============================
        if not pacientes_prioridad:
            ctk.CTkLabel(
                self.frame_prioridad,
                text="Sin pacientes en prioridad"
            ).pack(pady=5)
        else:
            for i, paciente in enumerate(pacientes_prioridad):

                frame_item = ctk.CTkFrame(self.frame_prioridad)
                frame_item.pack(fill="x", padx=5, pady=5)

                info = (
                    f"{paciente.nombre} | DNI: {paciente.dni} | "
                    f"Prioridad: {paciente.prioridad} | "
                )

                ctk.CTkLabel(
                    frame_item,
                    text=info,
                    anchor="w"
                ).pack(side="left", padx=5)

                # SOLO el primero puede marcar como atendido
                if i == 0:
                    btn = ctk.CTkButton(
                        frame_item,
                        text="Atendido",
                        width=100,
                        command=self.marcar_atendido
                    )
                else:
                    btn = ctk.CTkButton(
                        frame_item,
                        text="Atendido",
                        width=100,
                        state="disabled"
                    )

                btn.pack(side="right", padx=5)

        # ===============================
        # 🟢 MOSTRAR COLA FIFO
        # ===============================
        if not pacientes_fifo:
            ctk.CTkLabel(
                self.frame_normal,
                text="Sin pacientes en espera"
            ).pack(pady=5)
        else:
            for i, paciente in enumerate(pacientes_fifo):

                frame_item = ctk.CTkFrame(self.frame_normal)
                frame_item.pack(fill="x", padx=5, pady=5)

                info = (
                    f"{paciente.nombre} | DNI: {paciente.dni} | "
                    f"Hora llegada: {getattr(paciente, 'hora_llegada', '--')}"
                )

                ctk.CTkLabel(
                    frame_item,
                    text=info,
                    anchor="w"
                ).pack(side="left", padx=5)

                # SOLO el primero puede pasar a prioridad
                if i == 0:
                    btn = ctk.CTkButton(
                        frame_item,
                        text="Atender",
                        width=100,
                        command=self.pasar_a_prioridad
                    )
                else:
                    btn = ctk.CTkButton(
                        frame_item,
                        text="Atender",
                        width=100,
                        state="disabled"
                    )

                btn.pack(side="right", padx=5)

    # ==========================================
    # PASAR DE FIFO → PRIORIDAD
    # ==========================================
    def pasar_a_prioridad(self):

        paciente = self.gestor_citas.pasar_a_prioridad()

        if paciente:
            messagebox.showinfo(
                "Paciente en Atención",
                f"{paciente.nombre} pasó a cola de prioridad"
            )
        else:
            messagebox.showwarning(
                "Cola",
                "No hay pacientes en espera"
            )

        self.ventana_principal.actualizar_todo()

    # ==========================================
    # MARCAR ATENDIDO
    # ==========================================
    def marcar_atendido(self):

        paciente = self.gestor_citas.marcar_atendido()

        if paciente:
            messagebox.showinfo(
                "Atendido",
                f"Paciente atendido:\n{paciente.nombre}"
            )
        else:
            messagebox.showwarning(
                "Cola",
                "No hay pacientes en prioridad"
            )

        self.ventana_principal.actualizar_todo()

    def recuperar_paciente(self):

        paciente = self.gestor_citas.recuperar_ultimo_atendido()

        if paciente is None:
            messagebox.showinfo("Info", "No hay pacientes en el historial.")
            return

        self.ventana_principal.actualizar_todo()