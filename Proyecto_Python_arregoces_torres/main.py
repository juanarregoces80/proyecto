import camper
import trainer
import ruta
import evaluacion
import reportes
import campuslands

def menu():
    while True:
        print("""
        ====== CAMPUSLANDS SYSTEM ======
        1. Registrar Camper
        2. Registrar Trainer
        3. Crear Ruta
        4. Evaluar Camper
        5. Asignar Camper a Ruta
        6. Reportes
        0. Salir
        """)
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            camper.registrar_camper()
        elif opcion == "2":
            trainer.registrar_trainer()
        elif opcion == "3":
            ruta.crear_ruta()
        elif opcion == "4":
            evaluacion.evaluar_camper()
        elif opcion == "5":
            campuslands.asignar_camper_ruta()
        elif opcion == "6":
            reportes.listar_inscritos()
            reportes.listar_aprobados()
            reportes.listar_trainers()
        elif opcion == "0":
            print("👋 Saliendo...")
            break
        else:
            print("❌ Opción inválida")

if __name__ == "__main__":
    menu()
