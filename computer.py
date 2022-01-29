import random
import fighter as f

class Computer(f.fighter):
    def __init__(self, currentHp):
        self.currentHp = currentHp

    def attack(self):
        return random.randint(1, 5)

