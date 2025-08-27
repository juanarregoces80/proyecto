def menu_trainers(campus):
    while True:
        print("\n--- Menú Trainers ---")
        print("1. Registrar Trainer")
        print("2. Listar Trainers")
        print("3. Asignar Trainer a Ruta")
        print("4. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_trainer(campus)
        elif opcion == '2':
            listar_trainers(campus)
        elif opcion == '3':
            asignar_trainer_a_ruta(campus)
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def registrar_trainer(campus):
    print("\n--- Registrar Trainer ---")
    identificacion = input("Número de Identificación: ")
    nombres = input("Nombres: ")
    apellidos = input("Apellidos: ")
    telefono_celular = input("Teléfono Celular: ")
    ruta_asignada = None

    nuevo_trainer = {
        "identificacion": identificacion,
        "nombres": nombres,
        "apellidos": apellidos,
        "telefono_celular": telefono_celular,
        "ruta_asignada": ruta_asignada
    }

    campus.agregar_trainer(nuevo_trainer)
    print("Trainer registrado con éxito.")

def listar_trainers(campus):
    print("\n--- Listar Trainers ---")
    trainers = campus.obtener_trainers()
    if trainers:
        for trainer in trainers:
            print(f"Identificación: {trainer['identificacion']}, Nombres: {trainer['nombres']}, Apellidos: {trainer['apellidos']}")
    else:
        print("No hay trainers registrados.")

def asignar_trainer_a_ruta(campus):
    print("\n--- Asignar Trainer a Ruta ---")
    identificacion = input("Número de Identificación del Trainer: ")
    trainers = campus.obtener_trainers()
    trainer = next((t for t in trainers if t["identificacion"] == identificacion), None)

    if not trainer:
        print("No se encontró ningún trainer con esa identificación.")
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
        trainer["ruta_asignada"] = ruta_seleccionada["nombre"]
        print(f"Trainer asignado a la ruta {ruta_seleccionada['nombre']} con éxito.")
    else:
        print("Opción no válida.")