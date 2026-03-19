from estructuras.arbol_abb import ArbolABB
from estructuras.lista_enlazada import ListaEnlazada
from estructuras.cola_prioridad import ColaPrioridad
from estructuras.cola import Cola
from modelos import paciente
from modelos.paciente import Paciente


class GestorPacientes:

    def __init__(self):
        self.arbol = ArbolABB()
        self.lista = ListaEnlazada()
        self.cola_prioridad = ColaPrioridad()
        self.cola_normal = Cola() 

    # Registrar paciente
    def registrar_paciente(self, paciente: Paciente):

        # Insertar en árbol (por DNI)
        self.arbol.insertar(paciente)

        # Insertar en lista
        self.lista.insertar(paciente)

    # Buscar paciente
    def buscar_paciente(self, dni):

        return self.arbol.buscar(dni)

    # Eliminar paciente
    def eliminar_paciente(self, dni):

        paciente = self.buscar_paciente(dni)

        if paciente:
            self.arbol.eliminar(dni)
            self.lista.eliminar(paciente)
            return True

        return False

    # Listar pacientes
    def listar_pacientes(self):

        return self.lista.recorrer()
    
    def agregar_a_cola(self, paciente):
        self.cola_prioridad.enqueue(paciente)

    def buscar_por_dni_prefijo(self, prefijo):
        return self.arbol.buscar_por_prefijo(prefijo)