
#  HOME WORK #3 Task #3

import re
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    #for t in phone_number:

        ptrn = r"[\d\+]+"
        t_cln= re.findall(ptrn,phone_number)
        t_cln_2="".join(t_cln)
        match len(t_cln_2):
            case 10 :
                t_fn = "+38"+t_cln_2
            case 11 :
                t_fn = "+3"+t_cln_2
            case 12 :
                t_fn = "+"+t_cln_2
            case 13 :
                t_fn = t_cln_2
            case _ :
                t_fn = "This is wrong ph_num"
        return t_fn
        #print(t_fn)

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
    

