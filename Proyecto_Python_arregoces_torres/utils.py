import json

DATA_FILE = "data.json"

def cargar_datos():
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"campers": [], "trainers": [], "rutas": [], "evaluaciones": [], "matriculas": []}

def guardar_datos(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
