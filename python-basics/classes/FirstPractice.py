"""
Por convencion, los nombres de clases en Python se escriben en
CamelCase.
Recordar que las variables, por convencion, se escriben en
snake_case
"""

class Monster:

    #attributes (en este caso, globales para todas las instancias)
    health = 90
    energy = 40

    #methods
    def attack(self, amount): # los metodos de clases siempre necesitan definirse con al menos un parametro (en este cas self significa la propia instancia de clase que llama al metodo)
        print("The monster has attacked!")
        print(f'{amount} damage was dealt')
        monster.energy -= 20
        print('Monster energy: ', monster.energy)

    def move(self, speed):
        print('The monster has moved')
        print(f'It has speed of {speed}')


monster = Monster()
print(monster.health)
print(monster.energy)
monster.attack(40) # Python automaticamente pasa esta instancia de clase como argumento al metodo aunque nosotros no lo escribamos
monster.move(10)

monster1 = Monster()
monster1.attack(10)