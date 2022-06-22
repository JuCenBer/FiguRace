from matplotlib import pyplot as plt
import pandas as pd
import os
import json

#Abro los eventos
ruta = os.path.join(os.getcwd(), '..', 'datos', 'eventos_partidas.csv')
data_set = pd.read_csv(ruta, encoding='utf-8')

#Abro los perfiles
with open(os.path.join(os.getcwd(), "..", "datos", "perfiles.json"), "r", encoding='utf-8') as perfiles:
    jugadores = json.load(perfiles)

#Obtengo los eventos finalizados por usuario
usuarios_fin = data_set.groupby(["estado", "usuarie"])["usuarie"].count()
usuarios_fin = usuarios_fin["finalizado"]
#print(usuarios_fin)

#Obtengo los usuarios y sus generos
usuarios = {}
for usuario in usuarios_fin.keys():
    usuarios.update({usuario:""})

for jugador in jugadores:
    for usuario in usuarios:
        if(jugador["nick"] == usuario):
            usuarios[usuario] = jugador["genero"]

#Actualizo la cantidad de cada genero
cant_hombres = 0
cant_mujeres = 0
cant_nobinario = 0

for usuario in usuarios_fin.keys():
    if(usuarios[usuario] == "Hombre"):
        cant_hombres+= usuarios_fin[usuario]
    if(usuarios[usuario] == "No Binario"):
        cant_nobinario+= usuarios_fin[usuario]
    if(usuarios[usuario] == "Mujer"):
        cant_mujeres+= usuarios_fin[usuario]


#A partir de aca es para hacer la torta
etiquetas = ["Hombres", "Mujeres", "No Binario"]

data_dibujo = [cant_hombres, cant_mujeres, cant_nobinario]
explode = (0.1, 0.1, 0.1)

plt.pie(data_dibujo, explode=explode, labels=etiquetas, autopct='%1.2f%%', shadow=True, startangle=120, labeldistance= 1.2)
plt.axis('equal') 
plt.legend(etiquetas)

plt.title("Porcentaje de partidas finalizadas por genero")
plt.show()