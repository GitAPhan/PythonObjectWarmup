class fighter:
    def __init__(self, currentHp):
        self.currentHp = currentHp

    def defend(self, damage):
        self.currentHp -= damage
    