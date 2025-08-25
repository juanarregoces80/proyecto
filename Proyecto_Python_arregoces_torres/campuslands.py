from utils import cargar_datos, guardar_datos

def asignar_camper_ruta():
    data = cargar_datos()
    camper_id = input("ID del camper aprobado: ")
    ruta = input("Ruta asignada: ")
    trainer_id = input("ID del trainer: ")
    matricula = {
        "camper_id": camper_id,
        "ruta": ruta,
        "trainer_id": trainer_id,
        "salon": input("Salón: "),
        "fecha_inicio": input("Fecha inicio: "),
        "fecha_fin": input("Fecha finalización: ")
    }
    data["matriculas"].append(matricula)
    guardar_datos(data)
    print("✅ Matrícula registrada con éxito")
