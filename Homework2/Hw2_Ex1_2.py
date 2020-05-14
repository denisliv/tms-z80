# Пользователь вводит название дня недели.
# Вывести ближайший месяц и год, когда этот день недели выпадал на 1-ое число.
import calendar as cd
from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU')

x = input("Введите день недели: ").lower()
d = list(cd.day_name).index(x)
now = datetime.now()
month = now.month
year = now.year
while True:
    day = cd.weekday(year, month, 1)
    if day == d:
        print(f'{x} выпадал на 1 число в {month} месяце {year} года')
        break
    else:
        month -= 1
        if month == 0:
            year -= 1
            month = 12
