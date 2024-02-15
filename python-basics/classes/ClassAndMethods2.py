def add(a,b):
    return a + b

class Test:
    def __init__(self, add_function):
        self.add_function = add_function

test = Test(add_function=add)
print(test.add_function(1,2))



print("***** Exercise *****")
class Monster:
    def __init__(self, func):
        self.func = func

class Attacks:
    def bite(self):
        print("Bite!")

    def strike(self):
        print("Strike!")

    def slash(self):
        print("Slash!")

    def kick(self):
        print("Kick!")

attacks = Attacks()
monster = Monster(func=attacks.bite)
monster.func()
