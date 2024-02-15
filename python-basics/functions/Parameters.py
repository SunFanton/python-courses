# Funcion con valores por defecto para sus parametros:
def test_function(arg1="Argument 1",
                  arg2="Argument 2",
                  arg3="Argument 3",
                  arg4="Argument 4"):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

def greeter(
        person='Person',
        greet='Hello',
        weekday=None):
    print(f'{person} {greet}')
    print(f'It is {weekday}')


# Formas de llamar a una funcion:
print("----- FORMA 1 -----")
test_function(1, "2", True, [1, "2", "test"])
print("----- FORMA 2 -----")
test_function(
    arg4=1,
    arg2="2",
    arg3=True,
    arg1=[1, "2", "test"]
)
print("----- FORMA 3 -----")
test_function(
    1,
    arg2="2",
    arg3=True,
    arg4=[1, "2", "test"]
)
print("----- FORMA 4 -----")
test_function()

print("----- EJERCICIO -----")
greeter("Sol", weekday="Monday")