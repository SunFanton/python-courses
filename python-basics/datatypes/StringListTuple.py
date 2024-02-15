test_string = "this is a test"
test_list = [1,2,3,4]

# turning a string into a list or tuple
print(test_string.split()) # toma por defecto los espacios en blanco
print(test_string.split("t"))
print(list(test_string))
print(tuple(test_string))

# turn a list or tuple into string
print(' '.join(["one", "two"])) # la lista o tuple debe contener solo strings

print(type(str(test_list)))

# indexing on strings
print(test_string[0])
print(test_string[0:5])

# exercise
example = str(test_list).strip("[").strip("]").replace(", ", " ")
print(example)

