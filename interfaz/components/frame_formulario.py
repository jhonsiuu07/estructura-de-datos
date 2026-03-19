import customtkinter as ctk
from tkinter import messagebox
from modelos.paciente import Paciente


class FrameFormulario(ctk.CTkFrame):

    def __init__(self, parent, gestor_pacientes, gestor_citas, ventana_principal):
        super().__init__(parent)

        self.gestor_pacientes = gestor_pacientes
        self.gestor_citas = gestor_citas
        self.ventana_principal = ventana_principal

        self.crear_widgets()

    def crear_widgets(self):

        titulo = ctk.CTkLabel(self, text="Registrar Paciente", font=("Arial", 18))
        titulo.pack(pady=10)

        self.entry_dni = ctk.CTkEntry(self, placeholder_text="DNI")
        self.entry_dni.pack(pady=5, fill="x", padx=10)

        self.entry_nombre = ctk.CTkEntry(self, placeholder_text="Nombre")
        self.entry_nombre.pack(pady=5, fill="x", padx=10)

        self.entry_edad = ctk.CTkEntry(self, placeholder_text="Edad")
        self.entry_edad.pack(pady=5, fill="x", padx=10)


        btn_registrar = ctk.CTkButton(
            self,
            text="Registrar",
            command=self.registrar_paciente
        )
        btn_registrar.pack(pady=15)

    # ==========================
    # REGISTRAR PACIENTE
    # ==========================
    def registrar_paciente(self):
        dni = self.entry_dni.get()
        nombre = self.entry_nombre.get()
        edad = self.entry_edad.get()

        if not dni or not nombre or not edad:
            print("Todos los campos son obligatorios")
            return

        paciente = Paciente(dni, nombre, int(edad))

        self.gestor_pacientes.registrar_paciente(paciente)

        print("Paciente registrado correctamente")

        self.limpiar_campos()
        self.ventana_principal.actualizar_todo()

    def limpiar_campos(self):
        self.entry_dni.delete(0, ctk.END)
        self.entry_nombre.delete(0, ctk.END)
        self.entry_edad.delete(0, ctk.END)