"""
Los for pueden usarse para iterar en listas, tuplas, sets y diccionarios
"""

basic_list = [1,2,3]
basic_tuple = (1,2,3)
basic_dictionary = { 1: "one", 2: "two", 3: "three" }
basic_set = {1,2,3}
basic_string = "one two three"
basic_number = 3

print(" ### LISTA ###")
for x in basic_list:
    print(x)

print(" ### TUPLA ###")
for x in basic_tuple:
    print(x)

print(" ### SET ###")
for x in basic_set:
    print(x)

print(" ### DICCIONARIO ###")
for x in basic_dictionary: # itera sobre las keys
    print(x)

for x in basic_dictionary.values(): # itera sobre los values
    print(x)

for x in basic_dictionary.items(): # itera sobre los pares clave-valor
    print(x)

print(" ### STRING ###")
for x in basic_string:
    print(x)

print(" ### NUMERO ###")
"""
Dado que el for en Python necesita iterar sobre un objeto iterable, 
para iterar una determianda cantidad de veces hasta un cierto numero, existe 
la funcion range(number) que devuelve una especie de iterable que permite realizar 
dicho loop. De esta forma, el for de abajo se podria traducri asi en otros lenguajes:
for(int i = 0; i < basic_number; i++)

La funcion range acepta tres parametros: range(start, end, step), parecido al slicing
Por defecto, start es 0 y step es 1. El valor de end no se incluye en la iteracion
"""
print(range(basic_number))
for x in range(basic_number):
    print(x)

for x in range(10,20,2):
    print(x)

print(" ### EJERCICIO ###")
# exercise
practice_list = [[10,40,20,50], [2,42,10], [101,12,4]]
for nested_list in practice_list:
    for value in nested_list:
        if 10 <= value < 50:
            print(value)
        elif value > 100:
            break