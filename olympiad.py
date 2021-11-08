import re
from typing import Final

MAX_SCORE: Final = 100
scores = [0] * MAX_SCORE
quantity = [0] * MAX_SCORE
best_schools = [0] * MAX_SCORE
pattern = re.compile(r"^([А-ЯЁа-яё]+\s){2}\d{1,3}\s\d{1,3}$")
try:
    while True:
        string = input()
        if pattern.match(string) is None:
            print("ERROR!")
            exit(-1)
        school, score = map(int, string.rsplit(None, 2)[-2:])
        if school < 0 or school > MAX_SCORE:
            print("ERROR!")
            exit(-1)
        if score < 0 or score > MAX_SCORE:
            print("ERROR!")
            exit(-1)
        quantity[school] += 1
        scores[school] += score
except EOFError:
    pass
except ValueError:
    print("ERROR!")
    exit(-1)
max_element = quantity[1]
cardinality = 1
for i in range(2, len(quantity)):
    if max_element <= quantity[i]:
        if max_element == quantity[i]:
            best_schools[i] = scores[i]
            cardinality += 1
        else:
            best_schools = [0] * 101
            best_schools[i] = scores[i]
            cardinality = 1
            max_element = quantity[i]

while cardinality > 0:
    minimum = sum(best_schools) + 1
    index = 1
    for i in range(2, len(best_schools)):
        if best_schools[i] < minimum and best_schools[i] != 0:
            minimum = best_schools[i]
            index = i
    print(index, end=' ')
    cardinality -= 1
    best_schools[index] = 0
