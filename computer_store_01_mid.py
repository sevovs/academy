price_no_taxes = 0

command = input()

while command != "regular" and command != "special":
    if float(command) < 0:
        print("Invalid price!")
        command = input()
        continue

    price_no_taxes += float(command)

    command = input()

taxes = price_no_taxes * 0.2
total_sum = price_no_taxes + taxes

if total_sum <= 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_no_taxes:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    if command == "special":
        total_sum *= 0.9

    print(f"Total price: {total_sum:.2f}$")