import PySimpleGUI as sg
from . import manejar_datos
from . import menu_principal as menu
import csv

ronda= 0
def iniciar_pantalla_juego():
    config = manejar_datos.obtener_config()
    cuenta_regresiva= config["tiempo_ronda"] #hacer cuenta elemento_contador

    # En layout armamos la ventana.
    # layout es una lista que contiene una lista por cada fila de la ventana.
    opciones = [[sg.Button("Opcion 1",button_color=('black', 'white'), size=(60, 1), font=("Helvetica", 10),key="-option1-")],
    [sg.Button("Opcion 2",button_color=('black', 'white'), size=(60, 1), font=("Helvetica", 10),key="-option2-")],
    [sg.Button("Opcion 3",button_color=('black', 'white'), size=(60, 1), font=("Helvetica", 10),key="-option3-")],
    [sg.Button("Opcion 4",button_color=('black', 'white'), size=(60, 1), font=("Helvetica", 10),key="-option4-")],
    [sg.Button("Opcion 5",button_color=('black', 'white'), size=(60, 1), font=("Helvetica", 10),key="-option5-")]]
    # SELECCIONAR OPCION Y GUARDAR
    # CONFIRMAR CON OK  
    elemento_contador= [[sg.Text("TIEMPO: ",font=("bold", 15), text_color= "white",justification = "right")],
    [sg.Text(cuenta_regresiva,font=("bold", 15),justification = "left", text_color= "white",key="-CONTADOR-")]]

    caracteristicas=[[sg.Text("Nombre:",font=("Helvetica", 10), key="-name-")],[sg.Text("Ubicacion:",font=("Helvetica", 10), key="-UBICACION-")],
    [sg.Text("Elevacion: ", key="-ELEVACION-")],[sg.Text("Tipo:",font=("Helvetica", 10), key="-TIPO-")],[sg.Text("Estado:",font=("Helvetica", 10), key="-NOMBRE-")]]

    puntajes= []  # Agregar 10 niveles y un true or false

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
    window = sg.Window("Menu de juego", layout, size=(500, 500), finalize=True)
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
            cuenta_regresiva -= 1
            # Obtenemos el elemento "-CONTADOR-"
            elemento_contador = window["-CONTADOR-"]
            # Le enviamos un mensaje "update" con un nuevo valor
            elemento_contador.update(cuenta_regresiva)

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