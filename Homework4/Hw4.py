# Пользователь вводит целое число N.
# Программа выводит N случайных чисел в промежутке [1; 10) (от 1 до 10, не включая 10).
# Далее пользователь решает, что он хочет сделать с этими числами. Для этого он вводит фразу из трех слов.

import random
from functools import reduce

n = int(input("Введите число: "))
lst = [random.randint(1, 10) for i in range(n)]
words = input("Введите необходимую операцию: ").split(" ")


def my_filter_f(lst):
    odds = list(filter(lambda x: x % 2, lst))
    evens = list(filter(lambda x: not x % 2, lst))
    primes = list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))), lst))
    my_dict_filter = {"odds": odds, "evens": evens, "primes": primes}
    my_filter = [v for k, v in my_dict_filter.items() if k in words]
    return my_filter


def my_map_f(my_filter):
    negated = list(map(lambda x: -x, my_filter))
    inverted = list(map(lambda x: 1/x, my_filter))
    squared = list(map(lambda x: x * x, my_filter))
    my_dict_map = {"negated": negated, "inverted": inverted, "squared": squared}
    my_map = [v for k, v in my_dict_map.items() if k in words]
    return my_map


def my_reduce(my_map):
    sum = reduce(lambda a, x: a + x, my_map)
    multiply = reduce(lambda a, x: a * x, my_map)
    join = reduce(lambda a, b: str(a) + str(b), my_map)
    union = reduce(lambda l, i: l if i in l else l+[i], my_map, [])
    reverse = reduce(lambda a, x: [x] + a, my_map, [])
    my_dict_reduce = {"sum": sum, "multiply": multiply, "join": join, "union": union, "reverse": reverse}
    result = [v for k, v in my_dict_reduce.items() if k in words]
    return result


my_filter = my_filter_f(lst)
my_map = my_map_f(my_filter[0])
result = my_reduce(my_map[0])

print(*result, sep=", ")


