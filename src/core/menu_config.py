from tkinter import NONE
import PySimpleGUI as sg
from . import manejar_datos

def iniciar_pantalla_config():
    config_previa = manejar_datos.obtener_config()

    nombres_datasets = manejar_datos.obtener_nombres_datasets()
    
    elem_datasets = [sg.Text("Dataset ", font="Helvetica 13", justification="center"),
                sg.Combo(nombres_datasets, key="-CONFIG_DATASET-", default_value=config_previa["dataset"], font="Helvetica 13", s = (18, 1), readonly=True)]

    elem_tiempo = [sg.Text("Tiempo límite por ronda (seg)", justification="center", font="Helvetica 13"),
                sg.Slider(range=(2,10), key="-CONFIG_TIEMPO-", orientation="h",border_width= 10, default_value=config_previa["tiempo_ronda"], font="Helvetica 13", s = (18, 1))]

    elem_rondas = [sg.Text("Cantidad de rondas por partida", justification="center", font="Helvetica 13"),
                sg.Slider(range=(1,20), key="-CONFIG_RONDAS-", orientation="h",border_width= 10, default_value=config_previa["cant_rondas"], font="Helvetica 13", s = (18, 1))]

    elem_puntos_bien = [sg.Text("Puntos por correcta", font="Helvetica 13", justification="center"),
                sg.Slider(range=(1,20), key="-CONFIG_PUNTOS_BIEN-", orientation="h",border_width= 10, default_value=config_previa["puntos_bien"], font="Helvetica 13", s = (18, 1))]

    elem_puntos_mal = [sg.Text("Puntos restados por incorrecta", font="Helvetica 13", justification="center"),
                sg.Slider(range=(-1,-20), key="-CONFIG_PUNTOS_MAL-", orientation="h",border_width= 10, default_value=config_previa["puntos_mal"], font="Helvetica 13", s = (18, 1))]

    elem_carac_tarjeta = [sg.Text("Características a mostrar por tarjeta", font="Helvetica 13", justification="center"),
                sg.Slider(range=(1,5), key="-CONFIG_CANT_CARAC-", orientation="h",border_width= 10, default_value=config_previa["cant_carac"], font="Helvetica 13", s = (18, 1))]

    elem_guardar = [sg.Button("Guardar",key="-CONFIG_GUARDAR-", font="Helvetica 13",s=(10, 1)), 
                sg.Button("Volver",key="-CONFIG_VOLVER-", font="Helvetica 13",s=(10, 1))]

    contenedor = [sg.Frame(title="Opciones de configuración",title_location="n", vertical_alignment="center", element_justification="center",    expand_x=True, expand_y=True, layout=[elem_datasets, elem_tiempo, elem_rondas, elem_puntos_bien, elem_puntos_mal, elem_carac_tarjeta, [sg.HorizontalSeparator()], elem_guardar])]

    estructura = [contenedor]


    window = sg.Window("Configuración",estructura,size=(1000, 600))

    while True:
    # Esperamos un evento
        event, values = window.read()

        print(f"Evento: {event}, valores: {values}")
        if event == sg.WIN_CLOSED:
            break
        elif event == "-CONFIG_GUARDAR-":
            seleccionados = {"dataset": values["-CONFIG_DATASET-"],
                            "tiempo_ronda": values["-CONFIG_TIEMPO-"],
                            "cant_rondas" : values["-CONFIG_RONDAS-"],
                            "puntos_bien" : values["-CONFIG_PUNTOS_BIEN-"],
                            "puntos_mal" : values["-CONFIG_PUNTOS_MAL-"],
                            "cant_carac" : values["-CONFIG_CANT_CARAC-"] }
            
            manejar_datos.guardar_config(seleccionados)
            #print("Guardar")
            #print(seleccionados)
        elif event == "-CONFIG_VOLVER-":
            # Guardar config seleccionada en archivo
            #print("Volver")
            break
        
    window.close()
