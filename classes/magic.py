import random


class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

    def get_type(self):
        return self.type

    def generate_damage(self):
        low = self.dmg - 15
        high = self.dmg + 15
        return random.randrange(low, high)
