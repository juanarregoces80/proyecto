from utils import cargar_datos, guardar_datos

def crear_ruta():
    data = cargar_datos()
    ruta = {
        "nombre": input("Nombre de la ruta: "),
        "modulos": [
            "Fundamentos de programación",
            "Programación Web",
            "Programación formal",
            "Bases de datos",
            "Backend"
        ],
        "capacidad": 33
    }
    data["rutas"].append(ruta)
    guardar_datos(data)
    print("✅ Ruta creada con éxito")
