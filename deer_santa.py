from math import floor, ceil

number_of_days = int(input())
left_food_kg = int(input())
first_deer_food_kg = float(input())
second_deer_food_kg = float(input())
third_deer_food_kg = float(input())
total_needed_food = first_deer_food_kg * number_of_days + second_deer_food_kg * number_of_days \
                    + third_deer_food_kg * number_of_days
diff = abs(left_food_kg - total_needed_food)
if left_food_kg >= total_needed_food:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
