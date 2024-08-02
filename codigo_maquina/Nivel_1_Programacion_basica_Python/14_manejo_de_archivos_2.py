pasajeros = {}

with open("datos_metro.csv", "r", encoding="utf-8") as archivo:
    archivo.readline()
    estaciones = archivo.readlines()
    for estacion in estaciones:
        lista = estacion.strip().split(",")
        # Forma 1 (usando list comprehension):
        #pasajeros[lista[0]] = [int(cant) for cant in lista[1:]]
        # Forma 2 (usando map):
        cantidades = lista[1:]
        pasajeros[lista[0]] = list(map(int, cantidades)) # aplicar a cada elem de cantidades la funcion int()

print(pasajeros)