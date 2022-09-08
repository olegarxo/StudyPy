import random

rand = random.Random()
dic_bush = {}
count = int(input('Введите количество кустов - '))
max_bush = 2
max_count = dic_bush[max_bush] + dic_bush[max_bush - 1] + dic_bush[max_bush + 1]
tamp_count = 0
for i in range(count):
    dic_bush[i + 1] = rand.randint(0, 1001)
for i in range(count):
    if i <= count - 2:
        if tamp_count >  dic_bush[i + 3] + dic_bush[i + 2] + dic_bush[i + 4]:
            max_bush = dic_bush[i + 3]
    elif i == count - 1:


