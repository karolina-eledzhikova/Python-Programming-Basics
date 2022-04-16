first_time = int(input())
second_time = int(input())
third_time = int(input())
total_time = first_time+second_time + third_time
minutes = total_time // 60
#1min = 60s
#500s//60 = 8 + x sec
second = total_time % 60
# Взима се % защото взема остатъка тоест това са секундите
if second < 10: # 1. 2. 3. 4.
    print(f"{minutes}:0{second}")
else: #elif second >= 10
    print(f"{minutes}:{second}")




