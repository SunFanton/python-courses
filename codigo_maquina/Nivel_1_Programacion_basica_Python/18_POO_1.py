from Tragamonedas_POO import Tragamonedas # from nombre_archivo.py import nombre_clase

tragamonedas1 = Tragamonedas(1, 1000)
tragamonedas2 = Tragamonedas(2, 1300, "Azul")

print(f"Tragamonedas1: id->{tragamonedas1.id}, premio->{tragamonedas1.premio}, color->{tragamonedas1.color}")
print(f"Tragamonedas2: id->{tragamonedas2.id}, premio->{tragamonedas2.premio}, color->{tragamonedas2.color}")
print(f"Id tragamonedas1:{id(tragamonedas1)} - Id tragamonedas2:{id(tragamonedas2)}")

print(tragamonedas1) # llama a __str__
print(tragamonedas2)

print(f"Son iguales tragamonedas1 y tragamonedas2?: {tragamonedas1 == tragamonedas2}") # llama a __eq__

"""
for i in range(100):
    numeros, mensaje = tragamonedas1.jugar()
    print(f"Tragamonedas1: {numeros} -> {mensaje}")
    numeros, mensaje = tragamonedas2.jugar()
    print(f"Tragamonedas2: {numeros} -> {mensaje}")
"""

