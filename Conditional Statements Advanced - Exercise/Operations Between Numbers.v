number_1 = int(input())
number_2 = int(input())
operator = input()
result = 0
form = ''
if operator == '+':
    result = number_1 + number_2
    if result % 2 == 0:
        form = 'even'
    else:
        form = 'odd'
    print(f"{number_1} {operator} {number_2} = {result} - {form}")
elif operator == '-':
    result = number_1 - number_2
    if result % 2 == 0:
        form = 'even'
    else:
        form = 'odd'
    print(f"{number_1} {operator} {number_2} = {result} - {form}")
elif operator == '*':
    result = number_1 * number_2
    if result % 2 == 0:
        form = 'even'
    else:
        form = 'odd'
    print(f"{number_1} {operator} {number_2} = {result} - {form}")

elif number_2 == 0 and operator == "/":
    print(f"Cannot divide {number_1} by zero")

elif operator == "/":
    result = number_1 / number_2
    print(f"{number_1} / {number_2} = {result:.2f}")

elif number_2 == 0 and operator == "%":
    print(f"Cannot divide {number_1} by zero")
elif operator == "%":
    result = number_1 % number_2
    print(f"{number_1} % {number_2} = {re