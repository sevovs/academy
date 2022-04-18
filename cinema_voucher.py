voucher = int(input())
total_tickets = 0
total_other = 0
movie = 0
other_product = 0
command = input()
while command != "End":
    if len(command) > 8:
        first_char = command[0]
        second_char = command[1]
        total_tickets = ord(first_char) + ord(second_char)
        if total_tickets <= voucher:
            voucher -= total_tickets
            movie += 1
        else:
            break
    elif len(command) <= 8:
        first_char = command[0]
        total_other = ord(first_char)
        if total_other <= voucher:
            voucher -= total_other
            other_product += 1
        else:
            break
    command = input()
print(f"{movie}")
print(f"{other_product}")