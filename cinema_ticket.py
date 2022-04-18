student_tickets = 0
standard_tickets = 0
kids_tickets = 0
total_tickets = 0
command = input()
while command != "Finish":
    movie = command
    free_spaces = int(input())
    total_spaces = free_spaces
    sold_tickets = 0
    while total_spaces > 0:
        tickets = input()
        if tickets == "End":
            break
        if tickets == "student":
            student_tickets += 1
        elif tickets == "standard":
            standard_tickets += 1
        elif tickets == "kid":
            kids_tickets += 1
        total_spaces -= 1
        sold_tickets += 1
        total_tickets += 1
    print(f"{movie} - {sold_tickets / free_spaces * 100:.2f}% full.")
    command = input()
print(f"Total tickets: {total_tickets:.2f}")
print(f"{student_tickets / total_tickets * 100:.2f}% student tickets.")
print(f"{standard_tickets / total_tickets * 100:.2f}% standard tickets.")
print(f"{kids_tickets / total_tickets * 100:.2f}% kids tickets.")