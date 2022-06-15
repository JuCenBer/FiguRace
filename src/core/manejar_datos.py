import os
import json
import csv
from random import randint

def seleccionar_dificultad(dif_seleccionada):
    '''Recibe la dificultad seleccionada, obtiene el listado de dificultades y la configuración, y establece los valores de la nueva configuracion en base a los valores de la dificultad seleccionada'''
    dificultades = obtener_dificultades()
    config = obtener_config()
    for key in dificultades: config[key] = dificultades[key][dif_seleccionada]
    config["dificultad"] = dif_seleccionada
    guardar_config(config)

def obtener_dificultades():
    '''Retorna el listado de caracteristicas segun la dificultad'''
    dificultades = {"tiempo_ronda": {"Facil":30.0, "Normal":20.0, "Dificil":10.0, "Einstein": 5.0},
                    "cant_rondas": {"Facil":5.0, "Normal":10.0, "Dificil":20.0, "Einstein": 30.0},
                    "puntos_bien": {"Facil":50.0, "Normal":50.0, "Dificil":50.0, "Einstein": 60.0},
                    "puntos_mal": {"Facil":-10.0, "Normal":-25.0, "Dificil":-50.0, "Einstein": -100.0},
                    "cant_carac": {"Facil":5.0, "Normal":4.0, "Dificil":3.0, "Einstein": 2.0}}
    return dificultades

def obtener_ultima_sesion():
    '''Abre el archivo json que contiene la información de la ultima sesion, y retorna un diccionario. En caso de no existir, lo crea con valores por defecto'''
    try:
        with open(os.path.join(os.getcwd(), "src", "datos", "ultima_sesion.json"), "r", encoding='utf-8') as sesion:
            sesion_actual = json.load(sesion)
    except:
        with open(os.path.join(os.getcwd(), "src", "datos", "ultima_sesion.json"), "w", encoding='utf-8') as sesion:
            sesion_actual = {"nick":"", "dificultad":"facil", "puntaje":0, "fecha":"-"}
    return sesion_actual

def guardar_ultima_sesion(sesion_actual):
    '''Recibe la informacion de la ultima sesion y la guarda en el archivo de formato json'''
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


def obtener_config():
    '''Abre el archivo json del config y retorna un diccionario con los valores de la configuracion. Si no existe, crea uno y retorna un diccionario con valores por defecto equivalentes a la dificultad Facil y con dataset Aleatorio.'''
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
                      "dificultad": "Facil",
                      "nick": ""}
        return config_def


def guardar_config(dicc):
    '''Recibe el diccionario con los valores de la configuracion y los guarda en el archivo json de configuracion'''
    ruta = os.path.join(os.getcwd(), "src", "datos", "config.json")
    with open(ruta, "w") as archivo:
        dicc_json = []
        dicc_json.append(dicc)
        json.dump(dicc_json, archivo)

#Se utilizara en la segunda entrega para la pantalla de puntajes 
#def obtener_top_puntajes():
#    ruta = os.path.join(os.getcwd(), "src", "datos", "config.json")   
#    return []

def obtener_dataset(nombre_dataset):
    '''Recibe el nombre del dataset y chequea si es aleatorio o no. Retorna el dataset elegido, ya sea al azar o no, en forma de lista'''
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

def guardar_evento(evento):
    try:
        with open(os.path.join(os.getcwd(), "src", "datos", "dificultades.json"), "r", encoding='utf-8') as archivo:
            dificultades = json.load(archivo)
            return dificultades[0]
    except:
        with open(os.path.join(os.getcwd(), "src", "datos", "dificultades.json"), "w", encoding='utf-8') as archivo:
            dificultades = {"tiempo_ronda": {"Facil": 30.0, "Normal": 20.0, "Dificil": 10.0, "Einstein": 5.0},
                            "cant_rondas": {"Facil": 5.0, "Normal": 10.0, "Dificil": 20.0, "Einstein": 30.0},
                            "puntos_bien": {"Facil": 50.0, "Normal": 50.0, "Dificil": 50.0, "Einstein": 60.0},
                            "puntos_mal": {"Facil": -10.0, "Normal": -25.0, "Dificil": -50.0, "Einstein": -100.0},
                            "cant_carac": {"Facil": 5.0, "Normal": 4.0, "Dificil": 3.0, "Einstein": 2.0}}
            json.dump(dificultades)
    return dificultades
