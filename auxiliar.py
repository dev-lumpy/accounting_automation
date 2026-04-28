from tkinter import Tk

from lib import guardar_ventana
from windows_app import WindowError

root = Tk()

app = WindowError(root)
app.message("¡Error! No se pudo cargar la geometría guardada. Se aplicará la geometría por defecto.").show()

ventana_ejecutar = root

def handler(event):
    if (event.state & 0x4):
        match event.keysym:
            case "Left":
                mover(dx=-5)
            case "Right":
                mover(dx=5)
            case "Up":
                mover(dy=-5)
            case "Down":
                mover(dy=5)

            case "p":
                print("Guardando posición...")
                size, x, y = app.geometry().split("+")

                width, height = size.split("x")

                guardar_ventana(app.tag, {
                    "x": int(x),
                    "y": int(y),
                    "width": int(width),
                    "height": int(height)
                })
                print("Posición guardada.")
            


print("Ventana creada. Puedes moverla con Ctrl + Numpad 4/6/8/2.")
def mover(dx=0, dy=0):
    # Obtener geometría actual
    print("Moviendo ventana...")
    geo = app.geometry()
    print(geo)
    size_pos = geo.split("+")
    
    ancho_alto = size_pos[0]
    x = int(size_pos[1])
    y = int(size_pos[2])

    # Modificar posición
    x += dx
    y += dy

    # Aplicar nueva geometría
    app.geometry(f"{ancho_alto}+{x}+{y}")

print("Listo para mover la ventana.")
# Bind de teclas
app.bind("<Key>", handler)
print("Usa Ctrl + Numpad 4/6/8/2 para mover la ventana.")

ventana_ejecutar.mainloop()
