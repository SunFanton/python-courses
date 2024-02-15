test_list = [1,2,3,4,5,6,7,8,9,10]
"""
Slicing: lista[start(included):end(not included):step]
"""
print(test_list[1:2]) # devuelve lista en este caso solo con segundo item
print(test_list[1:1])
print(test_list[1:3])
print(test_list[0:9:3])
print(test_list[8:0:-1])

default_slicing = test_list[::] # devuelve todos los elementos
print(default_slicing)

#exercise
example = test_list[7:0:-2]
print(example)
example = test_list[-3:-10:-2]
print(example)

# tuple slicing
test_tuple = (1,2,3,4,5,6,7,8,9,10)
print(test_tuple[0:5:3])