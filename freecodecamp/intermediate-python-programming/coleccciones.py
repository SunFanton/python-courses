from collections import Counter, namedtuple

# Counter: cuenta la cantidad de veces que aparece cada valor en un iterable
print("*** COUNTER ***")
a = "aaabbbccad"
my_counter = Counter(a)
print(my_counter)
print(my_counter.values())
print(my_counter.keys())
print(my_counter.items())
# mostrar el primer item mas comun, o con mas apariciones
print("Primer elemento más común o repetido:", my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

print("*** NAMEDTUPLE ***")
