info = [x for x in input().split()]

command = input()
moves = 0

is_game_over = False

while command != "end":
    text = command.split()
    index1 = int(text[0])
    index2 = int(text[1])
    moves += 1
    if index1 == index2 or index1 < 0 or index1 >= len(info) or index2 < 0 or index2 >= len(info):
        middle = len(info) // 2
        info.insert(middle, f"-{moves}a")
        info.insert(middle, f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")
    elif info[index1] == info[index2]:
        print(f"Congrats! You have found matching elements - {info[index1]}!")
        x = info[index1]
        while x in info:
            info.remove(x)
    elif info[index1] != info[index2]:
        print("Try again!")
    if len(info) == 0:
        print(f"You have won in {moves} turns!")
        is_game_over = True
        break
    command = input()

if not is_game_over:
    print("Sorry you lose :(\n"
          f"{' '.join(info)}")
