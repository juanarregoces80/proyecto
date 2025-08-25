from utils import cargar_datos

def listar_inscritos():
    data = cargar_datos()
    print("\n📌 Campers Inscritos:")
    for c in data["campers"]:
        if c["estado"] == "Inscrito":
            print(f"- {c['nombres']} {c['apellidos']} ({c['id']})")

def listar_aprobados():
    data = cargar_datos()
    print("\n📌 Campers Aprobados:")
    for c in data["campers"]:
        if c["estado"] == "Aprobado":
            print(f"- {c['nombres']} {c['apellidos']} ({c['id']})")

def listar_trainers():
    data = cargar_datos()
    print("\n📌 Trainers registrados:")
    for t in data["trainers"]:
        print(f"- {t['nombres']} {t['apellidos']} ({t['especialidad']})")
