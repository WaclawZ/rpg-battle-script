from classes.game import Person, bcolors
from classes.magic import Spell

# Create offensive spells
fireball = Spell("Fireball", 10, 100, "offensive")
thunder = Spell("Thunder", 11, 110, "offensive")
blizzard = Spell("Blizzard", 10, 100, "offensive")
meteor = Spell("Meteor", 20, 200, "offensive")
earthquake = Spell("Earthquake", 14, 140, "offensive")

# Create defensive spells
cure = Spell("Cure", 12, 120, "defensive")
powerful_cure = Spell("Powerful cure", 18, 200, "defensive")

# Instantiate People
player = Person(480, 80, 60, 45, [fireball, thunder, blizzard, meteor, earthquake, cure, powerful_cure])
enemy = Person(1150, 40, 45, 24, [thunder, earthquake])

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    index = -1
    print("====================================")
    while index != 0 and index != 1:
        player.choose_action()
        choice = input("Chose action:")
        index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for:", dmg, "dmg")
    elif index == 1:
        player.choose_spell()
        spell_choice = int(input("Chose spell:")) - 1
        spell = player.magic[spell_choice]

        if player.get_mp() < spell.get_cost():
            print(bcolors.FAIL + "You don't have enough magic points for this spell" + bcolors.ENDC)
            continue

        magic_dmg = spell.generate_damage()
        player.reduce_mp(spell.get_cost())

        if spell.get_type() == "offensive":
            enemy.take_damage(magic_dmg)
            print(spell.get_name(), "dealt:", magic_dmg, "dmg")
        elif spell.get_type() == "defensive":
            player.heal(magic_dmg)
            print("You have been healed by:", magic_dmg, "hp")

    enemy_choice = 0

    if enemy_choice == 0 and enemy.get_hp() > 0:
        enemy_dmg = enemy.generate_damage()
        player.take_damage(enemy_dmg)
        print("Enemy attacked for:", enemy_dmg, "dmg")

    print("------------------------------------")
    print("Enemy HP:", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC)
    print("Enemy MP:", bcolors.FAIL + str(enemy.get_mp()) + "/" + str(enemy.get_max_mp()) + bcolors.ENDC + "\n")
    print("Your HP:", bcolors.OKGREEN + str(player.get_hp()) + "/" + str(player.get_max_hp()) + bcolors.ENDC)
    print("Your MP:", bcolors.OKBLUE + str(player.get_mp()) + "/" + str(player.get_max_mp()) + bcolors.ENDC)

    if enemy.get_hp() == 0:
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "You won!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print("\n" + bcolors.FAIL + bcolors.BOLD + "You lost!" + bcolors.ENDC)
        running = False
