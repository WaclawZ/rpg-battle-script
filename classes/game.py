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
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkLow = atk - 10
        self.atkHigh = atk + 10
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Spell", "Items"]

    def generate_damage(self):
        return random.randrange(self.atkLow, self.atkHigh)

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

    def restore_mp(self, mana):
        self.mp += mana
        if self.mp > self.maxMp:
            self.mp = self.maxMp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxHp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxMp

    def choose_action(self):
        i = 1
        print("\n    " + bcolors.BOLD + self.name + bcolors.ENDC)
        print(bcolors.OKBLUE + bcolors.BOLD + "    Actions" + bcolors.ENDC)
        for action in self.actions:
            print("        " + str(i) + ".", action)
            i += 1

    def choose_spell(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    Spells" + bcolors.ENDC)
        for spell in self.magic:
            print("        " + str(i) + ".", spell.get_name(), "(cost:", str(spell.get_cost()) + ")")
            i += 1

    def choose_item(self):
        i = 1
        print("\n" + bcolors.OKBLUE + bcolors.BOLD + "    Items" + bcolors.ENDC)
        for item in self.items:
            it = item["item"]
            print("        " + str(i) + ".", it.get_name() + ":", it.get_description() + " (x" + str(item["quantity"]) + ")")
            i += 1

    def get_stats(self):
        hp_bar = ""
        hp_bar_ticks = (self.hp / self.maxHp) * 100 / 4

        mp_bar = ""
        mp_bar_ticks = (self.mp / self.maxMp) * 100 / 10

        while hp_bar_ticks > 0:
            hp_bar += "█"
            hp_bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_bar_ticks > 0:
            mp_bar += "█"
            mp_bar_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        print("                    _________________________           __________ ")
        print(bcolors.BOLD + self.name + ":   " +
              str(self.hp) + "/" + str(self.maxHp) + " |" + bcolors.OKGREEN + hp_bar + bcolors.ENDC +
              "|   " + bcolors.BOLD + str(self.mp) + "/" + str(self.maxMp) + " |" + bcolors.OKBLUE +
              mp_bar + bcolors.ENDC + "|")

