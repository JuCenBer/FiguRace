from http.client import PROXY_AUTHENTICATION_REQUIRED
import os
import json
import csv
from random import randint

def seleccionar_dificultad(dif_seleccionada):
    '''Recibe la dificultad seleccionada, obtiene el listado de dificultades y la configuración, y establece los valores de la nueva configuracion en base a los valores de la dificultad seleccionada'''
    dificultades = obtener_dificultades()
    config = obtener_config()
    config["valores"] = dificultades[dif_seleccionada]
    config["dificultad"] = dif_seleccionada
    guardar_config(config)

def obtener_dificultades():
    '''Retorna el listado de caracteristicas segun la dificultad'''
    dificultades = {"Facil": {"tiempo_ronda": 30.0, "cant_rondas": 5.0, "puntos_bien": 50.0, "puntos_mal": -10.0, "cant_carac": 5.0},
                    "Normal": {"tiempo_ronda": 20.0, "cant_rondas": 10.0, "puntos_bien": 50.0, "puntos_mal": -25.0, "cant_carac": 4.0}, 
                    "Dificil": {"tiempo_ronda": 10.0, "cant_rondas": 20.0, "puntos_bien": 50.0, "puntos_mal": -50.0, "cant_carac": 3.0}, 
                    "Einstein": {"tiempo_ronda": 5.0, "cant_rondas": 30.0, "puntos_bien": 60.0, "puntos_mal": -100.0, "cant_carac": 2.0}}
    return dificultades

def obtener_ultima_partida():
    '''Abre el archivo json que contiene la información de la ultima sesion, y retorna un diccionario. En caso de no existir, lo crea con valores por defecto'''
    try:
        with open(os.path.join(os.getcwd(), "src", "datos", "ultima_partida.json"), "r", encoding='utf-8') as partida:
            ultima_partida = json.load(partida)
    except:
        with open(os.path.join(os.getcwd(), "src", "datos", "ultima_partida.json"), "w", encoding='utf-8') as partida:
            ultima_partida = {"nick": "Sin datos", "dificultad": "Sin datos", "fecha": "Sin datos", "puntaje": "Sin datos"}
            json.dump(ultima_partida, partida)
    return ultima_partida

def guardar_ultima_partida(ultima_partida):
    '''Recibe la informacion de la ultima sesion y la guarda en el archivo de formato json'''
    with open(os.path.join(os.getcwd(), "src", "datos", "ultima_partida.json"), "w", encoding='utf-8') as partida:
        json.dump(ultima_partida, partida)

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
        config_def = {"valores" : {
                        "tiempo_ronda": 30,
                        "cant_rondas": 5,
                        "puntos_bien": 50,
                        "puntos_mal": -10,
                        "cant_carac": 5},
                      "dataset": "Aleatorio",
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

def guardar_partidas(eventos, id):
    with open(os.path.join(os.getcwd(), "src", "datos", "eventos_partidas.csv"), "a", encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=["timestamp","id","evento","usuarie","estado","texto_ingresado","respuesta","nivel"], lineterminator='\n')
        for evento in eventos:
            evento["id"] = id
            writer.writerow(evento)
                
def obtener_id_ultima_partida():
    ruta = os.path.join(os.getcwd(), "src", "datos", "eventos_partidas.csv")
    try:
        with open(ruta, "r") as archivo:
            reader = csv.reader(archivo, delimiter=",")
            lista_partidas = list(reader)
            id = int(lista_partidas[len(lista_partidas)-1][1]) + 1
    except:
        with open(ruta, "w", encoding='utf-8') as archivo:
            writer = csv.writer(archivo, lineterminator="\n")
            encabezado = ["timestamp", "id","evento", "usuarie", "estado", "texto_ingresado", "respuesta", "nivel"]
            writer.writerow(encabezado)
            id = 1
    return id

def guardar_puntajes(puntajes, dificultad, nick, puntaje):
    try:
        puntajes[dificultad][nick].append(puntaje)
    except:
        puntajes[dificultad].update({nick:[puntaje]})
    
    with open(os.path.join(os.getcwd(), "src", "datos", "puntajes.json"), "w", encoding='utf-8') as archivo:
        json.dump(puntajes, archivo)

def obtener_puntajes():
    try:
        with open(os.path.join(os.getcwd(), "src", "datos", "puntajes.json"), "r", encoding='utf-8') as archivo:
            puntajes = json.load(archivo)
    except:
        with open(os.path.join(os.getcwd(), "src", "datos", "puntajes.json"), "w", encoding='utf-8') as archivo:
            puntajes = {"Facil": [],
                        "Normal": [],
                        "Dificil": [],
                        "Einstein": []
                        }
    return puntajes
