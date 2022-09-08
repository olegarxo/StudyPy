import random
rand = random.Random()
n = rand.randint(1, 101)
table = [] # Только если нужно ваывести список монеток
count_zero = 0
count_one = 0
for i in range(n):
    tamp = rand.randint(0, 2)
    table.append(tamp)
    if table[i] == 0:
        count_zero += 1
    else:
        count_one += 1
print(f'Получилось {count_zero} нулей и {count_one} едениц')
if count_zero > count_one:
    print(f'Нужно перевернуть {count_one} едениц')
elif count_zero < count_one:
    print(f'Нужно перевернуть {count_zero} нулей')
else:
    print('УХ ТЫ, они равны')
    print(f'Нужно перевернуть {count_zero} нулей или {count_one} едениц')





