old_record = float(input())
distance = float(input())
time_per_meter = float(input())
delay = distance // 15 * 12.5 #ЗАбавянето ми е равно на целочисено на 15 умножено по 15. Тоест връща колко пъти го забавя и се умножава по 12.5
total_time = distance * time_per_meter + delay
if total_time < old_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    second_more =  total_time - old_record
    print(f"No, he failed! He was {second_more:.2f} seconds slower.")