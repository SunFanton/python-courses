"""
Python permite la herencia multiple ilimitada

Cuando una clase hereda de dos clases o mas y necesitamos saber a
cual constructor de que clase padre llamar primero, debemos fijarnos el
orden en que declaramos la herencia de la clase.
En esta caso Shark(Monster,Fish), en primer lugar llamariamos al
constructor de Monster y luego al constructos de la clase Fish
Tambien podemos usar mro (method resolution order):
Por ej: print(Shark.mro())

Ahora bien, si el metodo super()__init__(...) lo llamamos pasando
argumentos nombrados, como el ejemplo de abajo, el orden en que pasemos esos
argumetos no importara porque Python automaticamente resolvera a que constructor
padre llamara primero y a cual despues. Y para esto es muy IMPORTANTE
que en las clases padres tengamos como argumento extra el **kwargs (y de ahi
que en la clase hija debamos pasar argumentos nombrados).
El **kwargs en cada clase padre se pasara como argumento dentro del __init__
como super()__init__(**kwargs) para que Python resuelva cual es la
siguiente clase a la que debera llamar
"""

class Monster:
    def __init__(self, health, energy, **kwargs):
        #print(kwargs)
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

    # methods
    def attack(self, amount):
        print("The monster has attacked!")
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved")
        print(f'It has speed of {speed}')



class Fish:
    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print(f'The fish is swimming at a speed of {self.speed}')


class Shark(Fish,Monster):
    def __init__(self, bite_strength, health, energy, speed, has_scales):
        super().__init__(
            health=health,
            energy=energy,
            speed=speed,
            has_scales=has_scales)
        self.bite_strength = bite_strength



shark = Shark(
    bite_strength=50,
    health=200,
    energy=55,
    speed=120,
    has_scales=False)
print(shark.bite_strength)
print(shark.health)
print(shark.energy)
print(shark.has_scales)
print(shark.speed)
