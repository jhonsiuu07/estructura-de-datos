from estructuras.nodo import Nodo


class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        nuevo = Nodo(dato)

        if self.cabeza is None:
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar(self, dni):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.dato.dni == dni:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente

        return False

    def buscar(self, dni):
        actual = self.cabeza

        while actual:
            if actual.dato.dni == dni:
                return actual.dato
            actual = actual.siguiente

        return None

    def recorrer(self):
        elementos = []
        actual = self.cabeza

        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente

        return elementos