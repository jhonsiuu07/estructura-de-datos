import customtkinter as ctk
from tkinter import messagebox


class FrameHistorial(ctk.CTkFrame):

    def __init__(self, parent, gestor_citas, ventana_principal):
        super().__init__(parent)

        self.gestor_citas = gestor_citas
        self.ventana_principal = ventana_principal

        self.crear_widgets()

    def crear_widgets(self):

        titulo = ctk.CTkLabel(self, text="Historial de Atención  (Pila LIFO)", font=("Arial", 18))
        titulo.pack(pady=10)

        self.scroll_frame = ctk.CTkScrollableFrame(self, height=150)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=5)


    # ==========================
    # ACTUALIZAR HISTORIAL
    # ==========================
    def actualizar(self):

        # Limpiar contenido
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        historial = self.gestor_citas.historial.recorrer()

        if not historial:
            ctk.CTkLabel(
                self.scroll_frame,
                text="No hay pacientes atendidos."
            ).pack(pady=10)
            return

        for paciente in historial:
            ctk.CTkLabel(
                self.scroll_frame,
                text=str(paciente),
                anchor="w"
            ).pack(fill="x", padx=5, pady=2)

    # ==========================
    # DESHACER
    # ==========================
    def deshacer_atencion(self):

        paciente = self.gestor_citas.deshacer_ultima_atencion()

        if paciente:
            messagebox.showinfo(
                "Deshacer",
                f"Se removió del historial:\n{paciente}"
            )
        else:
            messagebox.showwarning(
                "Historial",
                "No hay atenciones para deshacer."
            )

        self.ventana_principal.actualizar_todo()