# List unpacking to use an unlimited number of arguments
def print_all(first, *arguments, extra):
    print(first)
    print(arguments) # convertido en tupla
    print(extra)
    # print all arguments
    for argument in arguments:
        print(argument)


# keyword unpacking
def print_more(**arguments):
    print(arguments) # convertido en diccionario (como pasar un objeto en javascript)


def print_even_more(*args, **kwargs):
    print(args) # tupla
    print(kwargs) # diccionario

def calculator(*args):
    '''
    result = 0
    for arg in args:
        result += arg
    '''
    result = sum(args)
    print(result)

# print_all(1,2,3,"4",extra="hello")
# print_more(arg1=1,arg2=2,arg3="hello")
# print_even_more(1,2,3, one="1", two="2", three="3")

# exercise
calculator(1,2,3,4,5)