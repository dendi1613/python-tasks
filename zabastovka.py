try:
    days, duma = map(int, input().split())
    years = [0] * days
    mas = []
    for i in range(duma):
        mas.append(list(map(int, input().split())))
except ValueError:
    print("Ошибка! Неверный формат ввода!")
    exit(-1)
for i in range(duma):
    x = mas[i][0]
    while x <= days:
        years[x - 1] = 1
        x += mas[i][1]

if days >= 6:
    n = 5
    while n < days:
        years[n] = 0
        n += 7
if days >= 7:
    n = 6
    while n < days:
        years[n] = 0
        n += 7
print(sum(years))
