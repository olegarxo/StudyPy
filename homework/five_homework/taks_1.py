from random import randint as rand
snack = 2021
random_number = rand(0, 1)
count = 0
if random_number == 0:
    count = 1
else:
    count = 2
def Bot(snack):
    count = 0
    if snack // 28 > 1:
        snack = rand(10,29)
        return snack
def Game(snack, count):
    if count % 2 == 0:
        print('Ходит второй игрок')
    else:
        print('Ходит первый игрок')
    flag = False
    while not flag:
        count = int(input('Сколько печений хотите взять: '))
        if count > 29 or count < 0:
            print('Многовато')
        else:
            flag = True
    snack = snack - count
    return snack

while snack != 0:
    snack = Game(snack, count)
    print(snack)
    count += 1