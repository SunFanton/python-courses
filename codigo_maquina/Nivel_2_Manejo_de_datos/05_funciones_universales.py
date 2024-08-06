import numpy as np
from time import perf_counter

# Ver todas las funciones universales de numpy en la documentacion oficial de Python

arreglo1 = np.array([1, 2, 3, 4, 5])
arreglo2 = np.array([11, 12, 13, 14, 15])

print("Operaciones aritmeticas componente a componente entre vectores")
print()
print("Suma ( version con add() ) ->", np.add(arreglo1, arreglo2))
print("Suma ( version con + ) ->", arreglo1 + arreglo2)
print("Resta ( version con substract() ) ->", np.subtract(arreglo1, arreglo2))
print("Resta ( version con - ) ->", arreglo1 - arreglo2)
print("Division ( version con divide() ) ->", np.divide(arreglo2, arreglo1))
print("Division ( version con / ) ->", arreglo2 / arreglo1)
print("Multiplicacion ( version con multiply() ) ->", np.multiply(arreglo1, arreglo2))
print("Multiplicacion ( version con multiply() ) ->", arreglo1 * arreglo2)
print("Potencia", np.power(arreglo1, 2))
print("Valor absoluto", np.absolute(arreglo1))

print()

# alturas promedios de paises
altura = np.array([1.74, 1.8, 1.78, 1.68, 1.78, 1.7, 1.74, 1.74, 1.73, 1.79,
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

# peso promedio de paises
peso = np.array([81.4, 88.7, 87.3, 62.7, 81.6, 80.9, 74.6, 84.7, 76.7, 88.3,
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

# funcion que no usa asi como esta funciones vectoriales de numpy
def calculate_imc(peso, altura):
    return peso / (altura * altura)

# se puede convertir dicha funcion en funcion universal, es decir, una funcion que use las funciones vectoriales que ofrece numpy
calculate_imc = np.frompyfunc(calculate_imc, 2, 1) # funcion a convertir, cant parametros de entrada de la func, cantidad parametros de salida de la func

# help(calculate_imc)

print(calculate_imc(peso, altura))

print()

print("Evaluamos eficiencia")

inicio = perf_counter()

for i in range(10000):
    calculate_imc(peso, altura)

final = perf_counter()

print("Numpy: %0.2f" % (final - inicio))

# Probemos la eficiencia NO usando numpy
altura = [1.74, 1.8, 1.78, 1.68, 1.78, 1.7, 1.74, 1.74, 1.73, 1.79,
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
           1.68, 1.63, 1.67]

# peso promedio de paises
peso = [81.4, 88.7, 87.3, 62.7, 81.6, 80.9, 74.6, 84.7, 76.7, 88.3,
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
         60.4, 82.7, 90.6, 79.8, 61.2, 62.5, 59.7]

def calculate_imc(peso, altura):
    return peso / (altura * altura)

inicio = perf_counter()

imc = []
for i in range(10000):
    for j in range(len(peso)):
        imc.append(calculate_imc(peso[j], altura[j]))

final = perf_counter()

print("Listas tradicionales: %0.2f" % (final - inicio))
