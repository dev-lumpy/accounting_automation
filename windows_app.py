import tkinter as tk
from tkinter import scrolledtext

from lib import app_geometry
from lib import cargar_ventana


class WindowAsiento(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tag = "ASIENTO"
        self.configurar_ventana()
        self.crear_widgets()

        # Hijos
        self.plan = WindowPlanCuentas(self)
        self.lista = WindowListAsiento(self)
        self.error = WindowError(self)

    def configurar_ventana(self):
        self.title("Ventana fija")

        # Aplicar geometría guardada
        datos = cargar_ventana("ASIENTO")
        app_geometry(self, datos)

        # No redimensionable
        # self.resizable(False, False)

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
        self.tag = "PLAN_CUENTAS"
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
        self.tag = "LISTA_ASIENTOS"
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


class WindowError(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.title("Error - Traceback")
        self.tag = "ERROR_TRACEBACK"
        self.configure(bg="#1e1e1e")

        self.protocol("WM_DELETE_WINDOW", self.cerrar)

        self.withdraw()  # 👈 oculto hasta que se muestre
    
    def configurar_ventana(self):
        self.title("Error - Traceback")

        # Aplicar geometría guardada
        datos = cargar_ventana("ERROR_TRACEBACK")
        app_geometry(self, datos)

        self.deiconify()
        self.lift()
        self.focus_force()

    def __crear_widgets(self):
        # evitar duplicación
        if hasattr(self, "texto"):
            return

        tk.Label(
            self,
            text="Se ha producido un error",
            fg="red",
            bg="#1e1e1e",
            font=("Arial", 12, "bold")
        ).pack(pady=(10, 5))

        self.texto = scrolledtext.ScrolledText(
            self,
            width=80,
            height=20,
            bg="#2b2b2b",
            fg="#ff5555",
            insertbackground="white"
        )
        self.texto.pack(padx=10, pady=10, fill="both", expand=True)

        self.texto.insert("1.0", self.mensaje)
        self.texto.configure(state="disabled")

    def ajustar_tamano(self):
        self.update_idletasks()

        lineas = self.texto.get("1.0", "end").count("\n")

        ancho = 600
        alto = min(200 + lineas * 15, 600)

        x = self.parent.winfo_x() + 100
        y = self.parent.winfo_y() + 100

        self.geometry(f"{ancho}x{alto}+{x}+{y}")

    def message(self, texto):
        self.mensaje = texto
        return self

    def show(self):
        self.__crear_widgets()
        self.ajustar_tamano()

    def cerrar(self):
        self.destroy()