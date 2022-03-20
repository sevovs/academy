info = list(map(int, input().split("@")))

command = input()

last_position = 0
current_index_position = 0

while command != "Love!":
    text = command.split()
    action = text[0]
    index = int(text[1]) + current_index_position

    if index >= len(info):
        index = 0

    if -1 < index < len(info):
        if info[index] > 0:
            info[index] -= 2
            if info[index] == 0:
                print(f"Place {index} has Valentine's day.")
        else:
            print(f"Place {index} already had Valentine's day.")
    last_position = index
    current_index_position = index

    command = input()

result = [x for x in info if x == 0]
print(f"Cupid's last position was {last_position}.")

if len(result) != len(info):
    diff = abs(len(info) - len(result))
    print(f"Cupid has failed {diff} places.")
else:
    print("Mission was successful.")
