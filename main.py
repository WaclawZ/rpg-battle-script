from classes.game import Person, bcolors
from classes.magic import Spell
from classes.inventory import Item

# Create offensive spells
fireball = Spell("Fireball", 10, 100, "offensive")
thunder = Spell("Thunder", 11, 110, "offensive")
blizzard = Spell("Blizzard", 10, 100, "offensive")
meteor = Spell("Meteor", 20, 200, "offensive")
earthquake = Spell("Earthquake", 14, 140, "offensive")

# Create defensive spells
cure = Spell("Cure", 12, 120, "defensive")
powerful_cure = Spell("Powerful cure", 18, 200, "defensive")

# Create Items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
big_potion = Item("Big potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super potion", "potion", "Heals 300 HP", 300)
elixir = Item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
mega_elixir = Item("Mega elixir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

# Inventory and spellBook
player_spells = [fireball, thunder, blizzard, meteor, earthquake, cure, powerful_cure]
player_items = [potion, elixir, grenade]
enemy_spells = [thunder, earthquake]
enemy_items = []

# Instantiate People
player = Person(480, 80, 60, 45, player_spells, player_items)
enemy = Person(1150, 40, 45, 24, enemy_spells, enemy_items)

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    choice = -1
    print("====================================")
    while choice != 0 and choice != 1 and choice != 2:
        player.choose_action()
        choice = int(input("Chose action:")) -1

    if choice == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for:", dmg, "dmg")
    elif choice == 1:
        player.choose_spell()
        spell_choice = int(input("Chose spell:")) - 1

        if spell_choice < 0 or spell_choice >= len(player.magic):
            continue

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
    elif choice == 2:
        player.choose_item()
        item_choice = int(input("Chose item:")) - 1

        if item_choice < 0 or item_choice >= len(player.items):
            continue

        item = player.items[item_choice]

        if item.get_type() == "potion":
            player.heal(item.get_prop())
            print(item.get_name(), "healed you by:", item.get_prop(), "hp")
        elif item.get_type() == "elixir":
            player.heal(item.get_prop())
            player.restore_mp(item.get_prop())
            print(item.get_name(), "restored your HP and MP")
        elif item.get_type() == "attack":
            enemy.take_damage(item.get_prop())
            print(item.get_name(), "dealt:", item.get_prop(), "dmg")

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
