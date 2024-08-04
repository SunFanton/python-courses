import numpy as np

"""
Los arreglos en numpy son como las listas de Python pero mucho mas eficientes
ya que sus rutinas se encuentran implementadas en C o C++
"""

arreglo = np.array([1, 2, 3, 4, 5, 6])
arreglo = np.arange(1, 7) # geneera arreglo de elementos del 1 al 6

print(arreglo)
print(arreglo[0])
print(arreglo[1:4])
print(arreglo[::-1])

arreglo[0] = 100
print(arreglo)

print(arreglo.size) # muestra la cantidad total de elementos
print(len(arreglo))

arreglo.sort()

print(arreglo.dtype) # nos muestra el tipo de dato del arreglo, junto a la cantidad de bits de cada elemento del arreglo

print()

# es importante la cantidad de bytes al momento de procesar datos de un tamaño u otro

# Cada elemento del arreglo tendra la cantidad de bytes default (4 bytes)
arreglo = np.array([1, 2, 3, 4, 5, 6], dtype="i")
print(arreglo, arreglo.dtype, arreglo.itemsize)

# Cada elemento del arreglo tendra 2 bytes
arreglo = np.array([1, 2, 3, 4, 5, 6], dtype="i2")
print(arreglo, arreglo.dtype, arreglo.itemsize)

# Cada elemento del arreglo tendra 4 bytes
arreglo = np.array([1, 2, 3, 4, 5, 6], dtype="i4")
print(arreglo, arreglo.dtype, arreglo.itemsize)

# Cada elemento del arreglo tendra 8 bytes
arreglo = np.array([1, 2, 3, 4, 5, 6], dtype="i8")
print(arreglo, arreglo.dtype, arreglo.itemsize)

print()

arreglo = np.array([1, 2, 3, 4, 5, 6])
print(arreglo.shape) # nos muestra la cant de filas y columnas
# reshape nos muestra como quedaria el arreglo con la cantidad de filas y columnas que le pasemos, pero no cambia el arreglo original
# para cambiar el arreglo original debemos hacer arreglo = arreglo.reshape...
print(arreglo.reshape((2, 3)))
print(arreglo.reshape((3, 2)))

print()

print(np.append(arreglo, 7)) # me muestra el arreglo con el 7 agregago al final pero sin modificar el arreglo original
print(np.insert(arreglo, 1, 7)) # inserta en el arreglo el valor 7 en la pos 1, empujando los elementos ya existentes. asi como esta, esta funcion tampoco modifica el arreglo original
print(np.delete(arreglo, 2)) # borrar elemento de la posicion 2, igual que antes, no modifica el arreglo original
for pos in [1, 7]:
    arreglo = np.insert(arreglo, pos, 7)
print(arreglo)
print(np.where(arreglo == 7)) # me muestra las posiciones donde se encuentran los numeros que son iguales a 7

print()

print(arreglo + 1) # suma el valor 1 componente a componente
print(arreglo * 2)
print(arreglo * arreglo)

print()

# Ejercicio: indice de masa corporal (imc)

alturas = np.array([1.74, 1.8, 1.78, 1.68, 1.78, 1.7, 1.74, 1.74, 1.73, 1.79,
           1.78, 1.72, 1.65, 1.78, 1.7, 1.68, 1.79, 1.68, 1.82, 1.72,
           1.75, 1.66, 1.67, 1.79, 1.75, 1.65, 1.78, 1.73, 1.71, 1.81,
           1.73, 1.71, 1.68, 1.74, 1.75, 1.68, 1.74, 1.81, 1.73, 1.82,
           1.8, 1.67, 1.73, 1.7, 1.73, 1.7, 1.81, 1.81, 1.76, 1.82, 1.68,
           1.74, 1.65, 1.8, 1.78, 1.7, 1.68, 1.78, 1.79, 1.73, 1.64, 1.67,
           1.69, 1.74, 1.76, 1.66, 1.66, 1.73, 1.79, 1.81, 1.78, 1.63,
           1.76, 1.72, 1.71, 1.7, 1.62, 1.8, 1.75, 1.8, 1.78, 1.78, 1.76,
           1.65, 1.65, 1.68, 1.74, 1.75, 1.69, 1.75, 1.7, 1.83, 1.64, 1.7,
           1.69, 1.69, 1.64, 1.69, 1.77, 1.8, 1.78, 1.69, 1.7, 1.7, 1.7,
           1.63, 1.73, 1.84, 1.66, 1.78, 1.8, 1.79, 1.78, 1.74, 1.77,
           1.73, 1.77, 1.76, 1.75, 1.8, 1.75,  1.8, 1.79, 1.71, 1.73,
           1.59, 1.76, 1.75, 1.71, 1.76, 1.8, 1.68, 1.74, 1.77, 1.73,
           1.68, 1.63, 1.67])

pesos = np.array([81.4, 88.7, 87.3, 62.7, 81.6, 80.9, 74.6, 84.7, 76.7, 88.3,
         84.6, 74, 57.7, 84.1, 79.7, 63.8, 88.4, 71.2, 87.1, 67, 80.7,
         74.7, 60.5, 85.9, 72.4, 59.7, 87.3, 85.7, 64.1, 91.9, 82.8, 75.7,
         60.2, 73.1, 74.7, 65.9, 80.9, 91.3, 76, 86.8, 80.7, 74.2, 83.1,
         77.8, 84.5, 58.8, 89.5, 87, 84, 89.9, 56.5, 80.2, 61.8, 86.3,
         82.6, 69.4, 65.8, 79.3, 88.1, 78.5, 69.1, 62.5, 74, 74.4, 87.6,
         59.6, 61.4, 83.2, 89.2, 89.2, 103.7, 67.9, 85.4, 69.5, 75.7,
         83.9, 59.5, 87.9, 82.6, 88.1, 86.2, 88.9, 84.4, 58.4, 61.5, 69.2,
         84.2, 78, 81.1, 81.5, 74.7, 90.4, 59.2, 79.3, 65.1, 93, 60.5,
         76.4, 98.8, 89.1, 88.9, 61.1, 76.6, 86, 75.5, 66.9, 79.4, 87.9,
         72.3, 93.8, 89, 90.7, 86.7, 77.6, 85.1, 91.8, 103.2, 91.1, 67,
         86.9, 78.7, 87.1, 85.5, 69.8, 75, 53.9, 99, 93.7, 88, 79.4, 87.6,
         60.4, 82.7, 90.6, 79.8, 61.2, 62.5, 59.7])

imc = pesos / (alturas * alturas)
"""
En esta formula lo que ocurre es que alturas * alturas nos devuelve un vector que es resultado de que el 
vector alturas haga esto: [alturas[0] * alturas[0], alturas[1] * alturas[1], ..... ]
Y luego el vector pesos se divide por ese resultado, obteniendo un nuevo vector:
[pesos[0] / (alturas[0] * alturas[0]), pesos[1] / (alturas[1] * alturas[1]), ..... ]
Es decir, las operaciones se hacen componente a componente, al igual que ocurre por ejemplo cuando 
se suman dos vectores

Esto no es una operacion iterativa, sino vectorial, lo que la hace computacionalmente eficiente
"""

"""
Tradicionalmente, usando listas comunes, hubieramos hecho esto asi, que es mucho menos eficiente:
imc = []
for i in range(alturas.size):
    imc.append(float(pesos[i] / (alturas[i] * alturas[i])))
"""

"""
Numpy tiene ademas muchas funciones de estadistica implementadas, por ej el promedio
"""
print(imc.mean())