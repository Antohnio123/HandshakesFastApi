# Написать функцию для подсчета количества рабочих дней между двумя датами, удалив все выходные,
# без учёта праздников (даты передаются в качестве параметров)
import time
print ("\n Задача 1.")
try:
    d1 = input("Введите первую дату в формате дд.мм.гггг:  ")
    d1 = time.strptime(d1, "%d.%m.%Y")
    d2 = input("Введите вторую дату в формате дд.мм.гггг:  ")
    d2 = time.strptime(d2, "%d.%m.%Y")
    # print(str(d2))                                            # проверяем правильность перевода даты
except ValueError:
    print("Вы ввели ошибочные данные, программа выключается")
    exit()
d1 = time.mktime(d1)
d2 = time.mktime(d2)
Max = max(d1,d2)
Min = min(d1,d2)
deltadays = (Max - Min)/86400     # дней между датами
deltaweeks = int(deltadays//7*5)                     # находим количество целых недель и умножаем на 5 - число раб. дней в целых неделях

# Находим разницу в рабочих днях на неполной неделе ***********************************************************
MaxW=time.localtime(Max)[6]               # переводим макс. и мин. даты в формат struct_time, находим день недели максимума и минимума.
MinW=time.localtime(Min)[6]                 # день недели минимума может быть больше дня недели максимума
a=0                             # дней от меньшей даты до конца её недели
minidelta = 0
if MinW < 5:
    a = 5 - MinW

if MaxW ==6:
    minidelta = a
elif MaxW == 5:
    if MinW == 6:
        minidelta = 5
    else:
        minidelta = a
elif MaxW<5:
    if MinW<MaxW:
        minidelta = MaxW - MinW + 1
    else:
        minidelta = MaxW + 1 + a
else:
    print("Выпал непредвиденный случай: MinW = " +str(MinW) + ", MaxW = " + str(MaxW))

Rab=deltaweeks+minidelta
# print("MinW = " + str(MinW) + ", MaxW = " + str(MaxW))
# print ("Количество рабочих дней в целых неделях между датами = " + str(deltaweeks))
# print ("Количество рабочих дней в неполной неделе = "+ str(minidelta))
print ("Ответ: Количество рабочих дней между датами (учитывая обе эти даты) = "+ str(Rab))

# *********************************************************************************************
print ("\n Задача 2.")
