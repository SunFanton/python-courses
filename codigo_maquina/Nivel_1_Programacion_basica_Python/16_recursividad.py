from time import perf_counter

"""

CASO BASE: caso mas simple o ultimo caso

CASO RECURSIVO: caso donde la funcion se llama a si misma, pero resolviendo un problema menor

"""

"""
Imprimir del 5 al 0

Pasos:
Imprimir 5 + Imprimir del 4 al 0
Imprimir 4 + Imprimir del 3 al 0
Imprimir 3 + Imprimir del 2 al 0
Imprimir 2 + Imprimir del 1 al 0
Imprimir 1 + Imprimir 0 -> caso base

"""

def recursiva(n):
    print(n) # case base (y recursivo tambien, para este caso)
    if n > 0:
        recursiva(n - 1) # caso recursivo


"""
0! =           = 1 -> CASO BASE
1! = 1         = 1
2! = 1 * 2     = 2
3! = 1 * 2 * 3 = 6
...

"""

def factorial_it(n):
    if n == 0 or n == 1:
        return 1
    resul = 1
    for i in range(2, n+1):
        resul *= i
    return resul


def factorial_recursivo(n):
    if n == 0 or n == 1: # caso base
        return 1
    return n * factorial_recursivo(n - 1) # caso recursivo


recursiva(5)

print("Factorial iterativo")
for i in range(6):
    print(f"{i}! = {factorial_it(i)}")

print("Factorial recursivo")
for i in range(6):
    print(f"{i}! = {factorial_recursivo(i)}")


inicio = perf_counter()
for i in range(1000000):
    factorial_it(100)
fin = perf_counter()
print("Tardanza con factorial iterativo: %0.4f" % (fin - inicio))

inicio = perf_counter()
for i in range(1000000):
    factorial_recursivo(100)
fin = perf_counter()
print("Tardanza con factorial recursivo: %0.4f" % (fin - inicio))

