# Пользователь вводит целое число N.
# Программа выводит N случайных чисел в промежутке [1; 10) (от 1 до 10, не включая 10).
# Далее пользователь решает, что он хочет сделать с этими числами. Для этого он вводит фразу из трех слов.

import random
from functools import reduce

n = int(input("Введите число: "))
lst = [random.randint(1, 10) for i in range(n)]
words = input("Введите необходимую операцию: ").split(" ")

sum = reduce(lambda a, x: a + x, lst)
multiply = reduce(lambda a, x: a * x, lst)
join = reduce(lambda a, b: 10 * a + b, lst)
union = reduce(lambda l, i: l if i in l else l+[i], lst, [])
reverse = reduce(lambda a, x: [x] + a, lst, [])
negated = list(map(lambda x: -x, lst))
inverted = list(map(lambda x: 1/x, lst))
squared = list(map(lambda x: x * x, lst))
odds = list(filter(lambda x: x % 2, lst))
evens = list(filter(lambda x: not x % 2, lst))
primes = list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))), lst))

my_dict = {"sum": sum, "multiply": multiply,
      "union": union, "reverse": reverse,
      "negated": negated, "inverted": inverted,
      "squared": squared, "odds": odds,
      "evens": evens, "primes": primes}

my_ls = []
for key, value in my_dict.items():
    for i in words:
        if i == key:
            my_ls.append(value)

