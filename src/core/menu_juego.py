from lib2to3.pgen2.pgen import generate_grammar
from random import randrange, shuffle, choices
import PySimpleGUI as sg
from . import manejar_datos
from . import menu_principal as menu
import csv

def generar_opciones(dataset):
    lineas = choices(dataset, k=5)
    opcion_correcta = [sg.Button(lineas[0][5].title(), button_color=('black', 'white'), size=(60, 1), font=("Helvetica", 10), key="-OPCION CORRECTA-")]
    linea_correcta = lineas[0]
    opciones = [opcion_correcta]
    for i in range(1,5):
        boton_incorrecto = [sg.Button(lineas[i][5].title(), button_color=('black', 'white'), size=(60, 1), font=("Helvetica", 10), key="-OPCION INCORRECTA "+str(i)+"-")]
        opciones.append(boton_incorrecto)
        
    shuffle(opciones)
    return opciones, linea_correcta

def obtener_caracteristicas(config,encabezado,linea_correcta):
    caracteristicas = []
    for i in range(int(config["cant_carac"])):
        carac = [sg.Text(encabezado[i].title() + ": " + linea_correcta[i].title(),font=("Helvetica", 12))]
        caracteristicas.append(carac)
    return caracteristicas

def generar_layout(config,dataset):
    encabezado = dataset[0]
    cuenta_regresiva= config["tiempo_ronda"] #hacer cuenta elemento_contador
    elemento_contador= [[sg.Text("TIEMPO: ",font=("bold", 15), text_color= "white",justification = "right")],
    [sg.Text(cuenta_regresiva,font=("bold", 15),justification = "left", text_color= "white",key="-CONTADOR-")]]

    puntajes= []

    opciones, linea_correcta = generar_opciones(dataset)
    caracteristicas = obtener_caracteristicas(config,encabezado,linea_correcta)

    layout = [
        #Cuenta Regresiva
        elemento_contador,
        #Caracteristicas
        caracteristicas,
        #Opciones a elegir para pasar (son 5)
        opciones,
        #Puntaje actual
        puntajes,
        #Boton pasar (se pierde la ronda)
        [sg.Button("Pasar",button_color=('white', 'red'), size=(60, 1), font=("Helvetica", 10),key="-PASAR-")],
        #Volver menu (Se pierde actual y restantes)
        #sg.Button('1', button_color=('white', 'blue'), size=(5, 1), font=("Helvetica", 20))
        [sg.Button("Volver al Menu", button_color=('white', 'red'), size=(60, 1), font=("Helvetica", 10), key="-ABANDONO-")]
        #Popup mensaje final   
    ]
    return layout

ronda= 0
def iniciar_pantalla_juego():
    config = manejar_datos.obtener_config()
    cuenta_regresiva= config["tiempo_ronda"] #hacer cuenta elemento_contador
    dataset = manejar_datos.obtener_dataset(config["dataset"])

    window = sg.Window("Menu de juego", layout = generar_layout(config,dataset), size=(500, 500), finalize=True)
    while True:
        event, values = window.read(timeout=1000)
    
        print(f"{event} {values}")

        if event == sg.WIN_CLOSED:
            menu.crear_ventana_principal
            break
    
        if event == "-ABANDONO-":
            menu.crear_ventana_principal
            break
            
        elif event == "__TIMEOUT__":
            # Incrementamos el cuenta_regresiva
            if cuenta_regresiva > 0: cuenta_regresiva -= 1
            # Obtenemos el elemento "-CONTADOR-"
            elemento_contador = window["-CONTADOR-"]
            # Le enviamos un mensaje "update" con un nuevo valor
            elemento_contador.update(cuenta_regresiva)
        elif event == "-OPCION CORRECTA-":
            print("COOOOORRRECCCCTOOOOOOO")
        elif 'INCORRECTA' in event:
            print("INCORRECTO...")
        elif event == "-PASAR-":
            pass
    window.close()   

    # Cerramos la ventana
        
#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------
# FUNCIONES PARA INICIAR/ TERMINAR RONDAS
'''def iniciar_ronda(num_ronda):
    ronda+=1
    nombres_datasets=[]
    elegido= seleccion_dataset(nombres_datasets())
    definir_opciones(elegido)

def saltear_ronda():
    opcion_incorrecta()
    ronda+=1

def salir_menu():
    for x in Range(ronda,cant_rondas):
        opcion_incorrecta()
        ronda+=1
    '''


#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------
# SETEO DE OPCIONES DE UNA RONDA

'''def seleccion_dataset():
    nombres= obtener_nombres_datasets()     #Nombres datasets deberia devolver una lista de nombres
    elegido= nombres[randint(0,4)]     #Selecciono un dataset al azar
    return elegido


def definir_opciones(nomb_dataset, opcion_verdadera, vector_atributos = [], vector_falsas= [] ):
    with open(nomb_dataset,'r')as dataset_seleccionado:
        reader= csv.reader(nomb_dataset, delimiter=';')     
        titulo, datos= next(reader), list(reader)       # abro archivo, guardo sus datos

        linea_verdadera= datos[randint(0,len(datos))]    # selecciono una linea al azar
        opcion_verdadera= linea_verdadera[6]    #Caracteristica a adivinar siempre va a estar al final (linea 6)
        for x in range(0,4):
            vector_atributos.append(linea_verdadera[x])  # Devuelvo cantidad de opciones en un vector segun la dificultad

        for y in range(0, dificultad()):
            opcion_falsa= datos[randint]
            vector_falsas.append(opcion_falsa[6])
            

#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------
#  VALIDADOR DE UNA OPCION

def validador_opcion(vector_op, respuesta):
    return (vector_op[ronda]==respuesta)






# TOMAR UN DATASET ALEATORIO, DEVOLVER 5 DATOS
# ESTABLECER 5 OPCIONES DE NOMBRE PARA ELEGIR, 4 O 3 SEGUN LA DIFICULTAD
# VALIDAR SI LA OPCION SELECCIONADA ES LA CORRECTA Y GRAFICAR EN HISTORIAL RESPUESTAS



    
#VARIABLES FALTANTES N PREGUNTA ACT, VECTOR, NRO CTA REGRESIVA'''