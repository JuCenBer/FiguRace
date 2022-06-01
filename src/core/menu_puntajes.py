from multiprocessing import set_executable
from tkinter import NONE
import PySimpleGUI as sg
from . import manejar_datos

def iniciar_pantalla_puntajes():
    ''' Crea la ventana de la pantalla de puntajes para visualizar los mejores 20 puntajes por cada dificultad '''
    # Se obtendran los historiales de partidas con el modulo manejar_datos
    #tabla_top_usuarios = manejar_datos.obtener_top_puntajes()

    # Se hace una variable a modo de ejemplo para visualizar en la primera entrega
    tabla_top_usuarios = [["Usuario 1","112154"],["Usuario 2","45468"]]

    # Varias tablas para las distintas dificultades
    elem_tabla_1 = sg.Frame(title='Fácil', title_location='n', layout=[[sg.Table(headings=["Usuario","Puntos"], values=tabla_top_usuarios, auto_size_columns=True, font="Helvetica 13", hide_vertical_scroll=True, num_rows=20, justification="center")]])

    elem_tabla_2 = sg.Frame(title='Normal', title_location='n', layout=[[sg.Table(headings=["Usuario","Puntos"], values=tabla_top_usuarios, auto_size_columns=True, font="Helvetica 13", hide_vertical_scroll=True, num_rows=20, justification="center")]])

    elem_tabla_3 = sg.Frame(title='Difícil', title_location='n', layout=[[sg.Table(headings=["Usuario","Puntos"], values=tabla_top_usuarios, auto_size_columns=True, font="Helvetica 13", hide_vertical_scroll=True, num_rows=20, justification="center")]])

    elem_tabla_4 = sg.Frame(title='Einstein', title_location='n', layout=[[sg.Table(headings=["Usuario","Puntos"], values=tabla_top_usuarios, auto_size_columns=True, font="Helvetica 13", hide_vertical_scroll=True, num_rows=20, justification="center")]])

    elem_tablas = [elem_tabla_1, elem_tabla_2, elem_tabla_3, elem_tabla_4]
    
    elem_volver = [sg.Button("Volver",key="-PUNTAJES_VOLVER-", font="Helvetica 13",s=(10, 1))]

    contenedor = [[sg.Frame(title="Top 20 usuarios",title_location="n", vertical_alignment="center", element_justification="center", expand_x=True, expand_y=True, layout=[elem_tablas, [sg.HorizontalSeparator()], elem_volver])]]

    window = sg.Window("Configuración",contenedor,size=(1000, 600))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "-PUNTAJES_VOLVER-":
            break
    window.close()
