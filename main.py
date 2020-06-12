from classes.game import Person, bcolors

magic = [{"name": "Fire ball", "cost": 10, "dmg": 60},
         {"name": "Thunder", "cost": 15, "dmg": 80},
         {"name": "Blizzard", "cost": 12, "dmg": 68}]

player = Person(500, 100, 60, 45, magic)
enemy = Person(200, 40, 35, 24, magic)

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
        print("You attacked for:", dmg, "  Enemy HP:", enemy.get_hp())
    elif index == 1:
        player.choose_spell()
        spell_choice = input("Chose spell:")
        spell_index = int(spell_choice) - 1

        if player.get_mp() < player.get_spell_cost(spell_index):
            print(bcolors.FAIL + "You don't have enough magic points for this spell" + bcolors.ENDC)
            continue

        magic_dmg = player.generate_spell_damage(spell_index)
        player.reduce_mp(player.get_spell_cost(spell_index))
        enemy.take_damage(magic_dmg)
        print("You attacked for:", magic_dmg, "  You have", player.get_mp(),
              "magic points left", "  Enemy HP:", enemy.get_hp())

    enemy_choice = 0

    if enemy_choice == 0 and enemy.get_hp() > 0:
        dmg = enemy.generate_damage()
        player.take_damage(dmg)
        print("Enemy attacked for:", dmg, "  Your HP:", player.get_hp())

    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + bcolors.BOLD + "You won!" + bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(bcolors.FAIL + bcolors.BOLD + "You lost!" + bcolors.ENDC)
        running = False
