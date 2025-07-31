import random

def main():
    player_hp = 100
    enemy_hp = 100

    print("Welcome to the simple RPG!")
    while player_hp > 0 and enemy_hp > 0:
        print(f"Your HP: {player_hp} | Enemy HP: {enemy_hp}")
        print("1. Attack")
        print("2. Heal")
        choice = input("Choose an action: ")

        if choice == "1":
            damage = random.randint(10, 20)
            enemy_hp -= damage
            print(f"You hit the enemy for {damage} HP!")
        elif choice == "2":
            heal = random.randint(5, 15)
            heal2 = random.randint(5, 15)
            player_hp += heal
            enemy_hp += heal2
            print(f"You heal yourself for {heal} HP.")
        else:
            print("Invalid choice. Try again.")
            continue

        if enemy_hp > 0:
            enemy_damage = random.randint(5, 15)
            player_hp -= enemy_damage
            print(f"Enemy hits you for {enemy_damage} HP!")
        print()

    if player_hp > 0:
        print("You defeated the enemy!")
    else:
        print("You were defeated...")

if __name__ == "__main__":
    main()
