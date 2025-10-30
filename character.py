import random as rd
class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power * (rd.randint(30,90) / 100)

    def attack(self, other):
        other.hp -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power:.2f} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp:.2f} HP"
    
    def recovery(self):
        heal = self.hp * (rd.randint(5,20) / 100)
        self.hp += heal
        return f"{self.name}: get recovery by {heal:.2f} HP"
