import tkinter as tk
from tkinter import messagebox

class AppTarea(tk.Tk): # Hereda de tk.Tk para crear la ventana principal
    def __init__(self, servicio):
        super().__init__()
        self.servicio = servicio
        self.title("Gestor de Tareas Pro - Atajos de Teclado")
        self.geometry("400x500")
        
        self._configurar_interfaz()
        self._configurar_atajos()

    def _configurar_interfaz(self):
        # Entrada de tarea
        self.entrada = tk.Entry(self, font=("Arial", 12))
        self.entrada.pack(pady=10, padx=20, fill="x")
        self.entrada.focus_set() # Iniciar con el foco aquí

        # Lista de tareas
        self.lista_visual = tk.Listbox(self, font=("Arial", 11), selectmode=tk.SINGLE)
        self.lista_visual.pack(pady=10, padx=20, fill="both", expand=True)

        # Instrucciones de atajos
        lbl_info = tk.Label(self, text="Enter: Agregar | C: Completar | Del: Eliminar | Esc: Salir", 
                            font=("Arial", 8), fg="gray")
        lbl_info.pack(pady=5)

    def _configurar_atajos(self):
        # Vinculación de eventos de teclado
        self.bind('<Return>', lambda e: self._accion_agregar())
        self.bind('<Delete>', lambda e: self._accion_eliminar())
        self.bind('<d>', lambda e: self._accion_eliminar()) # Alternativa 'd'
        self.bind('<c>', lambda e: self._accion_completar())
        self.bind('<Escape>', lambda e: self.destroy())

    def _accion_agregar(self):
        desc = self.entrada.get()
        if self.servicio.agregar_tarea(desc):
            self.entrada.delete(0, tk.END)
            self._refrescar_lista()
        else:
            messagebox.showwarning("Error", "La tarea no puede estar vacía")

    def _accion_completar(self):
        seleccion = self.lista_visual.curselection()
        if seleccion:
            self.servicio.completar_tarea(seleccion[0])
            self._refrescar_lista()

    def _accion_eliminar(self):
        seleccion = self.lista_visual.curselection()
        if seleccion:
            self.servicio.eliminar_tarea(seleccion[0])
            self._refrescar_lista()

    def _refrescar_lista(self):
        self.lista_visual.delete(0, tk.END)
        for tarea in self.servicio.obtener_todas():
            self.lista_visual.insert(tk.END, str(tarea))
            # Cambio de color si está completada
            if tarea.completada:
                self.lista_visual.itemconfig(tk.END, fg="green")