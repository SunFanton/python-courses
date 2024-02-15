import my_module
from my_module import sum_calculator

print(my_module.test_var)
my_module.test_function("Hola!")
test = my_module.Test()
test.do_something()
print(sum_calculator(1,2,3))

# Dunder main
print()
print("***** DUNDER MAIN *****")
my_module.show_name()
print(__name__) # si el archivo que se esta ejecutando es este, esto mostrara "__main__", de lo contrario mostrara el nombre del archivo en si
if __name__ == "__main__":
    print("This is the main file")