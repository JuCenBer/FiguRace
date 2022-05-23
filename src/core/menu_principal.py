from email.policy import default
from multiprocessing.sharedctypes import Value
import PySimpleGUI as sg
#from datetime import datetime
from . import manejar_datos
from . import menu_perfiles
from . import menu_config
from . import menu_puntajes
from . import menu_juego

sg.theme('DarkAmber')

# sesion_actual = {"usuario": }

"""Por si por primera vez, no hay perfiles creados"""
def crear_ventana_nuevo_jugador():
    lista_edades = [i for i in range(5,131)]
    lista_generos = ['Hombre','Mujer','No Binario']
    layout = [[[sg.Text(text='Ingrese los datos del nuevo perfil: ', size=50)], [sg.Text(text='Nickname '), sg.Input()],
    [sg.Text(text='Ya existe un perfil con ese Nickname. Pruebe ingresando otro distinto.',key='-TEXTO NICKNAME EXISTENTE-', visible=False, text_color='red')],
    [sg.Text(text='No puede registrar un perfil con un Nickname vacio.', key='-TEXTO NICKNAME VACIO-', visible=False, text_color='red')]],
              [sg.Text(text='Edad '), sg.Combo(lista_edades, readonly=True, default_value = lista_edades[0])],
              [sg.Text(text='Genero autopercibido '), sg.Combo(lista_generos, readonly= True, default_value= lista_generos[0])],
              [sg.Button(button_text='Crear', key='-CONFIRMAR CREAR PRIMER JUGADOR-')],
              ]
    
    return sg.Window('Nuevo Perfil', layout, finalize=True)


def crear_ventana_principal():

    elem_botones = [sg.Col(layout=[
        [sg.Button("Jugar", key="-JUGAR-", font="Helvetica 13")],
        [sg.Button("Configuracion", key="-CONFIG-", font="Helvetica 13")],
        [sg.Button("Puntajes", key="-PUNTAJES-", font="Helvetica 13")],
        [sg.Button("Perfil", key="-PERFIL-", font="Helvetica 13")],
        [sg.Button("Salir", key="-EXIT-", font="Helvetica 13")]])]
        

    #Obtiene la ultima sesion abierta
    ultima_sesion = manejar_datos.obtener_ultima_sesion()
    # Consigo los jugadores y los guardo en el menu
    jugadores = manejar_datos.obtener_perfiles()
    if(len(jugadores)) == 0:
        return crear_ventana_nuevo_jugador()

    perfiles = []
    for jugador in jugadores:
        perfiles.append(jugador["nick"])

    elem_usuario = [sg.Frame(title="Usuario", element_justification="center", title_location="n", border_width=0, layout=[[sg.Combo(perfiles, key="-USER-", font="Helvetica 11", size=(20, 1), enable_events=True, readonly=True, default_value=ultima_sesion["nick"])]])]

    elem_dificultad = [sg.Frame(title="Dificultad", element_justification="center", title_location="n", border_width=0, layout=[[sg.Combo(["Facil", "Normal", "Dificil", "Einstein"], size=(20, 1), font="Helvetica 11", key="-MODE-", enable_events=True, readonly=True, default_value=ultima_sesion["dificultad"])]])]
    
    elem_sesion = [sg.Frame(title="Última partida", title_location="n", border_width=1,
                    layout=[[sg.Text(ultima_sesion["nick"], font="Helvetica 11")]])]

    elem_configs = [sg.Col(layout=[elem_usuario, elem_dificultad,elem_sesion])]

    elem_titulo = [sg.Text("FIGURACE", justification="center", font="Helvetica 15 bold", pad=((0, 0), (0, 10)))]

    elem_frame = [sg.Frame(title="Menú", element_justification="center", title_location="n", expand_x=True, border_width=1,
                layout=[elem_botones,elem_configs])]

    return sg.Window("Figurace", layout=[[sg.Col(layout=[elem_titulo,elem_frame], element_justification='center')]], size=(500, 500), finalize=True)


def iniciar_menu_principal():
    
    window = crear_ventana_principal()
    while True:
        event, values = window.read()

        if(event == sg.WIN_CLOSED) or (event == "-EXIT-"):

            break
        elif event == "-JUGAR-":
            window.close()
            window = menu_juego.iniciar_pantalla_juego()
            print(values["-USER-"])
            window = crear_ventana_principal()
        elif event == "-PUNTAJES-":
            window.close()
            window = menu_puntajes.iniciar_pantalla_puntajes()
            window = crear_ventana_principal()
        elif event == "-CONFIG-":
            window.close()
            window = menu_config.iniciar_pantalla_config()
            window = crear_ventana_principal()
        elif event == "-PERFIL-":
            window.close()
            window = menu_perfiles.iniciar_menu_perfiles()
            window = crear_ventana_principal()
        elif event == "-USER-":
            #format = datetime.now().strftime('%d/%m/%Y, %H:%M')
            sesion = {"nick": values["-USER-"], "dificultad":values["-MODE-"], "fecha":"-", "puntaje":0}
            manejar_datos.guardar_ultima_sesion(sesion)
        elif event == "-MODE-":
            sesion = manejar_datos.obtener_ultima_sesion()
            sesion["dificultad"] = values["-MODE-"]
            manejar_datos.guardar_ultima_sesion(sesion)
            # actualizar archivo config
        elif event == "-CONFIRMAR CREAR PRIMER JUGADOR-":
            window.close()
            jugador = {"nick":values[0], "edad":values[1], "genero":values[2]}
            sesion = {"nick": values[0], "dificultad":"Facil", "fecha":"-", "puntaje":0}
            manejar_datos.guardar_perfiles([jugador])
            manejar_datos.guardar_ultima_sesion(sesion)
            window = crear_ventana_principal()

    # Cerramos la ventana
    window.close()
