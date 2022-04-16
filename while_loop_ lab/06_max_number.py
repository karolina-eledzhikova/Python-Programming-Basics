import sys

max_number = sys.maxsize

while True:
    number = input()
    if number == 'Stop':
        break
    elif int(number) < max_number:
        max_number = int(number)
print(max_number)





i = 0
while i < 10:
    if i % 2 == 0:
        i += 1
        continue
    print(i)
i += 1








