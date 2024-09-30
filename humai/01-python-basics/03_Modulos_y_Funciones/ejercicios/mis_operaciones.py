def factorial_recursivo(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial_recursivo(num-1)
def factorial_iterativo(num):
    resul = 1
    for i in range(1, num+1):
        resul *= i
    return resul
