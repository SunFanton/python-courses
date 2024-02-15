"""
Son similares a los diccionarios, solo que unicamente tienen los valores, sin
las claves. Van tambien entre {}
Los duplicados son eliminados (cada valor es unico)
"""

my_set = {1,2,3,4,4}
print(my_set)
print(len(my_set))

my_set.add(5)
my_set.remove(2)
print(my_set)

# indexing and slicing does NOT work
# print(my_set[0]) da error
# print(my_set.pop()) quita y retorna primer elemento
print(list(my_set)[0])

# Los sets son muy utiles a la hora de compararse entre si
set1 ={1,2,3,4,4}
set2 = {4,5,6,7}

# Union
print(set1.union(set2))
print(set1 | set2)

# Interseccion
print(set1.intersection(set2))
print(set1 & set2)

# Difference
print(set1.difference(set2))
print(set1 - set2)

# exercise
test_list = [3,3,4,5,6,7,8,9,10,10,10,11]
print(len(test_list))
print(len(set(test_list)))
print(len(test_list) == len(set(test_list)))