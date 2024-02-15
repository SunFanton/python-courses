"""
Las listas y las tuplas son similares.
Conceptualmente podemos pensarlos como los arrays, y una misma tupla o 
una misma lista puede almacenar tipos de datos diferentes entre si (incluso 
otra tupla u otra lista).
Las diferencias son:
- Las tuplas van entre parentesis mientras que las listas entre corchetes
- Las tuplas son inmutables a diferencia de las lista que si pueden cambiarse
"""

# list + funstions + methods
print("***** LISTS *****")
my_list = [1, 2, 3.1, "word"]
print(my_list)
print(len(my_list))
#my_list.clear()
my_list.append("se agrega algo al final de la lista")
print(my_list)

print()
# tuple
print("***** TUPLES *****")
my_tuple = (1, 2, 4.5, "word",  [6, 7, 8])
print(my_tuple)
# my_tuple.append(10) # esto da error porque las tuplas son inmutables

print()

# how to pick an element from a tuple or a list -> Indexing or slicing
"""
Si vamos de izquierda a derecha, los indices empiezan, como siempre, en 
cero, uno , dos, etc
"""
print(my_list[0])
print(my_tuple[len(my_tuple) - 1])
print(my_tuple[4][0])
"""
Si en cambio vamos de derecha a izquierda, los indices comienzan de -1, 
-2, etc
"""
print(my_tuple[-1]) # en indice -1 obtengo lo mismo que si hiciera: my_tuple[len(my_tuple) - 1]

# exercise
example = ['first entry', [123, 456, [0, 'Hello :)']], 'bye']
print(example[1][2][1])