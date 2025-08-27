import json
from modules.campuslands import CampusLands
from modules import camper, trainer, ruta, evaluacion, reportes

def main():
    campus = CampusLands()
    campus.cargar_datos()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Gestión de Campers")
        print("2. Gestión de Trainers")
        print("3. Gestión de Rutas")
        print("4. Reportes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            camper.menu_campers(campus)
            campus.guardar_datos()
        elif opcion == '2':
            trainer.menu_trainers(campus)
            campus.guardar_datos()
        elif opcion == '3':
            ruta.menu_rutas(campus)
            campus.guardar_datos()
        elif opcion == '4':
            reportes.menu_reportes(campus)
        elif opcion == '5':
            campus.guardar_datos()
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()