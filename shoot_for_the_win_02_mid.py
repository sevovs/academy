info = list(map(int, input().split()))

command = input()
shots_target = 0

index_list = []


while command != "End":
    index = int(command)
    if index not in index_list and index < len(info):
        index_list.append(index)
        shots_target += 1
        temp = info[index]
        info[index] = -1
        for num in range(0, len(info)):
            if info[num] > temp and num not in index_list:
                info[num] -= temp
            elif info[num] <= temp and num not in index_list:
                info[num] += temp

    command = input()

copy_str = list(map(str, info))

print(f"Shot targets: {shots_target}", "->", " ".join(copy_str))