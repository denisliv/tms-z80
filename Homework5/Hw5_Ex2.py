# Реализуйте декоратор log, который для каждого вызова функции выводит в консоль ее имя, аргументы и результат:

def log(f):
    def wrapper(*args, **kwargs):
        print(f.__name__, args, sep='')
        value = f(*args, **kwargs)
        print(f'Результат {value}')
    return wrapper

@log
def a(x):
    return -x

@log
def b(x, y):
    return x * y


@log
def c(x, y, *args):
    result = x + y
    for arg in args:
        result += arg
    return result

a(1)
b(1, 2)
c(1, 2, 3)
