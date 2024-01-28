
#  HOME WORK #3 Task #1

from datetime import datetime

date = input('Date (yyyy-mm-dd): ')

def get_days_from_today(date):
    current_datetime = datetime.now()
    try:
        if 0<int(date[5:7])<13 and 0<int(date[8:9])<4 :
            user_date = datetime.strptime(date, "%Y-%m-%d")
            delta = current_datetime.toordinal() - user_date.toordinal()
            return abs(delta)
        else:
            print("Month is not in range 01-12 or//and day is in range 01-31")

    except :
        print('Invalid date or formate !')
    

print(get_days_from_today(date))
