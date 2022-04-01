def factorial(num):
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)


number = int(input())
number2 = int(input())

result = factorial(number) / factorial(number2)

print(f"{result:.2f}")