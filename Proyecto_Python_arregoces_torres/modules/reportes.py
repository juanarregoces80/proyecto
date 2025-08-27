def menu_reportes(campus):
    while True:
        print("\n--- Menú Reportes ---")
        print("1. Listar Campers Inscritos")
        print("2. Listar Campers Aprobados (Examen Inicial)")
        print("3. Listar Trainers")
        print("4. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            listar_campers_inscritos(campus)
        elif opcion == '2':
            listar_campers_aprobados(campus)
        elif opcion == '3':
            listar_trainers(campus)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def listar_campers_inscritos(campus):
    print("\n--- Listar Campers Inscritos ---")
    campers = campus.obtener_campers()
    campers_inscritos = [c for c in campers if c["estado"] == "En proceso de ingreso"]
    if campers_inscritos:
        for camper in campers_inscritos:
            print(f"Identificación: {camper['identificacion']}, Nombres: {camper['nombres']}, Apellidos: {camper['apellidos']}")
    else:
        print("No hay campers inscritos.")

def listar_campers_aprobados(campus):
    print("\n--- Listar Campers Aprobados (Examen Inicial) ---")
    campers = campus.obtener_campers()
    campers_aprobados = [c for c in campers if c["estado"] == "Aprobado"]
    if campers_aprobados:
        for camper in campers_aprobados:
            print(f"Identificación: {camper['identificacion']}, Nombres: {camper['nombres']}, Apellidos: {camper['apellidos']}")
    else:
        print("No hay campers aprobados.")

def listar_trainers(campus):
    print("\n--- Listar Trainers ---")
    trainers = campus.obtener_trainers()
    if trainers:
        for trainer in trainers:
            print(f"Identificación: {trainer['identificacion']}, Nombres: {trainer['nombres']}, Apellidos: {trainer['apellidos']}")
    else:
        print("No hay trainers registrados.")