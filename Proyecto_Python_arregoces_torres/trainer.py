from utils import cargar_datos, guardar_datos

def registrar_trainer():
    data = cargar_datos()
    trainer = {
        "id": input("ID Trainer: "),
        "nombres": input("Nombres: "),
        "apellidos": input("Apellidos: "),
        "especialidad": input("Especialidad: ")
    }
    data["trainers"].append(trainer)
    guardar_datos(data)
    print("✅ Trainer registrado con éxito")
