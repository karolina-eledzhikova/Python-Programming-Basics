budget = float(input())
number_of_statist = int(input())
one_dress_price = float(input())
decor = budget * 0.1
dresses_price = number_of_statist*one_dress_price
if number_of_statist > 150:
    dresses_price *= 0.9 #dresses_price = dresses_price * 0.9 (Вземи стойността на дрехите и ги умножи по 0,9, или вземи 90% от отстъпката. (100-10=90)
needed_money = decor + dresses_price
difference = abs(needed_money-budget)
if needed_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")