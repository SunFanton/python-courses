def repetition_decorator(repetitions):
    def decorator(func):
        def wrapper():
            for r in range(repetitions):
                func()

        return wrapper

    return decorator


@repetition_decorator(5)  # veces que quiero repetir la ejecucion de la funcion
def func():
    print("Function")


# func = repetition_decorator(5)(func)
func()
