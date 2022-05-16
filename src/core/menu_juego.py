from random import randint
import PySimpleGUI as sg
import csv
ronda= 0

# En layout armamos la ventana.
# layout es una lista que contiene una lista por cada fila de la ventana.
opciones = [[sg.Input("Opcion_1",key="-option1-")],[sg.Input("Opcion_2",key="-option2-")],[sg.Input("Opcion_3",key="-option3-")],
[sg.Input("Opcion_4",key="-option4-")],[sg.Input("Opcion_5",key="-option5-")]]

regresiva= [sg.Text(var_regresiva, key="-regresiva-")]

caracteristicas=[sg.Text("Nombre", key="-name-")],[sg.Text("Ubicacion:", key="-UBICACION-")],[sg.Text("Elevacion", key="-ELEVACION-")],
[sg.Text("Tipo", key="-TIPO-")],[sg.Text("Estado", key="-NOMBRE-")]

puntajes= []  # Agregar 10 niveles y un true or false

layout = [
    #Caracteristicas
    caracteristicas,
    #Opciones a elegir para pasar (son 5)
    opciones,
    #Cuenta Regresiva
    regresiva,
    #Puntaje actual
    puntajes,
    #Boton pasar (se pierde la ronda)
    [sg.Input("Pasar",key="-PASAR-")]
    #Volver menu (Se pierde actual y restantes)
    [sg.Input("Volver al Menu",key="ABANDONO")]
    #Popup mensaje final   
]

#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------
# FUNCIONES PARA INICIAR/ TERMINAR RONDAS
def iniciar_ronda(num_ronda):
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
    


#--------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------
# SETEO DE OPCIONES DE UNA RONDA

def seleccion_dataset():
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



    
#VARIABLES FALTANTES N PREGUNTA ACT, VECTOR, NRO CTA REGRESIVA