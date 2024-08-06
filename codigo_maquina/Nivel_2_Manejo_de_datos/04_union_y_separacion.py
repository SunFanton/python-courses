import numpy as np

# vemos funciones de union y agregacion de arreglos de numpy

altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78])
peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6])

print(np.stack((altura, peso), axis=0)) # cada array en este cado se convierte en una fila de una matriz con filas y columnas
print(np.stack((altura, peso), axis=1))
print(np.concatenate((altura, peso))) # concatena un vector al lado del otro
union = np.stack((altura, peso), axis=0)

print()

print(union, type(union))

print()

separados1 = np.split(union, 2) # devuelve lista de vectores de numpy
print(separados1, type(separados1))

for i in separados1:
    print(i, type(i))


