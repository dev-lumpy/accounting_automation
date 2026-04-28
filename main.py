import tkinter as tk

class VentanaAsiento:
    def __init__(self):
        self.root = tk.Tk()
        self.configurar_ventana()
        self.crear_widgets()

    def configurar_ventana(self):
        self.root.title("Ventana fija")

        # Tamaño y posición
        self.root.geometry("400x300+200+100")

        # No redimensionable
        # self.root.resizable(False, False)

        # Siempre encima
        self.root.attributes("-topmost", True)

    def crear_widgets(self):
        self.label = tk.Label(self.root, text="Ventana fija arriba")
        self.label.pack(pady=50)

    def ejecutar(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = VentanaAsiento()
    app.ejecutar()