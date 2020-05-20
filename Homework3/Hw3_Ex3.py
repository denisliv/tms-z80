# Пользователь непрерывно вводит числа. После каждой итерации выведите список тех чисел,
# которые пользователь ввел за последние 30 сек.
from collections import deque
import time

values = deque()
while True:
    n = int(input("Введите число: "))
    t = int(1000 * time.time())
    values.append((n, t))
    while len(values):
        value = values[0]
        if t - value[1] < 5000:
            break
        values.popleft()
    print(list(map(lambda x: x[0], values)))
