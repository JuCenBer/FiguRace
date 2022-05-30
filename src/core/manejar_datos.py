import os
import json
import csv
from random import randint

def seleccionar_dificultad(dif_seleccionada):
    dificultades = obtener_dificultades()
    config = obtener_config()
    for key in dificultades: config[key] = dificultades[key][dif_seleccionada]
    config["dificultad"] = dif_seleccionada
    guardar_config(config)

def obtener_dificultades():
    try:
        with open(os.path.join(os.getcwd(), "src", "datos", "dificultades.json"), "r", encoding='utf-8') as archivo:
            dificultades = json.load(archivo)
            return dificultades[0]
    except:
        with open(os.path.join(os.getcwd(), "src", "datos", "dificultades.json"), "w", encoding='utf-8') as archivo:
            dificultades = {"tiempo_ronda": {"Facil":30.0, "Normal":20.0, "Dificil":10.0, "Einstein": 5.0},
                            "cant_rondas": {"Facil":5.0, "Normal":10.0, "Dificil":20.0, "Einstein": 30.0},
                            "puntos_bien": {"Facil":50.0, "Normal":50.0, "Dificil":50.0, "Einstein": 60.0},
                            "puntos_mal": {"Facil":-10.0, "Normal":-25.0, "Dificil":-50.0, "Einstein": -100.0},
                            "cant_carac": {"Facil":5.0, "Normal":4.0, "Dificil":3.0, "Einstein": 2.0}}
            json.dump(dificultades)
    return dificultades

def obtener_ultima_sesion():
    try:
        with open(os.path.join(os.getcwd(), "src", "datos", "ultima_sesion.json"), "r", encoding='utf-8') as sesion:
            sesion_actual = json.load(sesion)
    except:
        with open(os.path.join(os.getcwd(), "src", "datos", "ultima_sesion.json"), "w", encoding='utf-8') as sesion:
            sesion_actual = {"nick":"", "dificultad":"facil", "puntaje":0, "fecha":"-"}
    return sesion_actual

def guardar_ultima_sesion(sesion_actual):
    with open(os.path.join(os.getcwd(), "src", "datos", "ultima_sesion.json"), "w", encoding='utf-8') as sesion:
        json.dump(sesion_actual, sesion)

def obtener_perfiles():
    '''Abre el archivo json de perfiles y retorna el listado de perfiles. En caso de que no exista, se crea el archivo y se retorna una lista vacia'''
    try:
        with open(os.path.join(os.getcwd(), "src", "datos", "perfiles.json"), "r", encoding='utf-8') as perfiles:
            jugadores = json.load(perfiles)
    except:
        with open(os.path.join(os.getcwd(), "src", "datos", "perfiles.json"), "w", encoding='utf-8') as perfiles:
            jugadores = []
    return jugadores

def guardar_perfiles(jugadores):
    '''Recibe el listado de jugadores, abre el archivo json de perfiles y lo almacena ahi'''
    with open(os.path.join(os.getcwd(), "src", "datos", "perfiles.json"), "w", encoding='utf-8') as perfiles:
        json.dump(jugadores, perfiles)


def obtener_nombres_datasets():
    ruta = os.path.join(os.getcwd(), "src", "datos", "nombres_datasets.json")
    try:
        with open(ruta, "r") as archivo:
            datos_archivo = json.load(archivo)
            nombres = datos_archivo["nombres"]
            return nombres
    except:
        return []


def obtener_config():
    ruta = os.path.join(os.getcwd(), "src", "datos", "config.json")
    try:
        with open(ruta, "r") as archivo:
            datos_archivo = json.load(archivo)
            return datos_archivo[0]
    except:
        config_def = {"dataset": "Aleatorio",
                      "tiempo_ronda": 30,
                      "cant_rondas": 5,
                      "puntos_bien": 50,
                      "puntos_mal": -10,
                      "cant_carac": 5,
                      "dificultad": "Facil"}
        return config_def


def guardar_config(dicc):
    ruta = os.path.join(os.getcwd(), "src", "datos", "config.json")
    with open(ruta, "w") as archivo:
        dicc_json = []
        dicc_json.append(dicc)
        json.dump(dicc_json, archivo)

def obtener_top_puntajes():
    ruta = os.path.join(os.getcwd(), "src", "datos", "config.json")
    
    return []

def obtener_dataset(nombre_dataset):
    nombres_datasets = ["erupciones_formateado.csv", "lagos_formateado.csv", "peliculas_formateado.csv", "jugadores_formateado.csv"]

    if nombre_dataset == "Aleatorio":
        nombre_dataset = nombres_datasets[randint(0,len(nombres_datasets)-1)]
    else:
        nombre_dataset = nombre_dataset.lower().split()[0] + "_formateado.csv"

    ruta = os.path.join(os.getcwd(), "src", "datasets", nombre_dataset)

    with open(ruta,'r',encoding='utf-8') as archivo:
        reader = csv.reader(archivo)
        lista = list(reader)
    return lista