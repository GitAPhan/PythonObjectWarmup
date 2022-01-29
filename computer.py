import random

class Computer:
    def __init__(self, currentHp):
        self.currentHp = currentHp

    def attack(self):
        return random.randint(1, 5)

    def defend(self, damage):
        self.currentHp -= damage