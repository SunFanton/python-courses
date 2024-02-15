def decorator(func):
    def wrapper(*args, **kwargs):
        print("Decorator begins")
        func(*args, **kwargs)
        print("Decorator ends")
    return wrapper

@decorator
def func(param):
    print(param)


func("Hello")