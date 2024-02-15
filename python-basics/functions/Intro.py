"""
Definicion de funciones en Python
"""
def test_function():
    print("Hello")
    test = 1 + 2
    print(test)

def calculator(num1, num2):
    result = num1 + num2
    print(result)
def better_calculator(num1,num2,operation):
    match(operation):
        case "plus":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        case "minus":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case _: result = "No operation found"


#test_function()
#calculator(1,2)
better_calculator(1,2,"minus")
better_calculator(1,2,"plus")