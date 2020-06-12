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
        choice = input("Chose action")
        index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for:", dmg, "  Enemy HP:", enemy.get_hp())

    enemy_choice = 0

    if enemy_choice == 0:
        dmg = enemy.generate_damage()
        player.take_damage(dmg)
        print("Enemy attacked for:", dmg, "  Your HP:", player.get_hp())

    # running = False
