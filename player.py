import random
import fighter as f

class Player(f.fighter):
    def __init__(self, currentHp):
        self.currentHp = currentHp

    def attack(self, attack):
        if attack == '1':
            return random.randint(2, 3)
        elif attack == '2':
            return random.randint(0, 5)