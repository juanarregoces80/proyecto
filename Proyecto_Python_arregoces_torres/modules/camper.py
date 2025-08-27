def menu_campers(campus):
    while True:
        print("\n--- Menú Campers ---")
        print("1. Registrar Camper")
        print("2. Evaluar Camper (Examen Inicial)")
        print("3. Listar Campers")
        print("4. Asignar Camper a Ruta")
        print("5. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_camper(campus)
        elif opcion == '2':
            evaluar_camper(campus)
        elif opcion == '3':
            listar_campers(campus)
        elif opcion == '4':
            asignar_camper_a_ruta(campus)
        elif opcion == '5':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def registrar_camper(campus):
    print("\n--- Registrar Camper ---")
    identificacion = input("Número de Identificación: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    direccion = input("Dirección: ")
    acudiente = input("Acudiente: ")
    telefono_celular = input("Teléfono Celular: ")
    telefono_fijo = input("Teléfono Fijo: ")
    estado = "En proceso de ingreso"
    riesgo = "Bajo"

    nuevo_camper = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "direccion": direccion,
        "acudiente": acudiente,
        "telefono_celular": telefono_celular,
        "telefono_fijo": telefono_fijo,
        "estado": estado,
        "riesgo": riesgo,
        "ruta_asignada": None
    }

    campus.agregar_camper(nuevo_camper)
    print("Camper registrado con éxito.")

def evaluar_camper(campus):
    print("\n--- Evaluar Camper (Examen Inicial) ---")
    identificacion = input("Número de Identificación del Camper: ")

    campers = campus.obtener_campers()
    camper = next((c for c in campers if c["identificacion"] == identificacion), None)

    if camper:
        nota_teorica = float(input("Nota Teórica: "))
        nota_practica = float(input("Nota Práctica: "))
        promedio = (nota_teorica + nota_practica) / 2

        if promedio >= 60:
            camper["estado"] = "Aprobado"
            print(f"El camper {camper['nombres']} {camper['apellidos']} ha sido Aprobado.")
        else:
            camper["estado"] = "Reprobado"
            print(f"El camper {camper['nombres']} {camper['apellidos']} ha sido Reprobado.")
    else:
        print("No se encontró ningún camper con esa identificación.")

def listar_campers(campus):
    print("\n--- Listar Campers ---")
    campers = campus.obtener_campers()
    if campers:
        for camper in campers:
            print(f"Identificación: {camper['identificacion']}, Nombres: {camper['nombres']}, Apellidos: {camper['apellidos']}, Estado: {camper['estado']}")
    else:
        print("No hay campers registrados.")

def asignar_camper_a_ruta(campus):
    print("\n--- Asignar Camper a Ruta ---")
    identificacion = input("Número de Identificación del Camper: ")
    campers = campus.obtener_campers()
    camper = next((c for c in campers if c["identificacion"] == identificacion), None)

    if not camper:
        print("No se encontró ningún camper con esa identificación.")
        return

    if camper["estado"] != "Aprobado":
        print("El camper no ha sido aprobado en el examen inicial.")
        return

    rutas = campus.obtener_rutas()
    if not rutas:
        print("No hay rutas disponibles. Primero debe crear una ruta.")
        return

    print("\n--- Rutas Disponibles ---")
    for i, ruta in enumerate(rutas):
        print(f"{i+1}. {ruta['nombre']}")

    ruta_index = int(input("Seleccione el número de la ruta a asignar: ")) - 1
    if 0 <= ruta_index < len(rutas):
        ruta_seleccionada = rutas[ruta_index]
        camper["ruta_asignada"] = ruta_seleccionada["nombre"]
        print(f"Camper asignado a la ruta {ruta_seleccionada['nombre']} con éxito.")
    else:
        print("Opción no válida.")