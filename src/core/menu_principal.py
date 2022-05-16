import PySimpleGUI as sg
from . import manejar_datos
from . import menu_perfiles
from . import menu_config

sg.theme('DarkAmber')

def iniciar_menu_principal():

    def crear_ventana_principal():
        menu = [
            [sg.Text("Figurace", justification="center", font="Helvetica 15 bold", pad=((0, 0), (0, 10)))],
            [sg.Button("Jugar", key="-JUGAR-", font="Helvetica 13")],
            [sg.Button("Configuracion", key="-CONFIG-", font="Helvetica 13")],
            [sg.Button("Puntajes", key="-PUNTAJES-", font="Helvetica 13")],
            [sg.Button("Perfil", key="-PERFIL-", font="Helvetica 13")],
            [sg.Button("Salir", key="-EXIT-", font="Helvetica 13")],
        ]

        #Consigo los jugadores y los guardo en el menu
        jugadores = manejar_datos.obtener_perfiles()
        perfiles = ["Usuario"]
        for jugador in jugadores:
            perfiles.append(jugador["nick"])

        layout_configs = [
            [sg.Combo(perfiles, key="-USER-",  enable_events=True, readonly=True, pad=((100, 0), (0, 150)), default_value="Usuario")],
            [sg.Combo(["Dificultad", "Facil", "Normal", "Dificil", "Einstein"], key="-MODE-", enable_events=True, readonly=True, pad=((100, 0), (0, 150)), default_value="Dificultad")]
        ]
        
        layout = [
            [sg.Col(menu, element_justification='center',  pad=((190, 0), (100, 100))), sg.Col(layout_configs)]
        ]

        return sg.Window("Figurace", layout, size=(500, 500), finalize=True)


    window = crear_ventana_principal()
    while True:
        current_window, event, values = sg.read_all_windows()
        
        if(event == sg.WIN_CLOSED) or (event == "-EXIT-"):
            break
        elif event == "-CONFIG-":
            current_window.close()
            window = menu_config.iniciar_pantalla_config()
            window = crear_ventana_principal()
        elif event == "-PERFIL-":
            window.close()
            window = menu_perfiles.iniciar_menu_perfiles()
            window = crear_ventana_principal()
        elif event == "-USER-":
            print(values["-USER-"])
        elif event == "-MODE-":
            print(values)

    # Cerramos la ventana
    window.close()

