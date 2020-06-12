import random


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkLow = atk - 10
        self.atkHigh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Spell"]

    def generate_damage(self):
        return random.randrange(self.atkLow, self.atkHigh)

    def generate_spell_damage(self, i):
        md_low = self.magic[i]["dmg"] - 5
        md_high = self.magic[i]["dmg"] + 5
        return random.randrange(md_low, md_high)

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def heal(self, health):
        self.hp += health
        if self.hp > self.maxHp:
            self.hp = self.maxHp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMp

    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_cost(self, i):
        return self.magic[i]["cost"]

    def choose_action(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Actions" + bcolors.ENDC)
        for action in self.actions:
            print(str(i) + ":", action)
            i += 1

    def choose_spell(self):
        i = 1
        print(bcolors.OKBLUE + bcolors.BOLD + "Spells" + bcolors.ENDC)
        for spell in self.magic:
            print(str(i) + ":", spell["name"], "(cost:", str(spell["cost"]) + ")")
            i += 1
