from tkinter import BROWSE, EXTENDED
import PySimpleGUI as sg
import json
import os
from . import manejar_datos


def iniciar_menu_perfiles():

    def crear_ventana_nuevo_jugador():
        layout = [[sg.Text(text='Ingrese los datos del nuevo perfil: ', size=50)], [sg.Text(text='Nickname '), sg.Input()],
                  [sg.Text(text='Edad '), sg.Input()],
                  [sg.Text(text='Genero autopercibido '), sg.Input()],
                  [sg.Button(button_text='Crear',
                             key='-CONFIRMAR CREAR JUGADOR-')]
                  ]
        return sg.Window('Nuevo Perfil', layout, finalize=True)

    def crear_ventana_editar_jugador(jugador_seleccionado):
        layout = [[sg.Text(text='Ingrese los datos del nuevo perfil: ', size=50)], [sg.Text(text='Nickname '), sg.Input(default_text=jugador_seleccionado[0][0], readonly=True)],
                  [sg.Text(text='Edad '), sg.Input(
                      default_text=jugador_seleccionado[0][1])],

                  [sg.Text(text='Genero autopercibido '), sg.Input(
                      default_text=jugador_seleccionado[0][2])],

                  [sg.Button(button_text='Confirmar edición',
                             key='-CONFIRMAR EDICION JUGADOR-')],

                  [sg.Button(button_text='Volver',
                             key='-CANCELAR EDICION JUGADOR-')]
                  ]
        return sg.Window('Editar Perfil', layout, finalize=True)

    def crear_perfil(datos):
        jugador = {'nick': datos[0], 'edad': datos[1], 'genero': datos[2]}
        jugadores = manejar_datos.obtener_perfiles()
        jugadores.append(jugador)
        manejar_datos.guardar_perfiles(jugadores)

    def crear_ventana_perfiles():
        jugadores = manejar_datos.obtener_perfiles()

        cabecera = ['Nickname', 'Edad', 'Genero Autopercibido']
        lista_jugadores = list()
        for jugador in jugadores:
            datos = [jugador['nick'], jugador['edad'], jugador['genero']]
            lista_jugadores.append(datos)

        layout = [[sg.Table(values=lista_jugadores, headings=cabecera,
                            auto_size_columns=True,
                            row_height=20,
                            enable_events=True,
                            select_mode=EXTENDED,
                            num_rows=len(lista_jugadores), key='-EDITAR JUGADOR-')],
                  [sg.Button('Crear Jugador', key='-CREAR JUGADOR-')],
                  [sg.Button('Volver', key='-VOLVER-')]]
        return sg.Window("Perfil", layout, margins=(200, 150), finalize=True)

    # Principal
    window = crear_ventana_perfiles()
    while True:
        current_window, event, values = sg.read_all_windows()
        print(f"Evento: {event}, Valores: {values}")
        if (event == sg.WIN_CLOSED) or (event == '-VOLVER-'):
            break
        elif event == '-EDITAR JUGADOR-':
            jugadores = manejar_datos.obtener_perfiles()
            lista_jugadores = list()

            for jugador in jugadores:
                datos = [jugador['nick'], jugador['edad'], jugador['genero']]
                lista_jugadores.append(datos)
            jugador_seleccionado = [lista_jugadores[row]
                                    for row in values[event]]
            window = crear_ventana_editar_jugador(jugador_seleccionado)
            current_window.close()
        elif event == '-CONFIRMAR EDICION JUGADOR-':
            window = crear_ventana_perfiles()
            current_window.close()
        elif event == '-CANCELAR EDICION JUGADOR-':
            window = crear_ventana_perfiles()
            current_window.close()
        elif event == '-CREAR JUGADOR-':
            window = crear_ventana_nuevo_jugador()
            current_window.close()
        elif event == '-CONFIRMAR CREAR JUGADOR-':
            crear_perfil(values)
            window = crear_ventana_perfiles()
            current_window.close()
    window.close()
