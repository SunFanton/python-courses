def update_health(amount):
    monster.health += amount

class Monster:
    def __init__(self, health, energy):
        self.health = health
        self.set_energy(energy)

    def update_energy(self, amount):
        self.energy += amount

    def set_energy(self, energy):
        new_energy = energy * 2
        self.energy = new_energy

    def get_damage(self, amount):
        self.health -= amount


monster = Monster(100,20)
print(monster.health)
monster.health += 20
print(monster.health)
update_health(20)
print(monster.health)
print(monster.energy)

print()
print("***** Exercise *****")

class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)

hero = Hero(damage=50, monster=monster)
print(monster.health)
hero.attack()
print(monster.health)