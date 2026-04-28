from main import VentanaAsiento
from lib import guardar_ventana

app = VentanaAsiento()

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
                size, x, y = app.root.geometry().split("+")

                width, height = size.split("x")

                guardar_ventana("ASIENTO", {
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
    geo = app.root.geometry()
    print(geo)
    size_pos = geo.split("+")
    
    ancho_alto = size_pos[0]
    x = int(size_pos[1])
    y = int(size_pos[2])

    # Modificar posición
    x += dx
    y += dy

    # Aplicar nueva geometría
    app.root.geometry(f"{ancho_alto}+{x}+{y}")

print("Listo para mover la ventana.")
# Bind de teclas
app.root.bind("<Key>", handler)
print("Usa Ctrl + Numpad 4/6/8/2 para mover la ventana.")

app.ejecutar()


$urlRepo = "https://github.com/torvalds/linux"

# Extraer owner/repo desde la URL
$path = ([uri]$urlRepo).AbsolutePath.Trim("/")
$apiUrl = "https://api.github.com/repos/$path"

try {
    Invoke-WebRequest $apiUrl -Method Head -Headers @{ "User-Agent"="PowerShell" } | Out-Null
    "EXISTE"
}
catch {
    "NO EXISTE"
}