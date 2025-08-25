from utils import cargar_datos, guardar_datos

def evaluar_camper():
    data = cargar_datos()
    camper_id = input("Ingrese ID del camper: ")
    teoria = float(input("Nota teórica: "))
    practica = float(input("Nota práctica: "))

    promedio = (teoria + practica) / 2
    estado = "Aprobado" if promedio >= 60 else "Reprobado"

    evaluacion = {
        "camper_id": camper_id,
        "teoria": teoria,
        "practica": practica,
        "promedio": promedio,
        "estado": estado
    }
    data["evaluaciones"].append(evaluacion)

    # Actualizar estado del camper
    for c in data["campers"]:
        if c["id"] == camper_id:
            c["estado"] = "Aprobado" if promedio >= 60 else "Inscrito"

    guardar_datos(data)
    print(f"✅ Evaluación registrada. Estado del camper: {estado}")
