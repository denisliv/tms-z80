# Пользователь вводит математическое выражение, состоящее только из положительных чисел и операторов +, -,
# * и /. Посчитайте результат этого выражения.


def is_numeric(value):  # определение, является ли строка числом (включая положительные, орицательные и дробные)
    try:
        float(value)
        return True
    except ValueError:
        return False


print("Введите n для выхода из программы")
while True:
    x = input("Введите математическое выражение, разделяя символы пробелом: ").split(" ")
    if x[0] == 'n':
        print("До свидания!")
        break
    a = []
    b = ''
    for i in x:
        if is_numeric(i):
            a.append(float(i))
        else:
            b = i
    for i in range(len(a) - 1):
        if b == "+":
            y = a[i] + a[i + 1]
            print(f"{a[i]} {b} {a[i + 1]} = {y}")
        elif b == "-":
            y = a[i] - a[i + 1]
            print(f"{a[i]} {b} {a[i + 1]} = {y}")
        elif b == "*":
            y = a[i] * a[i + 1]
            print(f"{a[i]} {b} {a[i + 1]} = {y}")
        elif b == "/":
            if a[i + 1] == 0:
                print("Деление на 0 запрещено")
            else:
                y = a[i] / a[i + 1]
                print(f"{a[i]} {b} {a[i + 1]} = {y}")
        else:
            print(f"{b} неверный знак")
