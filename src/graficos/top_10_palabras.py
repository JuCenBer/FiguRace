from matplotlib import pyplot as plt
import pandas as pd
import os

ruta = os.path.join(os.getcwd(), '..', 'datos', 'eventos_partidas.csv')

data_set = pd.read_csv(ruta, encoding='utf-8')

filas_respuestas_correctas = data_set[(data_set["texto_ingresado"] == data_set["respuesta"]) & (data_set["respuesta"] != "-")]

diez_palabras = filas_respuestas_correctas["respuesta"].sort_values(ascending=False).head(10)

#Aca va el grafico barras
etiquetas = ["Hombres", "Mujeres", "No Binario"]

data_dibujo = [cant_hombres, cant_mujeres, cant_nobinario]
explode = (0.1, 0.1, 0.1)

plt.pie(data_dibujo, explode=explode, labels=etiquetas, autopct='%1.2f%%', shadow=True, startangle=120, labeldistance= 1.2)
plt.axis('equal') 
plt.legend(etiquetas)

plt.title("Porcentaje de partidas finalizadas por genero")
plt.show()