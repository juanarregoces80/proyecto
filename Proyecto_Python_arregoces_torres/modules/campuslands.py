import json

class CampusLands:
    def __init__(self, archivo_datos='data/campuslands.json'):
        self.archivo_datos = archivo_datos
        self.data = {
            "campers": [],
            "trainers": [],
            "rutas": [],
            "areas": []
        }

    def cargar_datos(self):
        try:
            with open(self.archivo_datos, 'r') as file:
                self.data = json.load(file)
        except FileNotFoundError:
            print("Archivo de datos no encontrado. Se creará uno nuevo.")
        except json.JSONDecodeError:
            print("Error al decodificar el archivo JSON. Se utilizarán datos predeterminados.")
            self.data = {
                "campers": [],
                "trainers": [],
                "rutas": [],
                "areas": []
            }

    def guardar_datos(self):
        try:
            with open(self.archivo_datos, 'w') as file:
                json.dump(self.data, file, indent=4)
            print("Datos guardados con éxito.")
        except Exception as e:
            print(f"Error al guardar los datos: {e}")

    def agregar_camper(self, camper):
        self.data["campers"].append(camper)

    def agregar_trainer(self, trainer):
        self.data["trainers"].append(trainer)

    def agregar_ruta(self, ruta):
        self.data["rutas"].append(ruta)

    def obtener_campers(self):
        return self.data["campers"]

    def obtener_trainers(self):
        return self.data["trainers"]

    def obtener_rutas(self):
        return self.data["rutas"]