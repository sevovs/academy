info = input().split(", ")
command = input()

while command != "Craft!":
    action = command.split(" - ")
    command = action[0]
    item = action[1]
    if command == "Collect":
        while item not in info:
            info.append(item)
    elif command == "Drop":
        while item in info:
            info.remove(item)
    elif command == "Combine Items":
        text = action[1].split(":")
        old_items = text[0]
        new_items = text[1]
        if old_items in info:
            index = info.index(old_items)
            info.insert(index + 1, new_items)
    elif command == "Renew":
        if item in info:
            index = info.index(item)
            info.pop(index)
            info.append(item)
    command = input()

print(", ".join(info))
