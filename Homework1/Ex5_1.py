# Пользователь вводит математическое выражение, состоящее только из положительных чисел и операторов +, -,
# * и /. Посчитайте результат этого выражения.
x = input("Введите математическое выражение, разделяя символы пробелом: ").split(" ")
a = []
b = ''
for i in x:
    if i.isnumeric():  # не могу придумать, как провериь строку на число с плавающей точкой,
        # чтобы использовать и дробные числа
        a.append(int(i))
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
