from matplotlib import pyplot as plt
import pandas as pd
import os

ruta = os.path.join(os.getcwd(), '..', 'datos', 'eventos_partidas.csv')

data_set = pd.read_csv(ruta, encoding='utf-8')

""" print(data_set["estado"].value_counts())

columna = data_set["estado"]
print(columna[0])
print(columna[1])
print(columna[2])
print(data_set.loc[10:14]) """

""" estado_finalizado = data_set[data_set["estado"] == "finalizado"]
estado_timeout = data_set[data_set["estado"] == "timeout"]
estado_error = data_set[data_set["estado"] == "error"]
estado_cancelado = data_set[data_set["estado"] == "cancelado"] """

cantidad_estados = data_set.groupby(["estado"]).size()

estado_finalizado = cantidad_estados["finalizado"]
estado_timeout = cantidad_estados["timeout"]
estado_error = cantidad_estados["error"]
estado_cancelado = cantidad_estados["cancelado"]

etiquetas = ["Partidas finalizadas", "Timeout", "Partidas abandonadas", "Cierre del programa"]

data_dibujo = [estado_finalizado, estado_timeout, estado_cancelado, estado_error]
explode = (0.1, 0.1, 0.1, 0.1)

plt.pie(data_dibujo, explode=explode, labels=etiquetas, autopct='%1.2f%%', shadow=True, startangle=120, labeldistance= 1.2)
plt.axis('equal') 
plt.legend(etiquetas)

plt.title("Porcentaje de partidas por estado")
plt.show()
