import numpy as np

altura_y_pesos = np.array([[ 1.74, 91.40 ],
                           [ 1.80, 88.70 ],
                           [ 1.78, 87.30 ],
                           [ 1.68, 62.70 ],
                           [ 1.78, 81.60 ]]) # [altura de una persona, peso de una persona]

# Estas funciones asi como estan no discriminan por columnas, sino que toman todos los datos del arreglo de numpy
# pero nos gustaria que funcionara de acuerdo al contexto de este caso (una columna son las alturas y la otra son los pesos)
print("Minimo", altura_y_pesos.min())
print("Maximo", altura_y_pesos.max())
print("Pos Minimo", altura_y_pesos.argmin())
print("Pos Maximo", altura_y_pesos.argmax())
print("Suma", altura_y_pesos.sum())
print("Promedio", altura_y_pesos.mean())

print()

print(altura_y_pesos.ndim) # nos devuelve la cantidad de dimensiones del array
print(altura_y_pesos.shape) # nos devuelve la cant de filas y columnas (si hubiera mas dimensiones nos devolveria mas datos tambien)

print()

print("Minimo", altura_y_pesos.min(axis=0)) # el eje 0 realiza el analisis por columna. esto nos devolveria un array con el minimo de cada columna
print("Maximo", altura_y_pesos.max(axis=0))
print("Pos Minimo", altura_y_pesos.argmin(axis=0))
print("Pos Maximo", altura_y_pesos.argmax(axis=0))
print("Suma", altura_y_pesos.sum(axis=0))
print("Promedio", altura_y_pesos.mean(axis=0))

altura_y_pesos = altura_y_pesos.transpose() # nos devuelve la traspuesta, es lo mismo que hacer arreglo.T

print("Minimo", altura_y_pesos.min(axis=1)) # el eje 1 realiza el analisis por fila. esto nos devolveria un array con el minimo de cada fila
print("Maximo", altura_y_pesos.max(axis=1))
print("Pos Minimo", altura_y_pesos.argmin(axis=1))
print("Pos Maximo", altura_y_pesos.argmax(axis=1))
print("Suma", altura_y_pesos.sum(axis=1))
print("Promedio", altura_y_pesos.mean(axis=1))

"""
Lo importante respecto a los ejes es:
- Conocer las dimensiones del arreglo con el que estemos trabajando
- Conocer que dato representa cada dimension en el contexto que estemos usando. 
Por ej, en este caso, en principio el array tenia que cada fila representaba una persona, y las columnas 
eran las alturas por un lado y los pesos por el otro de todas las personas. Entonces si queriamos analizar 
los datos en funcion de una de esas caracteristicas pero de todas las personas, teniamos que trabajar por 
columna, es decir, con el eje 0
"""
