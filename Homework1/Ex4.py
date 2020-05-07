# Пользователь вводит x и N. Посчитайте приблизительное значение cos(x) с точностью до N-ого члена его разложения

from math import factorial, cos, pi


def term(x, i):
    p = 2 * i
    y = x ** p / factorial(p)
    if i % 2 == 0:
        return y
    else:
        return -y


x = pi * (float(input("Введите число: "))) / 100
n = int(input("Введите N-ый член для разложения: "))
result = 0
for i in range(n):
    result += term(x, i)
print(f"Значение разложения cos({x}) до {n}-ого члена равно {result}")
print(cos(x))
