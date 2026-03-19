import customtkinter as ctk

from servicios.gestor_pacientes import GestorPacientes
from servicios.gestor_citas import GestorCitas
from modelos.paciente import Paciente

from interfaz.components.frame_formulario import FrameFormulario
from interfaz.components.frame_lista_pacientes import FrameListaPacientes
from interfaz.components.frame_colas import FrameColas
from interfaz.components.frame_historial import FrameHistorial


class VentanaPrincipal(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Sistema de Clínica")
        self.geometry("1200x700")

        # ==========================
        # Servicios (Lógica)
        # ==========================
        self.gestor_pacientes = GestorPacientes()
        self.gestor_citas = GestorCitas()
        self.cargar_pacientes_prueba()
        

        # ==========================
        # Configuración GRID
        # ==========================
        self.grid_columnconfigure(0, weight=1)  # Formulario
        self.grid_columnconfigure(1, weight=2)  # Lista pacientes
        self.grid_columnconfigure(2, weight=1)  # Colas

        self.grid_rowconfigure(0, weight=0)  # Título
        self.grid_rowconfigure(1, weight=3)  # Zona principal
        self.grid_rowconfigure(2, weight=1)  # Historial

        self.crear_widgets()
        self.actualizar_todo()
    # ==========================
    # CREAR INTERFAZ
    # ==========================
    def crear_widgets(self):

        # -------- TÍTULO --------
        titulo = ctk.CTkLabel(
            self,
            text="SISTEMA DE GESTIÓN CLÍNICA",
            font=("Arial", 26)
        )
        titulo.grid(row=0, column=0, columnspan=3, pady=20)

        # -------- FORMULARIO --------
        self.frame_formulario = FrameFormulario(
            self,
            self.gestor_pacientes,
            self.gestor_citas,
            self
        )

        self.frame_formulario.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=10,
            pady=10
        )

        # -------- LISTA PACIENTES --------
        self.frame_lista = FrameListaPacientes(
            self,
            self.gestor_pacientes,
            self.gestor_citas,
            self
        )

        self.frame_lista.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=10,
            pady=10
        )

    # -------- COLAS --------
        self.frame_colas = FrameColas(
            self,
            self.gestor_citas,
            self
        )

        self.frame_colas.grid(
            row=1,
            column=2,
            rowspan=2,
            sticky="nsew",
            padx=10,
            pady=10
        )   

        # -------- HISTORIAL --------
        self.frame_historial = FrameHistorial(
            self,
            self.gestor_citas,
            self
        )

        self.frame_historial.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky="nsew",
            padx=10,
            pady=10
        )


    # ==========================
    # MÉTODO CENTRAL ACTUALIZACIÓN
    # ==========================
    def actualizar_todo(self):
        self.frame_lista.actualizar()
        self.frame_colas.actualizar()
        self.frame_historial.actualizar()

    def cargar_pacientes_prueba(self):

        pacientes_prueba = [
            Paciente("10402810", "Carlos Pérez", 30),
            Paciente("13201023", "María Gómez", 25),
            Paciente("20482019", "Luis Torres", 40),
            Paciente("18201930", "Ana Rodríguez", 35),
            Paciente("30281029", "Pedro Martínez", 50),
            Paciente("42039103", "Sofía Herrera", 28),
            Paciente("50193820", "Diego Castro", 45),
            Paciente("30281029", "Rosa Caceres", 45),
            Paciente("40293288", "Lis Tapia", 45),
            Paciente("80399192", "Juan Valdez", 45),
        ]

        for paciente in pacientes_prueba:
            self.gestor_pacientes.registrar_paciente(paciente)