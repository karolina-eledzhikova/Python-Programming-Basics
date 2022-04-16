hour = int(input())
day_of_week = input()
if 10 >hour < 18 or day_of_week == "Sunday":
    print("closed")
else:
    print("open")
