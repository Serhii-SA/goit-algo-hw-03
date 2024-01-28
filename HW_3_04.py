
#  HOME WORK #3 Task #4

import datetime 
from datetime import timedelta

users = [
    {"name": "Рома до 7 у робоч.дн", "birthday": "1985.01.29"},
    {"name": "Яна більше 7 дн", "birthday": "1990.02.15"},
    {"name": "Іван  до 7 у сб ", "birthday": "1990.02.03"},
    {"name": "Дмитро до 7 у  нд", "birthday": "1990.02.04"},
    {"name": "Богдана вже було", "birthday": "1990.01.01"}
]

def get_upcoming_birthdays(users):
    dt_tday=datetime.datetime.today().date()  #сьог.дата
    prg_out = [] # порожн.список в який засунемо вихідні словники  (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата'). 
    
    for user in users:
        crnt_us_nm = user.get('name') # присвоили перем текущ имя клиента

        user_brday = datetime.datetime.strptime(user["birthday"], "%Y.%m.%d").date() #зі словника витягає ДР клієнта та робить об.дататайм
        user_brday_crn_year=user_brday.replace(year=dt_tday.year) # замінюєм рік в ДР на поточн.
        delta = user_brday_crn_year.toordinal()-dt_tday.toordinal() # визначаємо різницю в дн.між ДР та поточн.датою знак(-) -ДР вже був
        if 0<= delta < 8 : # якщо ДР клієнта в найближчі 7днів
            week_d = user_brday_crn_year.weekday() # визначаємо день тижня
            if 0<= week_d<5 : # якщо ДР у робочий день
                cr_dic_conday ={'name': crnt_us_nm, 'congratulation_date': user_brday_crn_year.strftime("%Y.%m.%d")}
                #prg_out.append(cr_dic_conday)
            elif week_d==5: # якщо ДР у сб
                us_bdsd_repl = user_brday_crn_year + timedelta(days=2)
                cr_dic_conday ={'name': crnt_us_nm, 'congratulation_date': us_bdsd_repl.strftime("%Y.%m.%d")}
                #prg_out.append(cr_dic_conday)
            else: # решта тоді ДР у нд
                us_bdsd_repl = user_brday_crn_year + timedelta(days=1)
                cr_dic_conday ={'name': crnt_us_nm, 'congratulation_date': us_bdsd_repl.strftime("%Y.%m.%d")}
            prg_out.append(cr_dic_conday)
        elif delta < 0: # якщо ДР вже минув
            us_bdsd_repl = user_brday_crn_year.replace(year=dt_tday.year+1) # додаємо 1рік до дня привітання
            cr_dic_conday ={'name': crnt_us_nm, 'congratulation_date': us_bdsd_repl.strftime("%Y.%m.%d")}
            prg_out.append(cr_dic_conday)
    return prg_out
        
upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
       
        







    


