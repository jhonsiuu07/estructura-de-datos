from estructuras.nodo import Nodo


class ColaPrioridad:
    def __init__(self):
        self.frente = None

    def esta_vacia(self):
        return self.frente is None

    def obtener_valor_prioridad(self, prioridad):
        prioridades = {
            "Emergencia": 1,
            "Urgente": 2,
            "Normal": 3
        }
        return prioridades.get(prioridad, 3)

    def enqueue(self, paciente):
        nuevo = Nodo(paciente)

        if self.esta_vacia():
            self.frente = nuevo
            return

        prioridad_nueva = self.obtener_valor_prioridad(paciente.prioridad)

        # Insertar al inicio si tiene mayor prioridad
        prioridad_frente = self.obtener_valor_prioridad(self.frente.dato.prioridad)

        if prioridad_nueva < prioridad_frente:
            nuevo.siguiente = self.frente
            self.frente = nuevo
            return

        # Buscar posición correcta
        actual = self.frente

        while actual.siguiente:
            prioridad_siguiente = self.obtener_valor_prioridad(
                actual.siguiente.dato.prioridad
            )

            if prioridad_nueva < prioridad_siguiente:
                break

            actual = actual.siguiente

        nuevo.siguiente = actual.siguiente
        actual.siguiente = nuevo

    def dequeue(self):
        if self.esta_vacia():
            return None

        paciente = self.frente.dato
        self.frente = self.frente.siguiente
        return paciente

    def ver_frente(self):
        if self.esta_vacia():
            return None
        return self.frente.dato

    def recorrer(self):
        elementos = []
        actual = self.frente

        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente

        return elementos