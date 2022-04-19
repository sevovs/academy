price_cpu_in_usd = float(input())
price_gpu_in_usd = float(input())
price_for_one_ram_in_usd = float(input())
number_ram = int(input())
discount_percent = float(input())
price_cpu_in_bgn = price_cpu_in_usd * 1.57
price_gpu_in_bgn = price_gpu_in_usd * 1.57
price_for_ram_bgn = price_for_one_ram_in_usd * 1.57 * number_ram
price_cpu_in_bgn -= price_cpu_in_bgn * discount_percent
price_gpu_in_bgn -= price_gpu_in_bgn * discount_percent
total_sum = price_cpu_in_bgn + price_gpu_in_bgn + price_for_ram_bgn
print(f"Money needed - {total_sum:.2f} leva.")
