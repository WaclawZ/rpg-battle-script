import random
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
player_items = [{"item": potion, "quantity": 15}, {"item": big_potion, "quantity": 5},
                {"item": super_potion, "quantity": 5}, {"item": elixir, "quantity": 5},
                {"item": mega_elixir, "quantity": 2}, {"item": grenade, "quantity": 3}]
enemy_spells = [thunder, earthquake]
enemy_items = []

# Instantiate People
player1 = Person("Frodo  ", 375, 40, 50, 32, player_spells, player_items)
player2 = Person("Gandalf", 520, 99, 40, 28, player_spells, player_items)
player3 = Person("Boromir", 650, 60, 80, 70, player_spells, player_items)
enemy1 = Person("Imp  ", 1000, 10, 30, 25, [], [])
enemy2 = Person("Troll", 2500, 40, 100, 68, enemy_spells, enemy_items)
enemy3 = Person("Imp  ", 1000, 10, 30, 25, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]

running = True

print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACKS" + bcolors.ENDC)

while running:
    print("====================================")

    # Players stats
    print("\n\n")
    print("NAME                HP                                  MP")
    for player in players:
        player.get_stats()

    print("\n")
    for enemy in enemies:
        enemy.get_stats()

    # Players turn
    for player in players:
        choice = -1
        while choice != 0 and choice != 1 and choice != 2:
            player.choose_action()
            choice = int(input("    Chose action:")) - 1

        if choice == 0:
            dmg = player.generate_damage()
            enemy_index = player.choose_target(enemies)
            enemies[enemy_index].take_damage(dmg)
            print(bcolors.FAIL + "You attacked " + enemies[enemy_index].name.strip() + " for:", dmg,
                  "dmg" + bcolors.ENDC)
        elif choice == 1:
            player.choose_spell()
            spell_choice = int(input("    Chose spell:")) - 1

            if spell_choice < 0 or spell_choice >= len(player.magic):
                continue

            spell = player.magic[spell_choice]

            if player.get_mp() < spell.get_cost():
                print(bcolors.FAIL + "You don't have enough magic points for this spell" + bcolors.ENDC)
                continue

            magic_dmg = spell.generate_damage()
            player.reduce_mp(spell.get_cost())

            if spell.get_type() == "offensive":
                enemy_index = player.choose_target(enemies)
                enemies[enemy_index].take_damage(magic_dmg)
                print(bcolors.OKBLUE + spell.get_name(), "dealt:", magic_dmg,
                      "dmg to " + enemies[enemy_index].name + bcolors.ENDC)
            elif spell.get_type() == "defensive":
                player.heal(magic_dmg)
                print(bcolors.OKGREEN + "You have been healed by:", magic_dmg, "hp" + bcolors.ENDC)
        elif choice == 2:
            player.choose_item()
            item_choice = int(input("    Chose item:")) - 1

            if item_choice < 0 or item_choice >= len(player.items):
                continue

            item = player.items[item_choice]["item"]
            quantity = player.items[item_choice]["quantity"]

            if quantity == 0:
                print(bcolors.FAIL + "You don't have enough " + item.get_name() + "s" + bcolors.ENDC)
                continue

            player.items[item_choice]["quantity"] = quantity - 1

            if item.get_type() == "potion":
                player.heal(item.get_prop())
                print(bcolors.OKGREEN + item.get_name(), "healed you for:", item.get_prop(), "hp" + bcolors.ENDC)
            elif item.get_type() == "elixir":
                if item.get_name() == "Mega elixir":
                    for pl in players:
                        pl.heal(item.get_prop())
                        pl.restore_mp(item.get_prop())
                    print(bcolors.OKGREEN + item.get_name(), "restored party HP and MP" + bcolors.ENDC)
                else:
                    player.heal(item.get_prop())
                    player.restore_mp(item.get_prop())
                    print(bcolors.OKGREEN + item.get_name(), "restored your HP and MP" + bcolors.ENDC)
            elif item.get_type() == "attack":
                enemy_index = player.choose_target(enemies)
                enemies[enemy_index].take_damage(item.get_prop())
                print(bcolors.FAIL + item.get_name(), "dealt:", item.get_prop(),
                      "dmg to " + enemies[enemy_index].name + bcolors.ENDC)

    # Enemies turn
    for enemy in enemies:
        enemy_choice = 0
        target = random.randrange(0, 3)

        if enemy_choice == 0 and enemy.get_hp() > 0:
            enemy_dmg = enemy.generate_damage()
            players[target].take_damage(enemy_dmg)
            print(bcolors.FAIL + enemy.name.strip() + " attacked " + players[target].name + " for:", enemy_dmg,
                  "dmg" + bcolors.ENDC)

    print("------------------------------------")

    enemies_sum_hp = 1
    for enemy in enemies:
        enemies_sum_hp += enemy.get_hp()
    players_sum_hp = 1
    for player in players:
        players_sum_hp += player.get_hp()

    if enemies_sum_hp == 0:
        print("\n" + bcolors.OKGREEN + bcolors.BOLD + "You won!" + bcolors.ENDC)
        running = False
    elif players_sum_hp == 0:
        print("\n" + bcolors.FAIL + bcolors.BOLD + "You lost!" + bcolors.ENDC)
        running = False
