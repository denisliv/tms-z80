# Пользователь вводит список из чисел. Найдите число, которое встречается чаще других.
import collections

c = collections.Counter()

x = input("Введите список из чисел через пробел: ").split()
for i in x:
    c[i] += 1
lst = c.most_common(1)
for i in lst:
    print(f'Наиболее часто встречается число {i[0]} - {i[1]} раз')
