budget = float(input())
video_cards_num = int(input())
processor = int(input())
ram_memory = int(input())

video_cards_price = video_cards_num*250
processor_price = 0.35*video_cards_price
sum_processor = processor*processor_price
ram_memory_price = 0.1*video_cards_price
sum_ram_memory = ram_memory*ram_memory_price
total_sum = video_cards_price+sum_processor+sum_ram_memory
discount = 0
if video_cards_num > processor:
    discount = total_sum * 0.85
if total_sum <= budget:
    remaining_money = budget-discount
    print(f"You have {remaining_money:.2f} leva left!")
if total_sum > budget:
    needet_sum = discount - budget
    print(f"Not enough money! You need {needet_sum:.2f} leva more!")
