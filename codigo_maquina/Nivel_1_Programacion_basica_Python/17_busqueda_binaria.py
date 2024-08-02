"""
La busqueda binaria, que se usa para buscar un elemento dentri de una lista, 
parte de la base que la lista ya se encuentra ordenada

Variables para realizar la busqueda (indices de la lista):
bajo
alto
centro = (bajo + alto) // 2

[ 11    12    13    14    15    16    17 ]  dato 15
bajo               centro             alto  -> valores iniciales

lista[centro] < 15 ? si es asi, el 15 esta a la derecha
bajo ahora sera = centro + 1
alto no se mueve

[ 11    12    13    14    15    16    17 ]
                         bajo  centro alto

lista[centro] < 15 ? si no es asi, el 15 esta a la izquierda
alto ahora sera = centro - 1
bajo no se mueve

[ 11    12    13    14    15    16    17 ]
                         bajo
                         centro
                         alto

Se ha convergido y se ha hallado el resultado

"""

def busqueda_iterativa(lista, dato):
    bajo = 0
    alto = len(lista) - 1
    centro = (bajo + alto) // 2

    while bajo <= alto:
        if lista[centro] == dato:
            return centro
        elif lista[centro] < dato:
            bajo = centro + 1
        elif lista[centro] > dato:
            alto = centro - 1
        
        centro = (bajo + alto) // 2

    return -1


def busqueda_recursiva(lista, dato, bajo, alto):
    if bajo > alto:
        return -1
    centro = (bajo + alto) // 2
    if lista[centro] == dato: # caso base
        return centro
    elif lista[centro] < dato: # casos recursivos
        bajo = centro + 1
    else:
        alto = centro - 1
    return busqueda_recursiva(lista, dato, bajo, alto)
    


lista = [11,12,13,14,15,16,17]
try:
    print("Búsqueda binaria iterativa")
    for i in range(10, 19):
        pos = busqueda_iterativa(lista,i)
        print(f"El dato {i} se encuentra en la posición {pos}")

    print()
    
    print("Búsqueda binaria recursiva")
    for i in range(10, 19):
        pos = busqueda_recursiva(lista,i, 0, len(lista) - 1)
        print(f"El dato {i} se encuentra en la posición {pos}")

    print()
    
    print("Búsqueda binaria definida en Python")
    for i in range(11, 18): # altero los indices porque el metodo index lanza ValueError si no se encuentra
        pos = lista.index(i)
        print(f"El dato {i} se encuentra en la posición {pos}")
except Exception as e:
    print("Ha ocurrido un error. Intente nuevamente")

