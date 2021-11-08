def amount(a, b):
    if a != 0:
        a = a - 1
        b = b + 1
        return amount(a, b)
    elif a == 0:
        return b


try:
    d = int(input())
    e = int(input())
    if d < 0:
        print("Ошибка! Неверный формат ввода!")
    elif e < 0:
        print("Ошибка! Неверный формат ввода!")
    else:
        print(amount(d, e))

except ValueError:
    print("Ошибка! Неверный формат ввода!")
