status_pirate_ship = list(map(int, input().split(">")))
status_warship = list(map(int, input().split(">")))
max_health = int(input())

command = input()

is_fight_over = False

while command != "Retire":
    text = command.split()
    action = text[0]
    if action == "Fire":
        index = int(text[1])
        damage = int(text[2])
        if 0 <= index < len(status_warship):
            status_warship[index] -= damage
            if status_warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                is_fight_over = True
                break
    elif action == "Defend":
        start_index = int(text[1])
        end_index = int(text[2])
        damage = int(text[3])
        if 0 <= start_index < len(status_pirate_ship) and 0 <= end_index < len(status_pirate_ship):
            for num in range(start_index, end_index + 1):
                status_pirate_ship[num] -= damage
            if min(status_pirate_ship) <= 0:
                print("You lost! The pirate ship has sunken.")
                is_fight_over = True
                break
    elif action == "Repair":
        index = int(text[1])
        health = int(text[2])
        if 0 <= index < len(status_pirate_ship):
            if status_pirate_ship[index] + health <= max_health:
                status_pirate_ship[index] += health
            else:
                status_pirate_ship[index] = max_health
    elif action == "Status":
        result = int(max_health * 0.2)
        count_list = [num for num in status_pirate_ship if num < result]
        print(f"{len(count_list)} sections need repair.")

    command = input()


if not is_fight_over:
    print(f"Pirate ship status: {sum(status_pirate_ship):.0f}")
    print(f"Warship status: {sum(status_warship):.0f}")
