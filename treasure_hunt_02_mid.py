info = input().split("|")

command = input()

while command != "Yohoho!":
    text = command.split()
    action = text[0]

    if action == "Loot":
        item = 0
        for i in range(1, len(text)):
            if text[i] not in info:
                info.insert(0, text[i])
    elif action == "Drop":
        index = int(text[1])
        if index > len(info):
            pass
        else:
            item = info[index]
            info.pop(index)
            info.append(item)
    elif action == "Steal":
        stolen_items = []
        count = int(text[1])
        if count > len(info):
            stolen_items.extend(info)
            info.clear()
        else:
            for i in range(count):
                stolen_items.insert(0, info[-1])
                info.pop(-1)
        print(", ".join(stolen_items))
    command = input()

new_list = []

for word in info:
    for ch in word:
        new_list.append(ch)

if len(info) == 0:
    print("Failed treasure hunt.")
else:
    average = len(new_list) / len(info)
    print(f"Average treasure gain: {average:.2f} pirate credits.")
