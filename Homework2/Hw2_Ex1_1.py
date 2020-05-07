# Пользователь вводит дату своего рождения в формате DD.MM.YYYY.
# Вывести название дня недели, в который родился пользователь.
import calendar as cd
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU')

bd = (input("Введите дату своего рождения в формате DD.MM.YYYY: ").split("."))
cd.setfirstweekday(cd.MONDAY)
print(f"Вы родились в: {cd.day_name[cd.weekday(int(bd[2]), int(bd[1]), int(bd[0]))]}")
