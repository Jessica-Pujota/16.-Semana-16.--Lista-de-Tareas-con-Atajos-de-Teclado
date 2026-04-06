
class Tarea: # Modelo para representar una tarea
    def __init__(self, descripcion): # Inicializa una tarea con su descripción y estado de completada
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self): # Marca la tarea como completada
        self.completada = True

    def __str__(self): # Devuelve una representación de la tarea, mostrando su estado y descripción
        estado = "[✔]" if self.completada else "[ ]"
        return f"{estado} {self.descripcion}"