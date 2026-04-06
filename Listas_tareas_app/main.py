from servicios.servicio_tarea import TareaServicio
from ui.app_tkinter import AppTarea

if __name__ == "__main__":
    servicio = TareaServicio()
    app = AppTarea(servicio)
    app.mainloop()