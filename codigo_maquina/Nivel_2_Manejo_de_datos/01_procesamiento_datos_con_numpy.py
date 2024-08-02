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

arreglo[0] = 100
print(arreglo)

print(arreglo.size)
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