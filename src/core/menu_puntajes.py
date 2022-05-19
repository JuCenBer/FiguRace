from multiprocessing import set_executable
from tkinter import NONE
import PySimpleGUI as sg
from . import manejar_datos

def iniciar_pantalla_puntajes():

    tabla_top_usuarios = manejar_datos.obtener_top_puntajes()
    tabla_top_usuarios = [["Usuario 1","112154"],["Usuario 2","45468"]]

    elem_tabla = [sg.Table(headings=["Usuario","Puntos"], values=tabla_top_usuarios, auto_size_columns=True, font="Helvetica 13", hide_vertical_scroll=True, num_rows=20, justification="center")]

    elem_tabla = [sg.Table(headings=["Usuario","Puntos"], values=tabla_top_usuarios, auto_size_columns=True, font="Helvetica 13", hide_vertical_scroll=True, num_rows=20, justification="center")]

    elem_tabla = [sg.Table(headings=["Usuario","Puntos"], values=tabla_top_usuarios, auto_size_columns=True, font="Helvetica 13", hide_vertical_scroll=True, num_rows=20, justification="center")]
    
    elem_volver = [sg.Button("Volver",key="-PUNTAJES_VOLVER-", font="Helvetica 13",s=(10, 1))]
    
    contenedor = [sg.Frame(title="Top 20 usuarios",title_location="n", vertical_alignment="center", element_justification="center", expand_x=True, expand_y=True, layout=[elem_tabla, elem_tabla, [sg.HorizontalSeparator()], elem_volver])]

    estructura = [contenedor]


    window = sg.Window("Configuración",estructura,size=(1000, 600))

    while True:
        event, values = window.read()
        #print(f"Evento: {event}, valores: {values}")
        if event == sg.WIN_CLOSED:
            break
        elif event == "-PUNTAJES_VOLVER-":
            #print("Volver")
            break
    window.close()
