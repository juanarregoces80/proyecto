def menu_rutas(campus):
    while True:
        print("\n--- Menú Rutas ---")
        print("1. Crear Ruta")
        print("2. Listar Rutas")
        print("3. Volver al Menú Principal")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            crear_ruta(campus)
        elif opcion == '2':
            listar_rutas(campus)
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def crear_ruta(campus):
    print("\n--- Crear Ruta ---")
    nombre = input("Nombre de la Ruta: ")
    modulos = input("Módulos (separados por comas): ").split(',')
    sgbd_principal = input("SGBD Principal: ")
    sgbd_alternativo = input("SGBD Alternativo: ")

    nueva_ruta = {
        "nombre": nombre,
        "modulos": [m.strip() for m in modulos],
        "sgbd_principal": sgbd_principal,
        "sgbd_alternativo": sgbd_alternativo
    }

    campus.agregar_ruta(nueva_ruta)
    print("Ruta creada con éxito.")

def listar_rutas(campus):
    print("\n--- Listar Rutas ---")
    rutas = campus.obtener_rutas()
    if rutas:
        for ruta in rutas:
            print(f"Nombre: {ruta['nombre']}, Módulos: {', '.join(ruta['modulos'])}, SGBD Principal: {ruta['sgbd_principal']}, SGBD Alternativo: {ruta['sgbd_alternativo']}")
    else:
        print("No hay rutas registradas.")