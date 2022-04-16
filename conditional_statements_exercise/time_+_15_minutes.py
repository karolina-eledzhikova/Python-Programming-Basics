hour = int(input())
minutes = int(input())
minutes += 15
#hour *= 60
#total_time = hour + minutes
hour += minutes // 60 #Към стойността на тази променлива добави това, което се намира от дясната страна на равенството
minutes %= 60 #(minutes = minutes % 60) А тук делим на модулно деление защото взима остатъка и се използва за минути

if hour > 23: #if hour == 24
    hour = 0  #hour -=24
if minutes <= 9:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")




