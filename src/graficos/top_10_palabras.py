from matplotlib import pyplot as plt
import pandas as pd
import os

ruta = os.path.join(os.getcwd(), '..', 'datos', 'eventos_partidas.csv')

data_set = pd.read_csv(ruta, encoding='utf-8')

filas_respuestas_correctas = data_set[(data_set["texto_ingresado"] == data_set["respuesta"]) & (data_set["respuesta"] != "-")]

diez_palabras = filas_respuestas_correctas["respuesta"].sort_values(ascending=False).head(10)

print(diez_palabras)