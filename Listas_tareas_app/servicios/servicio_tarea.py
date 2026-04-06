class TareaServicio: # Servicio para gestionar las tareas
    def __init__(self):
        self._tareas = []

    def agregar_tarea(self, descripcion): # Agrega una nueva tarea a la lista si la descripción no está vacía
        if descripcion.strip():
            nueva_tarea = Tarea(descripcion)
            self._tareas.append(nueva_tarea)
            return True
        return False

    def eliminar_tarea(self, indice): # Elimina una tarea de la lista si el índice es válido
        if 0 <= indice < len(self._tareas):
            del self._tareas[indice]

    def completar_tarea(self, indice): #   Marca una tarea como completada si el índice es válido
        if 0 <= indice < len(self._tareas):
            self._tareas[indice].marcar_completada()

    def obtener_todas(self): # Devuelve la lista de todas las tareas
        return self._tareas