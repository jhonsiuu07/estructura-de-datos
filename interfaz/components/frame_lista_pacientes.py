import customtkinter as ctk
from tkinter import messagebox


class FrameListaPacientes(ctk.CTkFrame):

    def __init__(self, parent, gestor_pacientes, gestor_citas, ventana_principal):
        super().__init__(parent)

        self.gestor_pacientes = gestor_pacientes
        self.gestor_citas = gestor_citas
        self.ventana_principal = ventana_principal

        self.crear_widgets()

    def crear_widgets(self):

        titulo = ctk.CTkLabel(self, text="Pacientes Registrados", font=("Arial", 18))
        titulo.pack(pady=10)

        self.entry_busqueda = ctk.CTkEntry(self, placeholder_text="Buscar por DNI")
        self.entry_busqueda.pack(pady=5)
        self.entry_busqueda.bind("<KeyRelease>", self.buscar_dinamico)
        
        # Scrollable donde irán los pacientes
        self.scroll_frame = ctk.CTkScrollableFrame(self)
        self.scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # ==========================
    # ACTUALIZAR LISTA
    # ==========================
    def actualizar(self, pacientes_filtrados=None):

        # Limpiar contenido anterior
        for widget in self.scroll_frame.winfo_children():
            widget.destroy()

        # Si no viene lista filtrada → mostrar todos
        if pacientes_filtrados is None:
            pacientes = self.gestor_pacientes.listar_pacientes()
        else:
            pacientes = pacientes_filtrados

        if not pacientes:
            ctk.CTkLabel(
                self.scroll_frame,
                text="No hay pacientes encontrados."
            ).pack(pady=10)
            return

        for paciente in pacientes:

            frame_paciente = ctk.CTkFrame(self.scroll_frame)
            frame_paciente.pack(fill="x", pady=5, padx=5)

            info = ctk.CTkLabel(
                frame_paciente,
                text=str(paciente),
                anchor="w"
            )
            info.pack(side="left", padx=5, pady=5)

            btn_cola = ctk.CTkButton(
                frame_paciente,
                text="Realizar cita",
                width=120,
                command=lambda p=paciente: self.abrir_modal_cita(p)
            )
            btn_cola.pack(side="right", padx=5)

        
    def buscar_dinamico(self, event):
        texto = self.entry_busqueda.get().strip()

        if texto == "":
            # Mostrar todos
            self.actualizar()
        else:
            pacientes_filtrados = self.gestor_pacientes.buscar_por_dni_prefijo(texto)
            self.actualizar(pacientes_filtrados)


    

    def abrir_modal_cita(self, paciente):
        modal = ctk.CTkToplevel(self)
        modal.title("Realizar cita")
        modal.geometry("400x350")
        modal.grab_set()  # Hace que sea modal real

        # --- Datos del paciente ---
        ctk.CTkLabel(modal, text=f"DNI: {paciente.dni}").pack(pady=5)
        ctk.CTkLabel(modal, text=f"Nombre: {paciente.nombre}").pack(pady=5)
        ctk.CTkLabel(modal, text=f"Edad: {paciente.edad}").pack(pady=5)

        # --- Síntoma ---
        ctk.CTkLabel(modal, text="Síntoma").pack(pady=5)
        entry_sintoma = ctk.CTkEntry(modal)
        entry_sintoma.pack(pady=5)

        # --- Prioridad ---
        ctk.CTkLabel(modal, text="Prioridad").pack(pady=5)
        combo_prioridad = ctk.CTkComboBox(
            modal,
            values=["Emergencia", "Urgente", "Normal"]
        )
        combo_prioridad.pack(pady=5)
        combo_prioridad.set("Normal")

        # --- Confirmar ---
        def confirmar():
            sintoma = entry_sintoma.get()
            prioridad = combo_prioridad.get()

            if not sintoma:
                print("Debe ingresar un síntoma")
                return

            paciente.sintoma = sintoma
            paciente.prioridad = prioridad

            self.gestor_citas.registrar_cita(paciente)

            modal.destroy()
            self.ventana_principal.actualizar_todo()

        ctk.CTkButton(
            modal,
            text="Confirmar cita",
            command=confirmar
        ).pack(pady=15)

    