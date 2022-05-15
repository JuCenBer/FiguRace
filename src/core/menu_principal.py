import PySimpleGUI as sg
import os

def obtener_perfiles():
    #Creo un archivo perfiles.json en el mismo directorio antes de que organizemos las carpetas
    ruta_perfiles = os.path.join(os.getcwd(), "perfiles.json")

def menu_principal():
    sg.theme('DarkAmber')    

    layout_menu = [
        [sg.Button("Jugar", key="-BOTON_JUGAR-")],
        [sg.Button("Configuracion", key="-BOTON_CONFIG-")],
        [sg.Button("Puntajes", key="-BOTON_PUNTAJES-")],
        [sg.Button("Perfil", key="-PERFIL-")],
        [sg.Button("Salir", key="-EXIT-")],
    ]

    perfiles = obtener_perfiles()
    
    layout = [
        [sg.Text("Figurace", justification="center")],
        [sg.Column(layout_menu, element_justification='center', vertical_alignment='center')],
        [sg.Combo(perfiles)]
    ]


    window = sg.Window("Figurace", layout, size=(500, 500), element_justification='c')

    while True:
        event, values = window.read()
        
        if(event == sg.WIN_CLOSED) or (event == "-EXIT-"):
            break
        elif event == "-CONTAR-":
            print("Esta contando")

    # Cerramos la ventana
    window.close()

menu_principal()