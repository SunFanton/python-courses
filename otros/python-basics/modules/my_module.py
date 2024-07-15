def test_function(content):
    print(f"This is an imported function with a parameter: {content}")


def sum_calculator(*nums):
    # print(args)
    return sum(nums)


def show_name():
    print(__name__) # Dunder main

class Test:
    def __init__(self):
        self.name = "My App"
        self.value = 12

    def do_something(self):
        print("Hello!")


test_var = "my test"
