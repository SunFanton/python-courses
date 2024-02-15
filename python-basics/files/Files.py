# open and close the file manually
# file = open('test.txt')
# print(list(file))
# file.close()

# open and close the file automatically
with open('test.txt') as file:
    # print(file.read())
    for line in list(file):
        print(line)

# write some file
"""
la funcion open() recibe el path como argumento, y el segundo argumento 
es la accion a ejecutar con el archivo (r -> read, a -> append, w -> write)
el valor por defecto es r
"""
with open('test.txt', 'a') as file:
    file.write("***** Mas texto *****")

with open('test2.txt', 'w') as file:
    file.write("***** Mas texto *****")