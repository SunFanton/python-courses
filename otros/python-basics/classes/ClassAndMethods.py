"""
La direfencia entre una funcion y un metodo es que los metodos pertenecen
a objetos/clases, mientras que las funciones no.
Las funciones, ademas, son objetos en si mismas.
Otra diferencia es que las funciones (como test() aca abajo) al ver
los dunder methods que tiene encontramos el __call__ por defecto, lo
que implica que podemos llamar a la funcion asi por ej: test()
"""

def test():
    pass

letter = 'a'

print(dir(letter))
print(dir(test))