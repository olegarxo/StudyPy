from random import randint as rand
snack = 300
random_number = rand(0, 1)
count = 0
if random_number == 0:
    count = 1
else:
    count = 2
def Bot(snack):
    if snack // 28 > 1:
        snack = rand(10, 29)
    elif 0 < snack < 29:
        snack = snack
    elif snack < 100:
        snack = rand(5, 12)
    else:
        snack = snack % 28
    return snack
def Game(snack, count):
    if count % 2 == 0:
        print('Ходит бот')
        snack = Bot(snack)
        return  snack
    else:
        print('Ходит первый игрок')
        flag = False
        while not flag:
            count = int(input('Сколько печений хотите взять: '))
            if count > 28 or count < 0:
                print('Многовато')
            else:
                flag = True
        return count

while snack != 0:
    tamp = Game(snack, count)
    print(f'{tamp} печенек взяли')
    snack = snack - tamp
    print(f'{snack} печенек осталось')
    if snack == 0:
        if count % 2 == 0:
            print('Победил бот')
        else:
            print('Победил игрок')
    count += 1