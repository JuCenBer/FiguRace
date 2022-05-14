from ast import Nonlocal
from cgitb import text
from time import sleep
from tkinter import BROWSE, EXTENDED
from turtle import width
import PySimpleGUI as sg
import json
import os


def crear_ventana_nuevo_jugador():
    layout = [[sg.Text(text='Ingrese los datos del nuevo perfil: ', size=50)], [sg.Text(text='Nickname '), sg.Input()],
              [sg.Text(text='Edad '), sg.Input()],
              [sg.Text(text='Genero autopercibido '), sg.Input()],
              [sg.Button(button_text='Crear', key='-CONFIRMAR CREAR JUGADOR-')]
              ]
    return sg.Window('Nuevo Perfil', layout, finalize=True)


def crear_perfil(datos):
    jugador = {'nick': datos[0], 'edad': datos[1], 'genero': datos[2]}
    with open(os.path.realpath(os.path.join('src', 'datos', 'perfiles.json')), "r", encoding='utf-8') as perfiles:
        try:
            jugadores = json.load(perfiles)  # intento cargar el json
        except:
            jugadores = []  # si el json esta vacio, creo una lista vacia
    with open(os.path.realpath(os.path.join('src', 'datos', 'perfiles.json')), "w", encoding='utf-8') as perfiles:
        print(jugador)
        jugadores.append(jugador)
        print(jugadores)
        json.dump(jugadores, perfiles)


def crear_ventana_perfiles():
    try:
        with open(os.path.realpath(os.path.join('src', 'datos', 'perfiles.json')), "r", encoding='utf-8') as perfiles:
            jugadores = json.load(perfiles)  # intento cargar el json
    except:
        with open(os.path.realpath(os.path.join('src', 'datos', 'perfiles.json')), "w", encoding='utf-8') as perfiles:
            jugadores = []

    cabecera = ['Nickname', 'Edad', 'Genero Autopercibido']
    lista_jugadores = list()
    for jugador in jugadores:
        datos = [jugador['nick'], jugador['edad'], jugador['genero']]
        lista_jugadores.append(datos)
    layout = [[sg.Table(values=lista_jugadores, headings=cabecera,
                        auto_size_columns=True,
                        row_height=20,
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
    elif event == '-CREAR JUGADOR-':
        window = crear_ventana_nuevo_jugador()
        current_window.close()
    elif event == '-CONFIRMAR CREAR JUGADOR-':
        crear_perfil(values)
        window = crear_ventana_perfiles()
        current_window.close()
window.close()
