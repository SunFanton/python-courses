import time


def decorator(func):
    def wrapper():
        print("Decorator begins")
        func()
        print("Decorator ends")
    return wrapper


def duration_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        duration = time.time() - start_time
        print(f'Duration: {duration}')
    return wrapper


def double_decorator(func):
    def wrapper():
        func()
        func()
    return wrapper


@double_decorator
@decorator
@duration_decorator
def func():
    print("Function")
    time.sleep(1)


# func = decorator(func) esto equivale a colocar @decorator en func original

"""
como func lo pase por parametro a la funcion que actua como 
decorator, es como si 'reescribiera' func, pero sin cambiarle nada y 
agregandole funcionalidad extra con el wrapper dentro del decorator.
entonces al llamar a func() al que termino llamando realmente es al 
wrapper (que es la funcion que envuelve a func original, y siendo 
wrapper lo que el decoraror me retorno)
"""
func()
