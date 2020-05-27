# Реализуйте декоратор multiply, который перемножает все аргументы перед вызовом функции:
from functools import reduce


def multiply(f):
    def wrapper(*args):
        return f(reduce(lambda x, y: x * y, args))
    return wrapper


numbers = list(map(int, input("Введите цифры через пробел: ").split()))


@multiply
def func(x):
    print(x)


func(*numbers)
