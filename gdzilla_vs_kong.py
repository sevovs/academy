budget = float(input())
number_of_statists = int(input())
price_outfit_for_one_statists = float(input())
outfit = number_of_statists * price_outfit_for_one_statists
decor = budget * 0.1
if number_of_statists > 150:
    outfit -= outfit * 0.1
total_sum = outfit + decor
diff = abs(total_sum - budget)
if total_sum > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {diff:.2f} leva more.")
elif total_sum <= budget:
    print(f"Action!")
    print(f"Wingard starts filming with {diff:.2f} leva left.")