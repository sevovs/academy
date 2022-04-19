budget = int(input())
price = 0
command = input()
target_reached = False
while command != "closed":
    if command == "haircut":
        order = input()
        if order == "mens":
            price += 15
        elif order == "ladies":
            price += 20
        elif order == "kids":
            price += 10
    elif command == "color":
        order = input()
        if order == "touch up":
            price += 20
        elif order == "full color":
            price += 30
    if price >= budget:
        target_reached = True
        print(f"You have reached your target for the day!" )
        break
    command = input()
if not target_reached:
    diff = abs(budget - price)
    print(f"Target not reached! You need {diff}lv. more.")
print(f"Earned money: {price}lv.")