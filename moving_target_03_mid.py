info = [int(x) for x in input().split()]

command = input()

while command != "End":
    text = command.split()
    action = text[0]
    index = int(text[1])

    if action == "Shoot":
        power = int(text[2])
        if 0 <= index < len(info):
            info[index] -= power
            if info[index] <= 0:
                info.remove(info[index])

    elif action == "Add":
        value = int(text[2])
        if 0 <= index < len(info):
            info.insert(index, value)
        else:
            print("Invalid placement!")

    elif action == "Strike":
        radius = int(text[2])
        if 0 <= index - radius and index + radius < len(info):
            info = info[:index - radius] + info[index + radius + 1:]
        else:
            print("Strike missed!")

    command = input()

output = list(map(str, info))

print("|".join(output))
