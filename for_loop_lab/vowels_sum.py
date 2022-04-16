text = input()
current_num = 0
total_sum = 0
for x in text:
    if x == 'a':
        current_num = 1
    elif x == 'e':
        current_num = 2
    elif x == 'i':
        current_num = 3
    elif x == 'o':
        current_num = 4
    elif x == 'u':
        current_num = 5
    else:
        current_num = 0
    total_sum += current_num
print(total_sum)


# tova e drug podoben varian za reshavane na tazi zadacha
text = input()
sum = 0
for x in range(1, len(text)):
    if text[x] == 'a':
        sum += 1
    if text[x] == 'e':
        sum += 2
    if text[x] == 'i':
        sum += 3
    if text[x] == 'o':
        sum += 4
    if text[x] == 'u':
        sum += 5
print(sum)


