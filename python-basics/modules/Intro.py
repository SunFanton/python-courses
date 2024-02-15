"""
Los modulos son dependencias externas que necesitamos
para desarrollar diversas funcionalidades de nuestros programas
(como sucede en Java con sus dependencias, o los node_modules de
Node js)
Python cuenta con modulos de su biblioteca o libreria standard
(que ya vienen instalados junto con el propio Python), o bien
otro desarrollados por terceros que debemos instalar por separado
para utilizarlos
En este ejemplo, utilizaremos la libreria standard
"""

# Formas de importar modulos:

import string # importamos un modulo particular
# import random, string # importamos dos modulos juntos
# from math import factorial # se importa una funcionalidad especifica del modulo
from math import factorial as function_factorial # le cambiamos el nombre a la funcion en nuestro archivo
from random import * # importamos todas las funcionalidades pero sin tener que escribir rando.algo para invocarlas
from datetime import datetime

print("***** RANDOM *****")
random_number = randint(0,10)
print(random_number)
# print(help(random))

test_list = [45,"hello",3.9,True,21,1]
print(choice(test_list))

print()
print("***** STRING *****")
print(string.ascii_lowercase)

print()
print("***** MATH *****")
print(function_factorial(4))

print()
print("***** DATETIME *****")
x = datetime.now()
print(x)
print(f"Año: {x.year} - Mes: {x.strftime("%B")} - Día: {x.day}")