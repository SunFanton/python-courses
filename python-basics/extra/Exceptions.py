# Anticipating Exceptions
print("***** Anticipating Exceptions *****")
try:
    print("Try statement")
    # print(a)
    # print(1/0)
except ZeroDivisionError: # equivalente el catch
    print("You cannot divide by zero")
except NameError:
    print("The variable does not exist")
except: # Para capturar errores no previstos
    print("Unknown error")
else: # Para ejecutar codigo despues del try, sabiendo que no hubo errores
    print("Else statement")
finally: # Se ejecuta al final, independientemente si hubo o no errores
    print("Finally statement")

print()

# Raising (throwing) Exceptions
print("***** Raising (throwing) Exceptions *****")
var_must_be_string = "This is a string"

if isinstance(var_must_be_string, str):
    print(f"'{var_must_be_string}' is OK, it´s a string!")
else:
    raise TypeError("Must be a string")

print()

# Assert
print("***** Assert *****")
"""
assert es como un if, pero si la condicion evaluada es falsa, 
se detiene la ejecucion de todo el programa con un error
"""
a = 5
assert a == 5

print()

# Exercise
print("***** Exercise *****")
my_list = [1,2,3,4,5]
try:
    print(my_list[99])
except IndexError:
    print("The index does not exist")
else:
    print("The index exists :)")
finally:
    print("Finished")
