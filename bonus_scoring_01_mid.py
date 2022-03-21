from math import ceil

students = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())

attendances = 0
max_bonus_points = 0

for num in range(1, students + 1):
    current_number = int(input())

    total_bonus = (current_number / number_of_lectures) * (5 + additional_bonus)
    if total_bonus > max_bonus_points:
        max_bonus_points = total_bonus
        attendances = current_number

print(f"Max Bonus: {ceil(max_bonus_points)}.")
print(f"The student has attended {attendances} lectures.")