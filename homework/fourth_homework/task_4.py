import random
num = [1, 'x']
flag = True
enter_num = int(input('Введите коэффециент: '))
f = open('function.txt','a')
while flag:
    rand = random.randint(0, 101)
    if enter_num == 0:
        if rand == 0:
            f.write('')
        else:
            f.write(f'{rand}')
            enter_num -= 1
    elif enter_num == -1:
        f.write(' = 0\n')
        flag = False
    else:
        if rand == 0:
            f.write('')
        else:
            if enter_num == 1:
                f.write(f'{rand}x + ')
                enter_num -= 1
            else:
                f.write(f'{rand}x^{enter_num} + ')
                enter_num -= 1
f.close()
