from utils import cargar_datos, guardar_datos

def registrar_camper():
    data = cargar_datos()
    camper = {
        "id": input("ID: "),
        "nombres": input("Nombres: "),
        "apellidos": input("Apellidos: "),
        "direccion": input("Dirección: "),
        "acudiente": input("Acudiente: "),
        "telefono": input("Teléfono celular: "),
        "telefono_fijo": input("Teléfono fijo: "),
        "estado": "Inscrito",
        "riesgo": "Ninguno"
    }
    data["campers"].append(camper)
    guardar_datos(data)
    print("✅ Camper registrado con éxito")
