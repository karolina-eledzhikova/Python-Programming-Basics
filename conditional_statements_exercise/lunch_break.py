
from math import ceil
name_serial = input()
time_episode = int(input())
time_rest = int(input())

time_to_lunch = time_rest * 1/8
time_to_relax = time_rest * 1/4
difference = time_rest - time_to_lunch - time_to_relax
difference_time = abs(time_episode - difference)
# Ако времето е достатъчно да изгледате епизода:
# "You have enough time to watch {име на сериал} and left with {останало време} minutes free time."
if difference >= time_episode:
    print(f"You have enough time to watch {name_serial} and left with {ceil(difference_time)} minutes free time.")

# Ако времето не Ви е достатъчно:
# "You don't have enough time to watch {име на сериал}, you need {нужно време} more minutes."
else:
    print(f"You don't have enough time to watch {name_serial}, you need {ceil(difference_time)} more minutes.")
