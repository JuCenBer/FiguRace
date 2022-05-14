import os
import json


def obtener_perfiles():
    try:
        with open(os.path.join(os.getcwd(), "src", "datos", "perfiles.json"), "r", encoding='utf-8') as perfiles:
            jugadores = json.load(perfiles)  # intento cargar el json
    except:
        with open(os.path.join(os.getcwd(), "src", "datos", "perfiles.json"), "w", encoding='utf-8') as perfiles:
            jugadores = []
    return jugadores


def guardar_perfiles(jugadores):
    with open(os.path.join(os.getcwd(), "src", "datos", "perfiles.json"), "w", encoding='utf-8') as perfiles:
        json.dump(jugadores, perfiles)


def obtener_nombres_datasets():
    ruta = os.path.join(os.getcwd(), "src", "datos", "nombres_datasets.json")
    try:
        with open(ruta, "r") as archivo:
            datos_archivo = json.load(archivo)
            nombres = datos_archivo[0].values()
            return nombres
    except:
        return []


def obtener_config():
    ruta = os.path.join(os.getcwd(), "src", "datos", "config.json")
    try:
        with open(ruta, "r") as archivo:
            datos_archivo = json.load(archivo)
            config = datos_archivo[0]
            return config
    except:
        config_def = {"dataset": "Volcanes",
                      "tiempo_ronda": 10,
                      "cant_rondas": 5,
                      "puntos_bien": 2,
                      "puntos_mal": -1,
                      "cant_carac": 3}
        return config_def


def guardar_config(dicc):
    ruta = os.path.join(os.getcwd(), "src", "datos", "config.json")
    with open(ruta, "w") as archivo:
        dicc_json = []
        dicc_json.append(dicc)
        json.dump(dicc_json, archivo)
