import random

class Fighter:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


    def takeDamage(self, amount):
        self.health -= amount


    def attack(self):
        dmg = random.randrange(1, self.damage)
        return dmg

    def isDead(self):
        if self.health <= 0:
            return True

        return False


    def heal(self, amount):
        self.health += amount


    def ToString(self):
        output = ""

        output += "Name: " + self.name + "\n"
        output += "Health: " + str(self.health) + "\n"

        return output
 
class DualWieldingFighter(Fighter):
    def attack(self):
        dmg = random.randrange(1, self.damage) * 2
        return dmg


class ArmoredFighter(Fighter):
    def __init__(self, name, health, damage):
        super().__init__(name, age)
        self.damage = damage

    def takeDamage(self, amount):
        self.health -= (amount - defense)


class DodgeFighter(Fighter):
    def takeDamage(self, amount):
        if random.randint(1, 3) == 2:
            self.health -= 0
            print(self.name + " Dodged!")
        else:
            self.health -= amount

class ReviveFighter(Fighter):
    def isDead(self):
        if self.health <= 0:
            if random.randint(1, 3) == 2:
                self.health = health + 25
                print(self.name + " Revived!")
                return False
            return True
        return False
