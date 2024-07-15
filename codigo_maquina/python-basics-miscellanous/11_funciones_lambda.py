
suma = lambda a, b : a + b # 2 parametros
multiplicacion = lambda a, b, c : a * b * c # 3 parametros
constante = lambda : 10 # sin parametros

print(suma(2,3), multiplicacion(2,3,4), constante())

# ejemplo funciones lambda como funciones anonimas:

personas = [("Juan", 82, 5), ("Luisa", 41, 10), ("Adolfo", 75, 20)] 

print("Desordenada", personas)
personas.sort() # ordenara por defecto usando el nombre
print("Ordenada por nombre", personas)

# pero podemos establecer el criterio de orden pasando a sort() una funcion lambda (funcion anonima)

personas.sort(key=lambda persona : persona[1]) # ordena por edad (segundo elemento de cada tupla de la lista

print("Ordenada por edad", personas)

personas.sort(key=lambda persona : persona[1] + persona[2])

print("Ordenada por edad + cant años credito", personas)
