"""
A las funciones se les pasan parametros por referencia en unos casos y por valor en otros.
Por valor (copia del valor que contiene el parametro original) se pasan los tipos primitivos
Por referencia (la direccion de memoria del original) se pasan las estructuras de datos
como listas, tupas, diccionarios, etc, por la gran cantidad de datos que estos pueden almacenar y que seria muy dificil o poco eficiente hacer una copia para pasar a una funcion
"""

def doblar(referencia, valor):
    referencia *= 2
    valor *= 2
    print("DURANTE", referencia, valor)

estructura = ["a", "b", "c"]
primitiva = "abc"

print("ANTES", estructura, primitiva)
doblar(estructura, primitiva)
print("DESPUES", estructura, primitiva)


