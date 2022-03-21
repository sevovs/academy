info = list(map(int, input().split()))

command = input()

while command != "end":
    text = command.split()
    word = text[0]

    if word == "swap":
        index1 = int(text[1])
        index2 = int(text[2])
        info[index1], info[index2] = info[index2], info[index1]
    elif word == "multiply":
        index1 = int(text[1])
        index2 = int(text[2])
        info[index1] = info[index1] * info[index2]
    elif word == "decrease":
        info = list(map(lambda x: x - 1, info))
    command = input()

copy_info = list(map(str, info))
print(", ".join(copy_info))
