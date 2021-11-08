from typing import Final

MAX: Final = 8
ox = []
oy = []
for i in range(MAX):
    try:
        x, y = input().split()
        x = int(x)
        y = int(y)
        if x < 0 or x > MAX or y < 0 or y > MAX:
            print("Ошибка! Координаты должны быть в виде двух целых чисел от 1 до 8.")
            exit(-1)
    except ValueError:
        print("Ошибка! На вход ожидались два целых числа.")
        exit(-1)
    ox.append(x)
    oy.append(y)
checker = False
for i in range(MAX):
    for j in range(i + 1, MAX):
        if ox[i] == ox[j] or oy[i] == oy[j] or (abs(ox[i] - ox[j]) == abs(oy[i] - oy[j])):
            checker = True
if checker:
    print("YES")
else:
    print("NO")
