import PySimpleGUI as sg

# En layout armamos la ventana.
# layout es una lista que contiene una lista por cada fila de la ventana.
opciones = [[sg.Input("Opcion_1",key="-option1-")],[sg.Input("Opcion_2",key="-option2-")],[sg.Input("Opcion_3",key="-option3-")],
[sg.Input("Opcion_4",key="-option4-")],[sg.Input("Opcion_5",key="-option5-")]]

regresiva= [sg.Text(var_regresiva, key="-regresiva-")]

caracteristicas=[sg.Text("Nombre", key="-name-")],[sg.Text("Ubicacion:", key="-UBICACION-")],[sg.Text("Elevacion", key="-ELEVACION-")],
[sg.Text("Tipo", key="-TIPO-")],[sg.Text("Estado", key="-NOMBRE-")]

puntajes= [[sg.Input("Opcion_1",key="-option1-")],[sg.Input("Opcion_2",key="-option2-")],[sg.Input("Opcion_3",key="-option3-")],
[sg.Input("Opcion_4",key="-option4-")],[sg.Input("Opcion_5",key="-option5-")]]

layout = [
    #Caracteristicas
    caracteristicas,
    #Opciones a elegir para pasar (son 5)
    opciones,
    #Cuenta Regresiva
    regresiva,
    #Puntaje actual
    puntajes,
    #Boton pasar (se pierde la ronda)
    [sg.Input("Pasar",key="-PASAR-")]
    #Volver menu (Se pierde actual y restantes)
    [sg.Input("Abandonar",key="ABANDONO")]
    #Popup mensaje final
    
]

# Creamos el objeto ventana
window = sg.Window("Título de la ventana", layout)

