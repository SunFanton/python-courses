"""
Los llamados dunder methods son los metodos del estilo __nombre__
Dunder -> double underscore (doble guion bajo)
Son los metodos que uno no llama explicitamente sino que es
Python es que los llama en determinadas ocasiones
Por ej, el metodo __init__ que Python llama al crear un objeto
o __len__ que Python llama la llamar a la funcion len
(el __len__ que llame va a ser el que esta definido en la clase
del objeto que se le pasa por argumento)
"""


class Monster:

    def __init__(self, health, energy): # este es el dunder method que mas utilizaremos
        # Attributes
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.health

    def __call__(self): # Permite que la instancia se pueda invocar asi por ej: monster1()
        print("The monster was called")

    def __add__(self, more_health):
        return self.health + more_health

    def __str__(self):
        return f"Monster - Energy: {self.energy}, Health: {self.health}"

    # Methods
    def attack(self, amount): # los metodos de clases siempre necesitan definirse con al menos un parametro (en este cas self significa la propia instancia de clase que llama al metodo)
        print("The monster has attacked!")
        print(f'{amount} damage was dealt')
        self.energy -= 20
        print('Monster energy: ', self.energy)

    def move(self, speed):
        print('The monster has moved')
        print(f'It has speed of {speed}')

monster1 = Monster(10,20)
monster2 = Monster(health = 50, energy = 100)

print(monster1.health)
print(monster2.health)
print(len(monster1))
print(dir(monster1))
print(monster1.__dict__)
monster1()
print(monster1 + 1) # llama a __add__()
print(str(monster1)) # llama a __str__()
print(monster1) # llama a __str__()