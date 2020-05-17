# Пользователь непрерывно вводит числа. После каждой итерации выведите список тех чисел,
# которые пользователь ввел за последние 30 сек.

import time
x = []
while True:
    t = time.time()
    n = input("Введите число: ")
    # можно было написать:
    # if n == 'exit':
    #     break
    # x.append((n, t))
    # тогда бы не пришлось делать лишний pop
    x.append((n, t))
    if n == 'exit':
        x.pop()
        break

# выводить обновленный список нужно было сразу после того, как пользователь ввел число
# т.е. в цикле, а не в конце
y = [int(i[0]) for i in x if time.time() - i[1] <= 30]

print(f"Список введеных за последние 30 сек чисел: {y}")

