"""
Los diccionarios son muy similares a los objetos de Javascript
"""

test_dict = {
    'A': 123,
    'B': [1,2,3],
    1: True
}

#basics
print(test_dict)
print(test_dict.values())
print(type(test_dict.values()))
print(test_dict.keys())
print(test_dict.items())
print(len(test_dict))

#converting a dict
print(list(test_dict)) # devulve lista solo de las keys
print(tuple(test_dict))

# indexing with dictionaries
print(test_dict["A"]) # tira error si no encuentra esa key
print(test_dict.get("A"))
print(test_dict.get("X")) # no tira error si no encuentra esa key

#exercise
test_dict.update({'C': (1,2,3)})
test_dict.update(D = "hola", E = "esto es Python")
test_dict["E"] = 100
print((test_dict))