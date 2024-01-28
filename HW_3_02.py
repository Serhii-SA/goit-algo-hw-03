
#  HOME WORK #3 Task # 2

import random
try:
    max=int(input("Please input end of a band (it must be int & max - 1000) ?"))
    min=int(input("Please input start of a band (it must be int & min - 1) ?"))
    quantity=int(input("Please input a quantity (any between = (end)-(start) )?"))
except:
    print("Invalid input")
    exit("Please,restart the program")
    
def get_numbers_ticket(min, max, quantity): 
    if 0<min<1001 and 0<max<1001 and quantity<=max-min :
        band = [x for x in range(min,max+1)  ]
        return sorted(random.sample(band,quantity))
    else:
        print("Incorrect input!")
        return []

lottery_numbers = get_numbers_ticket(min, max, quantity)
print("Ваші лотерейні числа:", lottery_numbers)



      
