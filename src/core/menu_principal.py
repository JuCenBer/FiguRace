import PySimpleGUI as sg
from . import manejar_datos
from . import menu_perfiles
from . import menu_config
from . import menu_puntajes

sg.theme('DarkAmber')

def iniciar_menu_principal():

    def crear_ventana_principal():
        menu = [
            [sg.Text("FIGURACE", justification="center", font="Helvetica 15 bold", pad=((0, 0), (0, 10)))],
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
            [sg.Frame(title="Usuario",element_justification="center", title_location="n", pad=((50, 0), (0, 150)), border_width=0, 
            layout=[[sg.Combo(perfiles, key="-USER-", font="Helvetica 11", size=(20,1),enable_events=True, readonly=True)]])],
            
            [sg.Frame(title="Dificultad",element_justification="center", title_location="n", pad=((50, 0), (0, 150)), border_width=0, 
            layout=[[sg.Combo(["Facil", "Normal", "Dificil", "Einstein"], size=(20,1), font="Helvetica 11", key="-MODE-", enable_events=True, readonly=True)]])]
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
        elif event == "-PUNTAJES-":
            current_window.close()
            window = menu_puntajes.iniciar_pantalla_puntajes()
            window = crear_ventana_principal()
        elif event == "-CONFIG-":
            current_window.close()
            window = menu_config.iniciar_pantalla_config()
            window = crear_ventana_principal()
        elif event == "-PERFIL-":
            current_window.close()
            window = menu_perfiles.iniciar_menu_perfiles()
            window = crear_ventana_principal()
        elif event == "-USER-":
            print(values["-USER-"])
        elif event == "-MODE-":
            print(values)
            # actualizar archivo config

    # Cerramos la ventana
    window.close()

