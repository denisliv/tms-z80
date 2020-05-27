# Реализуйте декоратор log, который для каждого вызова функции выводит в консоль ее имя, аргументы и результат:

def concat(*args):
    for arg in args:
        yield from arg

def log(f):
    def wrapper(*args, **kwargs):
        r = f(*args, **kwargs)
        arg_str = ', '.join(concat(map(str, args), map(lambda x: f'{x[0]}={x[1]}', kwargs.items())))
        print(f'{f.__name__}({arg_str}) -> {r}')
        return r
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
