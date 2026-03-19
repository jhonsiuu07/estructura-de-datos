class NodoABB:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


class ArbolABB:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        self.raiz = self._insertar(self.raiz, dato)

    def _insertar(self, nodo, dato):
        if nodo is None:
            return NodoABB(dato)

        if dato.dni < nodo.dato.dni:
            nodo.izquierda = self._insertar(nodo.izquierda, dato)
        else:
            nodo.derecha = self._insertar(nodo.derecha, dato)

        return nodo

    def buscar(self, dni):
        return self._buscar(self.raiz, dni)

    def _buscar(self, nodo, dni):
        if nodo is None:
            return None

        if dni == nodo.dato.dni:
            return nodo.dato

        if dni < nodo.dato.dni:
            return self._buscar(nodo.izquierda, dni)
        else:
            return self._buscar(nodo.derecha, dni)

    def inorden(self):
        elementos = []
        self._inorden(self.raiz, elementos)
        return elementos

    def _inorden(self, nodo, lista):
        if nodo:
            self._inorden(nodo.izquierda, lista)
            lista.append(nodo.dato)
            self._inorden(nodo.derecha, lista)

    # ==============================
    # BUSQUEDA POR PREFIJO (DNI)
    # ==============================

    def buscar_por_prefijo(self, prefijo):
        resultados = []
        self._buscar_prefijo_recursivo(self.raiz, str(prefijo), resultados)
        return resultados

    def _buscar_prefijo_recursivo(self, nodo, prefijo, resultados):
        if nodo is None:
            return

        dni_actual = str(nodo.dato.dni)

        # Si el DNI empieza con el prefijo → agregar
        if dni_actual.startswith(prefijo):
            resultados.append(nodo.dato)

        # Recorremos ambos lados
        self._buscar_prefijo_recursivo(nodo.izquierda, prefijo, resultados)
        self._buscar_prefijo_recursivo(nodo.derecha, prefijo, resultados)