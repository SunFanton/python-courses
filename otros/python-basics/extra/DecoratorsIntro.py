"""
Los decorators son funciones que 'envuelven' otras funciones dentro de si.
Esto nos permite ejecutar codigo antes de dichas funciones internas o despues
Y esto permite ademas que no haga falta cambiar nada en dicha funcion interna
"""


def func():
    print()
    print("INNER WRAPPER FUNCTION")
    print("Function")
    print()


def wrapper(function): # recibe una funcion por parametro
    print()
    print("***** WRAPPER *****")
    print("Hello")
    function()
    print("Goodbye")


def function_generator():
    print()
    print("***** FUNCTION GENERATOR *****")
    def new_funtion():
        print()
        print("***** GENERATED FUNCTION *****")
        print("New function")
    return new_funtion


# func()
# print(func)
print(wrapper(func))
new_funtion = function_generator()
new_funtion()