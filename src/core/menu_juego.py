from random import shuffle, choices
import PySimpleGUI as sg
import datetime
from . import manejar_datos
from . import menu_principal as menu

def generar_opciones(dataset):
    '''Genera las opciones a seleccionar en el juego, devolviendo 5 botones, 4 falsos, 1 como opcion correcta.
    Tambien devuelve los datos de la opcion verdadera para mostrar en la pantalla a la hora de encontrar la verdadera'''
    lineas = choices(dataset, k=5)    #Guarda 5 lineas aleatorias del dataset, (se trae como lista de listas)
    opcion_correcta = [sg.Button(lineas[0][5].title(), size=(60, 1), font=("Helvetica", 10),key="-OPCION CORRECTA-")]
    linea_correcta = lineas[0] #Me guardo los datos de la linea correcta
    opciones = [opcion_correcta] #Creo lista de elemento botones con la primera opcion V
    for i in range(1,5):
        boton_incorrecto = [sg.Button(lineas[i][5].title(), size=(60, 1), font=("Helvetica", 10),key="-OPCION INCORRECTA "+str(i)+"-")]
        opciones.append(boton_incorrecto)   #Agrego botones falsos(4)
    shuffle(opciones) #Mezclo los botones
    return opciones, linea_correcta

def obtener_caracteristicas(config,encabezado,linea_correcta):
    ''' Este modulo busca los datos de linea correcta y los nombres de las caracteristicas
    para mostrar ordenadamente cada CARACTERISTICA = DATO '''
    caracteristicas = [[sg.Text('CARACTERISTICAS',font=("overstrike", 14))]] #Creo lista de elementos texto, para mostrar todas las caracteristicas
    for i in range(int(config["valores"]["cant_carac"])):
        nueva_carac = [sg.Text(encabezado[i].title() + ": " + linea_correcta[i].title(),font=("Helvetica", 12),text_color='#C0C0C0')]
        caracteristicas.append(nueva_carac) # Agrego nuevo elemento de texto a mi lista de caracteristicas
    return caracteristicas #Devuelvo lista de elementos

def generar_layout(config,dataset):
    '''Genero lista de elementos para iniciar la pantalla'''
    
    encabezado = dataset[0]
    dataset.pop(0)
    cantidad_tiempo = config["valores"]["tiempo_ronda"] #Busca cantidad de tiempo a utilizar en config  


    #Se define contador con la cantidad de tiempo establecida por la dificultad'''
    
    elemento_contador = [sg.Frame(title="TIEMPO", title_location="n", border_width = 2,
                                 layout=[[sg.Text(cantidad_tiempo,font = ("bold", 15), text_color = "white",key="-CONTADOR-")]])]
    
    elemento_puntaje = [sg.Frame(title="PUNTAJE", title_location="n", border_width = 2,
                                 layout=[[sg.Text(0 ,font = ("bold", 15), text_color = "white",key="-PUNTOS-")]])]
                              
    #Genero opciones y caracteristicas a traves de los modulos definidos anteriormente'''
    opciones, linea_correcta = generar_opciones(dataset)
    caracteristicas = obtener_caracteristicas(config,encabezado,linea_correcta)
   
    #Se crea la lista de elementos
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
<<<<<<< HEAD
        elemento_contador,
        #[sg.Image(r'C:\Users\gon\Desktop\Integrador\CORRECTO.png')]
=======
        elemento_puntaje,

        elemento_contador
>>>>>>> c4a092f00c9bf7db779f13230ab5289c57d22126
    ]
    return layout



def iniciar_pantalla_juego():
    ''' Este modulo crea la pantalla de juego y inicia la ejecucion de menu de juego'''
<<<<<<< HEAD
   
=======

>>>>>>> c4a092f00c9bf7db779f13230ab5289c57d22126
    #A traves mis manejadores de datos, obtengo las configuraciones y el dataset de los archivos correspondientes para generar mi ventana
    config = manejar_datos.obtener_config()
    dataset = manejar_datos.obtener_dataset(config["dataset"])
    cantidad_tiempo = config["valores"]["tiempo_ronda"] #En esta variable guardo el tiempo disponible actual para actualizarlo cada seg
    
    cantidad_puntos = 0

    eventos = list()
    evento = {"timestamp": datetime.datetime.timestamp(datetime.datetime.now()),
                "id": "",
                "evento": "inicio_partida",
                "usuarie": config["nick"],
                "estado": "nueva",
                "texto_ingresado": "-",
                "respuesta": "-",
                "nivel": config["dificultad"],
            }
    eventos.append(evento)

    #Creo mi ventana con generar_layout con los parametros correspondientes
    window = sg.Window("Menu de juego", layout = generar_layout(config,dataset), size=(500, 550), finalize=True)
    while True:
        event, values = window.read(timeout=1000)
        if event != "__TIMEOUT__":
          print(f"{event} {values}")

        if event == sg.WIN_CLOSED:
            menu.crear_ventana_principal
            break

        if event == "-ABANDONO-":
            evento["timestamp"] = datetime.datetime.timestamp(datetime.datetime.now())
            evento["evento"] = "fin"
            evento["estado"] = "cancelada"
            eventos.append(evento)
            menu.crear_ventana_principal
            break

        elif event == "__TIMEOUT__":
            # Incrementamos el cantidad_tiempo
            if cantidad_tiempo > 0: 
                cantidad_tiempo -= 1
                elemento_contador = window["-CONTADOR-"]   
                elemento_contador.update(cantidad_tiempo)
            else:
                evento["timestamp"] = datetime.datetime.timestamp(datetime.datetime.now())
                evento["evento"] = "intento"
                evento["estado"] = "timeout"
                evento["texto_ingresado"] = "-"
                evento["respuesta"] = "-"
                print(evento)
                eventos.append(evento)
                #PASAR_DE_RONDA()

        elif event == "-OPCION CORRECTA-":
            evento["timestamp"] = datetime.datetime.timestamp(datetime.datetime.now())
            evento["evento"] = "intento"
            evento["estado"] = "ok"
            evento["texto_ingresado"] = window[event].get_text()
            evento["respuesta"] = window["-OPCION CORRECTA-"].get_text()

            cantidad_puntos = cantidad_puntos + config["valores"]["puntos_bien"]
            elemento_puntaje = window["-PUNTOS-"]
            elemento_puntaje.update(cantidad_puntos)
            print(evento)
            eventos.append(evento)
            #PASAR_DE_RONDA()

        elif 'INCORRECTA' in event:
            evento["timestamp"] = datetime.datetime.timestamp(datetime.datetime.now())
            evento["evento"] = "intento"
            evento["estado"] = "error"
            evento["texto_ingresado"] = window[event].get_text()
            evento["respuesta"] = window["-OPCION CORRECTA-"].get_text()

            cantidad_puntos = cantidad_puntos + config["valores"]["puntos_mal"]
            elemento_puntaje = window["-PUNTOS-"]
            elemento_puntaje.update(cantidad_puntos)

            print(evento)
            eventos.append(evento)
            #PASAR_DE_RONDA()

        elif event == "-PASAR-":
            evento["timestamp"] = datetime.datetime.timestamp(datetime.datetime.now())
            evento["evento"] = "intento"
            evento["estado"] = "pasar"
            evento["texto_ingresado"] = "-"
            evento["respuesta"] = window["-OPCION CORRECTA-"].get_text()
            print(evento)
            eventos.append(evento)
            #PASAR_DE_RONDA()
        
    window.close()  
