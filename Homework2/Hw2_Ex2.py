# Пользователь вводит 3 числа. Определить, существует ли треугольник с такими сторонами,
# и если существует, найти его углы. Для решения задачи можно использовать теорему косинусов.

from math import acos, degrees

x = input("Введите три числа через пробел: ").split(" ")
# ты каждый раз выполняешь преобразование str в int, хотя мог бы сделать это один раз заранее, например:
# a, b, c = map(int, input(...).split())
if int(x[0]) + int(x[1]) > int(x[2]) and int(x[1]) + int(x[2]) > int(x[0]) and int(x[0]) + int(x[2]) > int(x[1]):
    y_1 = round(degrees(acos((int(x[0])**2 + int(x[1])**2 - int(x[2])**2) / (2 * int(x[0]) * int(x[1])))), 2)
    y_2 = round(degrees(acos((int(x[1])**2 + int(x[2])**2 - int(x[0])**2) / (2 * int(x[1]) * int(x[2])))), 2)
    y_3 = round(degrees(acos((int(x[2])**2 + int(x[0])**2 - int(x[1])**2) / (2 * int(x[2]) * int(x[0])))), 2)
    print(f"Треугольник существует, его углы равны {y_1}, {y_2}, {y_3} градуса")
else:
    print("Треугольника не существует")
