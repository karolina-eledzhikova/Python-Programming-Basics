product = input()
town = input()
quantity = float(input())
price = 0
if town == "Sofia":
    if product == "coffee":
        price = 0.50 * quantity
    elif product == "water":
        price = 0.80 * quantity
    elif product == "beer":
        price = 1.20 * quantity
    elif product == "sweets":
        price = 1.45 * quantity
    elif product == "peanuts":
        price = 1.60 * quantity
    print(price)
if town == "Plovdiv":
    if product == "coffee":
        price = 0.40 * quantity
    elif product == "water":
        price = 0.70 * quantity
    elif product == "beer":
        price = 1.15 * quantity
    elif product == "sweets":
        price = 1.30 * quantity
    elif product == "peanuts":
        price = 1.50 * quantity
    print(price)
if town == "Varna":
    if product == "coffee":
        price = 0.45 * quantity
    elif product == "water":
        price = 0.70 * quantity
    elif product == "beer":
        price = 1.10 * quantity
    elif product == "sweets":
        price = 1.35 * quantity
    elif product == "peanuts":
        price = 1.55 * quantity
    print(price)