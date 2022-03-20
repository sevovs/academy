people = int(input())
wagons = input().split()

copy_wagons = list(map(int, wagons))

total_space = (len(copy_wagons) * 4) - sum(copy_wagons)

for num in range(len(copy_wagons)):
    if total_space == 0 or people == 0:
        break
    else:
        if copy_wagons[num] >= 4:
            pass
        elif copy_wagons[num] < 4 and people >= 4:
            temp = (4 - copy_wagons[num])
            people -= temp
            total_space -= temp
            copy_wagons[num] += temp
        elif copy_wagons[num] < 4 and people < 4:
            copy_wagons[num] += people
            total_space -= people
            people -= people

copy_wagons_str = list(map(str, copy_wagons))

if total_space == 0 or people == 0:
    if total_space > people == 0:
        print("The lift has empty spots!")
    if people > total_space == 0:
        print(f"There isn't enough space! {people} people in a queue!")

print(" ".join(copy_wagons_str))

