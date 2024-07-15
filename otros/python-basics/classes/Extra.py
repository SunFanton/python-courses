"""
Temas extras:
1) Atributos privados:
Son aquellos atributos que en el __init__ de la clase estan declarados
como _nombreDelAtributo
Por convencion, el _ indica a los desarrolladores que este tipo de
atributos son privados y no deberian cambiarse desde fuera de la clase
(tecnicamente sí se puede, pero por convencion no)

2) hasattr y setattr:
hasattr(object, 'nombre_atributo') -> devuelve boolean

setattr(object, 'nombre_atributo', valueDelAtributo)
este ultimo le da al atributo referenciado un valor (si el atributo no existe
en el objeto, lo crea)
Es lo mismo que hacer: object.nombre_atributo = value

3) doc:
Documentacion de la clase

"""

class Monster:
    '''A monsters that has some attributes'''
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
        self._id = 5 # atributo privado

    # methods
    def attack(self, amount):
        print("The monster has attacked!")
        print(f'{amount} damage was dealt')
        self.energy -= 20

    def move(self, speed):
        print("The monster has moved")
        print(f'It has speed of {speed}')


monster = Monster(20,10)
print(hasattr(monster, 'health'))
print(hasattr(monster, 'speed'))
# setattr(monster, 'weapon', 'Sword')
# print(monster.weapon)
new_attributes = (['weapon', 'Sword'], ['armor', 'Shield'], ['potion', 'Mana'])
for attr,value in new_attributes:
    setattr(monster,attr,value)

print(vars(monster)) # nos muestra los atributos de este objeto

print(monster.__doc__)
help(monster)
