a = 10 # variable global

def test_func():
    a = 2 # variable local de esta funcion (Python la considera diferente de la global)
    print(a)

def test_func_2():
    a = 200 # variable local de esta funcion
    print(a)

def test_func_3():
    # a += 2 # se refiere a la variable global, pero esto da error porque las variables globales no pueden cambiarse dentro de una funcion
    print(a)

def test_func_4(a):
    a += 2 # se refiere a la variable que recibi por parametro
    return a

test_func()
test_func_2()
test_func_3()
print(test_func_4(a)) # le estoy pasando la variable global

# exercise
multiplier = 2
has_calculated = False
def multiply_calculator(num):
    global has_calculated
    result = num * multiplier
    has_calculated = True
    return result

print(multiply_calculator(3))