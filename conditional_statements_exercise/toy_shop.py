price_for_excursion = float(input())
puzzle = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())
# Променливи
discount = 0
rent = 0
profit = 0
# цени за играчки
puzzle_price = 2.60
dolls_price = 3
teddy_bears_price = 4.10
minions_price = 8.20
trucks_price = 2
# Обща цена
total_price = puzzle*puzzle_price + dolls*dolls_price + teddy_bears*teddy_bears_price+ minions*minions_price + trucks*trucks_price
orders = puzzle+dolls+teddy_bears+minions+trucks
if orders >= 50:
    discount = 0.25*total_price
final_price = total_price-discount
rent = 0.1*final_price
profit = final_price - rent
if profit > price_for_excursion:
    remaining_money = profit - price_for_excursion
    print(f"Yes! {remaining_money:.2f} lv left.")
else:
    lack_of_money = price_for_excursion - profit
    print(f"Not enough money! {lack_of_money:.2f} lv needed.")
