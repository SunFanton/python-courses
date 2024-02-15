"""
En Python existe la herencia multiple.
Es decir, una clase puede heredar de un numero ilimitado de clases
"""

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    # methods
    def attack(self, amount):
        print("The monster has attacked!")
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved")
        print(f'It has speed of {speed}')

# La clase Shark hereda de Monster
class Shark(Monster):
    def __init__(self, speed, health, energy):
        # Forma 1 de llamar al init de la clase padre:
        #Monster.__init__(self, health, energy)
        # Forma 2 (utilizada hoy en dia):
        super().__init__(health, energy)
        self.speed = speed

    def bite(self):
        print("The shark has bitten!")

    # sobreescribe metodo del padre
    def move(self):
        print("The shark has moved")
        print(f'The speed of the shark is {self.speed}')


class Scorpion(Monster):
    def __init__(self, poison_damage, health=100, energy=70):
        super().__init__(health, energy)
        self.poison_damage = poison_damage

    def attack(self):
        print("The scorpion has attacked!")
        print(f'Poison damage: {self.poison_damage}')


print("***** Shark *****")
shark = Shark(speed=120, health=100, energy=50)
print(shark.health)
print(shark.energy)
print(shark.speed)
print(shark.bite())
print(shark.move())

print()
print("***** Scorpion *****")
scorpion = Scorpion(poison_damage=30, health=120)
print(scorpion.energy)
scorpion.attack()
scorpion.move(30)