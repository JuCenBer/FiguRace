import PySimpleGUI as sg

def iniciar_config():
    valores_tiempo_ronda = ["Opcion 1", "Opcion 2", "Opcion 3"] # Aca se llamaria a un archivo
    valor_previo = "Opcion 1"
    estructura = [[sg.Text("Tiempo límite por ronda", font=("Arial", 12), justification="center"),
                sg.Combo(valores_tiempo_ronda, key="-COMBO_TIEMPO-", default_value=valor_previo, font=("Arial", 12), s = (10, 1), readonly=True)],
                [sg.Text("Cantidad de rondas por partida", font=("Arial", 12), justification="center"),
                sg.Combo(valores_tiempo_ronda, key="-COMBO_RONDAS-", default_value=valor_previo, font=("Arial", 12), s = (10, 1), readonly=True)],
                [sg.Text("Puntos por correcta", font=("Arial", 12), justification="center"),
                sg.Combo(valores_tiempo_ronda, key="-COMBO_PUNTOS_BIEN-", default_value=valor_previo, font=("Arial", 12), s = (10, 1), readonly=True)],
                [sg.Text("Puntos restados por incorrecta", font=("Arial", 12), justification="center"),
                sg.Combo(valores_tiempo_ronda, key="-COMBO_PUNTOS_MAL-", default_value=valor_previo, font=("Arial", 12), s = (10, 1), readonly=True)],
                [sg.Text("Características a mostrar por tarjeta", font=("Arial", 12), justification="center"),
                sg.Combo(valores_tiempo_ronda, key="-COMBO_CARACTERISTICAS-", default_value=valor_previo, font=("Arial", 12), s = (10, 1), readonly=True)],
                [sg.Button("Guardar",key="-CONFIG_GUARDAR-", font=("Arial", 12),s=(10, 1)), 
                sg.Button("Volver",key="-CONFIG_VOLVER-", font=("Arial", 12),s=(10, 1))]]
    window = sg.Window("Configuración",estructura,size=(1000, 500))

    while True:
    # Esperamos un evento
        event, values = window.read()

        print(f"Evento: {event}, valores: {values}")
        if event == sg.WIN_CLOSED:
            break
        elif event == "-CONFIG_GUARDAR-":
            # Guardar config seleccionada en archivo
            print("Guardar")
        elif event == "-CONFIG_VOLVER-":
            # Guardar config seleccionada en archivo
            print("Volver")
        
    window.close()

iniciar_config()