class Paciente:
    def __init__(self, dni, nombre, edad):
        self.dni = dni
        self.nombre = nombre
        self.edad = edad
        
        # Estos se asignarán cuando se haga la cita
        self.sintoma = None
        self.prioridad = None
        self.hora_llegada = None

        # Historial clínico (pila)
        self.historial_clinico = []

    def __str__(self):
        return f"DNI: {self.dni} | Nombre: {self.nombre} | Edad: {self.edad}"