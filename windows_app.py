
import tkinter as tk

from lib import app_geometry
from lib import cargar_ventana


class WindowAsiento(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configurar_ventana()
        self.crear_widgets()

        # Hijos
        self.plan = WindowPlanCuentas(self)
        self.lista = WindowListAsiento(self)

    def configurar_ventana(self):
        self.title("Ventana fija")

        # Aplicar geometría guardada
        datos = cargar_ventana("ASIENTO")
        app_geometry(self, datos)

        # No redimensionable
        self.resizable(False, False)

        # Siempre encima
        self.attributes("-topmost", True)

    def crear_widgets(self):
        self.label = tk.Label(self, text="Ventana fija arriba")
        self.label.pack(pady=50)

    def ejecutar(self):
        self.mainloop()

class WindowPlanCuentas(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.configurar_ventana()
        self.crear_widgets()

    def configurar_ventana(self):
        self.title("Plan de cuentas")

        # Aplicar geometría guardada
        datos = cargar_ventana("PLAN_CUENTAS")
        app_geometry(self, datos)

    def crear_widgets(self):
        tk.Label(self, text="Plan de cuentas").pack(pady=50)


class WindowListAsiento(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.withdraw()  # Oculta la ventana inicialmente
        self.configurar_ventana()
        self.crear_widgets()


    def configurar_ventana(self):
        self.title("Lista de asientos")

        # Aplicar geometría guardada
        datos = cargar_ventana("LISTA_ASIENTOS")
        app_geometry(self, datos)

    def crear_widgets(self):
        tk.Label(self, text="Lista de asientos").pack(pady=50)