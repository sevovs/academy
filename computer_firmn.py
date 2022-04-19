number_of_computers = int(input())
p1 = 0
possible_sells = 0
average = 0
rating = 0
for num in range(1, number_of_computers + 1):
    number = int(input())
    p1 += number % 10
    rating = number % 10
    if rating == 2:
        possible_sells += (number // 10) * 0
    elif rating == 3:
        possible_sells += (number // 10) * 0.5
    elif rating == 4:
        possible_sells += (number // 10) * 0.7
    elif rating == 5:
        possible_sells += (number // 10) * 0.85
    elif rating == 6:
        possible_sells += (number // 10)
average = p1 / number_of_computers
print(f"{possible_sells:.2f}")
print(f"{average:.2f}")
