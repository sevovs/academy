lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
gladiator_exp = 0
shield_counter = 0
for lost in range(1, lost_fight_count + 1):
    if lost % 2 == 0:
        gladiator_exp += helmet_price
    if lost % 3 == 0:
        gladiator_exp += sword_price
        if lost % 2 == 0:
            gladiator_exp += shield_price
            shield_counter += 1
            if shield_counter == 2:
                gladiator_exp += armor_price
                shield_counter = 0
print(f"Gladiator expenses: {gladiator_exp:.2f} aureus")
