from estructuras.cola import Cola
from estructuras.cola_prioridad import ColaPrioridad
from estructuras.pila import Pila
from datetime import datetime


class GestorCitas:

    def __init__(self):
        self.cola_llegada = Cola()          # FIFO
        self.cola_prioridad = ColaPrioridad()
        self.historial = Pila()

    # =====================================
    # REGISTRAR CITA (entra solo a FIFO)
    # =====================================

    def registrar_cita(self, paciente):
        paciente.hora_llegada = datetime.now().strftime("%H:%M:%S")
        self.cola_llegada.enqueue(paciente)

    # =====================================
    # PASAR DE FIFO → PRIORIDAD
    # =====================================

    def pasar_a_prioridad(self):
        """
        Solo el primero de la cola FIFO puede pasar.
        """
        if self.cola_llegada.esta_vacia():
            return None

        paciente = self.cola_llegada.dequeue()
        self.cola_prioridad.enqueue(paciente)

        return paciente

    # =====================================
    # MARCAR COMO ATENDIDO
    # =====================================

    def marcar_atendido(self):
        if self.cola_prioridad.esta_vacia():
            return None

        paciente = self.cola_prioridad.dequeue()
        self.historial.push(paciente)

        return paciente
    
    def recuperar_ultimo_atendido(self):

        if not self.historial:
            return None

        paciente = self.historial.pop()  # SACAMOS DE LA PILA

        # Reinsertar al inicio de la cola
        self.cola_prioridad.enqueue(paciente)

        return paciente

    # =====================================
    # CONSULTAS PARA INTERFAZ
    # =====================================

    def ver_cola_llegada(self):
        return self.cola_llegada.recorrer()

    def ver_cola_prioridad(self):
        return self.cola_prioridad.recorrer()

    def ver_historial(self):
        return self.historial.recorrer()

    def hay_pacientes_fifo(self):
        return not self.cola_llegada.esta_vacia()

    def hay_pacientes_prioridad(self):
        return not self.cola_prioridad.esta_vacia()