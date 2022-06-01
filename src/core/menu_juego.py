from random import randrange, shuffle, choices
import PySimpleGUI as sg
from . import manejar_datos
from . import menu_principal as menu
import csv
'''Genera las opciones a seleccionar en el juego, devolviendo 5 botones, 4 falsos, 1 como opcion correcta.
 Tambien devuelve los datos de la opcion verdadera para mostrar en la pantalla a la hora de encontrar la verdadera'''
def generar_opciones(dataset):
    lineas = choices(dataset, k=5)    #Guarda 5 lineas aleatorias del dataset, (se trae como lista de listas)
    opcion_correcta = [sg.Button(lineas[0][5].title(), size=(60, 1), font=("Helvetica", 10),key="-OPCION CORRECTA-")]
    linea_correcta = lineas[0] #Me guardo los datos de la linea correcta
    opciones = [opcion_correcta] #Creo lista de elemento botones con la primera opcion V
    for i in range(1,5):
        boton_incorrecto = [sg.Button(lineas[i][5].title(), size=(60, 1), font=("Helvetica", 10),key="-OPCION INCORRECTA "+str(i)+"-")]
        opciones.append(boton_incorrecto)   #Agrego botones falsos(4)
    shuffle(opciones) #Mezclo los botones
    return opciones, linea_correcta
#text_color = None,
   # background_color = None
''' Este modulo busca los datos de linea correcta y los nombres de las caracteristicas
para mostrar ordenadamente cada CARACTERISTICA = DATO '''
def obtener_caracteristicas(config,encabezado,linea_correcta):
    caracteristicas = [[sg.Text('CARACTERISTICAS',font=("overstrike", 14))]] #Creo lista de elementos texto, para mostrar todas las caracteristicas
    for i in range(int(config["cant_carac"])):
        nueva_carac = [sg.Text(encabezado[i].title() + ": " + linea_correcta[i].title(),font=("Helvetica", 12),text_color='#C0C0C0')]
        caracteristicas.append(nueva_carac) # Agrego nuevo elemento de texto a mi lista de caracteristicas
    return caracteristicas #Devuelvo lista de elementos

'''Genero lista de elementos para iniciar la pantalla'''
def generar_layout(config,dataset):
    
    encabezado = dataset[0]
    dataset.pop(0)
    cantidad_tiempo= config["tiempo_ronda"] #Busca cantidad de tiempo a utilizar en config  

    '''Se define contador con la cantidad de tiempo establecida por la dificultad'''
    
    elemento_contador= [sg.Frame(title="TIEMPO", title_location="n", border_width=2,
                                 layout=[[sg.Text(cantidad_tiempo,font=("bold", 15), text_color= "white",key="-CONTADOR-")]])]

    # puntajes= []  

    '''Genero opciones y caracteristicas a traves de los modulos definidos anteriormente'''
    opciones, linea_correcta = generar_opciones(dataset)
    caracteristicas = obtener_caracteristicas(config,encabezado,linea_correcta)

    '''Se crea la lista de elementos'''
    layout = [
        #Caracteristicas
        caracteristicas,

        #Opciones a elegir para pasar (son 5)
        opciones,

        #En esta linea se va a implementar los puntajes por rondas
        #puntajes,
    
        #Boton pasar (se pierde la ronda)
        [sg.Button("Pasar", size=(60, 1), font=("Helvetica", 10),button_color=('black','gray'),key="-PASAR-")],

        #Volver menu (Se pierde actual y restantes)
        [sg.Button("Volver al Menu", size=(60, 1), font=("Helvetica", 10),button_color=('black','gray'), key="-ABANDONO-")],
 
        #Cuenta Regresiva
        elemento_contador
    ]
    return layout

''' Este modulo crea la pantalla de juego y inicia la ejecucion de menu de juego'''
def iniciar_pantalla_juego():
   
    '''A traves mis manejadores de datos, obtengo las configuraciones
    y el dataset de los archivos correspondientes para generar mi ventana'''
    config = manejar_datos.obtener_config()
    dataset = manejar_datos.obtener_dataset(config["dataset"])
    cantidad_tiempo= config['tiempo_ronda'] #En esta variable guardo el tiempo disponible actual para actualizarlo cada seg

    '''Creo mi ventana con generar_layout con los parametros correspondientes'''
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
            # Incrementamos el cantidad_tiempo
            if cantidad_tiempo > 0: cantidad_tiempo -= 1
            # Obtenemos el elemento "-CONTADOR-"
            elemento_contador = window["-CONTADOR-"]
            # Le enviamos un mensaje "update" con un nuevo valor
            elemento_contador.update(cantidad_tiempo)
        elif event == "-OPCION CORRECTA-":
            print("COOOOORRRECCCCTOOOOOOO")
        elif 'INCORRECTA' in event:
            print("INCORRECTO...")
        elif event == "-PASAR-":
            pass
    window.close()   

    # Cerramos la ventana
