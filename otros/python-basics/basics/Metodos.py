"""
A diferencia de las funciones, los metodos siempre estan asociados a un objeto y se invocan o
llaman de manera similar a las funciones pero con el punto '.'
Por ejemplo: mi_variable_string.upper()
"""
test = "a word".upper()
print(test)

username = "JOhn SmithXX".title().strip("x")

print(dir(username)) # dir me devuelve el listado de metodos que el tipo de datos de "username" puede usar

print(username.isalpha())

exercise_string = "I like puppies"
exercise_string.replace("puppies", "kittens")
print(exercise_string)