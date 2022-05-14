import PySimpleGUI as sg
from . import manejar_datos

def iniciar_pantalla_config():
    valores_tiempo_ronda = ["Opcion 1", "Opcion 2", "Opcion 3"] # Aca se llamaria a un archivo
    config_previa = manejar_datos.obtener_config()

    nombres_datasets = manejar_datos.obtener_nombres_datasets()
    # SELECTORES CORRECTOS, MOSTRAR OPCIONES ACORDES
    
    elem_datasets = [sg.Text("Dataset ", font=("Arial", 12), justification="center"),
                sg.Combo(nombres_datasets, key="-COMBO_DATASET-", default_value=config_previa["dataset"], font=("Arial", 12), s = (10, 1), readonly=True)]

    elem_tiempo = [sg.Text("Tiempo límite por ronda", font=("Arial", 12), justification="center"),
                sg.Combo(valores_tiempo_ronda, key="-COMBO_TIEMPO-", default_value=config_previa["tiempo_ronda"], font=("Arial", 12), s = (10, 1), readonly=True)]

    elem_rondas = [sg.Text("Cantidad de rondas por partida", font=("Arial", 12), justification="center"),
                sg.Combo(valores_tiempo_ronda, key="-COMBO_RONDAS-", default_value=config_previa["cant_rondas"], font=("Arial", 12), s = (10, 1), readonly=True)]

    elem_puntos_bien = [sg.Text("Puntos por correcta", font=("Arial", 12), justification="center"),
                sg.Combo(valores_tiempo_ronda, key="-COMBO_PUNTOS_BIEN-", default_value=config_previa["puntos_bien"], font=("Arial", 12), s = (10, 1), readonly=True)]

    elem_puntos_mal = [sg.Text("Puntos restados por incorrecta", font=("Arial", 12), justification="center"),
                sg.Combo(valores_tiempo_ronda, key="-COMBO_PUNTOS_MAL-", default_value=config_previa["puntos_mal"], font=("Arial", 12), s = (10, 1), readonly=True)]

    elem_carac_tarjeta = [sg.Text("Características a mostrar por tarjeta", font=("Arial", 12), justification="center"),
                sg.Combo(valores_tiempo_ronda, key="-COMBO_CANT_CARAC-", default_value=config_previa["cant_carac"], font=("Arial", 12), s = (10, 1), readonly=True)]

    elem_guardar = [sg.Button("Guardar",key="-CONFIG_GUARDAR-", font=("Arial", 12),s=(10, 1)), 
                sg.Button("Volver",key="-CONFIG_VOLVER-", font=("Arial", 12),s=(10, 1))]

    estructura = [elem_datasets, elem_tiempo, elem_rondas, elem_puntos_bien, elem_puntos_mal, elem_carac_tarjeta, elem_guardar]

    window = sg.Window("Configuración",estructura,size=(1000, 500))

    while True:
    # Esperamos un evento
        event, values = window.read()

        print(f"Evento: {event}, valores: {values}")
        if event == sg.WIN_CLOSED:
            break
        elif event == "-CONFIG_GUARDAR-":
            seleccionados = {"dataset": values["-COMBO_DATASET-"],
                            "tiempo_ronda": values["-COMBO_TIEMPO-"],
                            "cant_rondas" : values["-COMBO_RONDAS-"],
                            "puntos_bien" : values["-COMBO_PUNTOS_BIEN-"],
                            "puntos_mal" : values["-COMBO_PUNTOS_MAL-"],
                            "cant_carac" : values["-COMBO_CANT_CARAC-"] }
            
            manejar_datos.guardar_config(seleccionados)
            #print("Guardar")
            #print(seleccionados)
        elif event == "-CONFIG_VOLVER-":
            # Guardar config seleccionada en archivo
            #print("Volver")
            break
        
    window.close()
