from calendar import c
import numbers
from random import randint as rand


def Write_field(list_field): # Отрисовка поля
    for i in list_field:
        print('\n')
        for j in i:
            print(j, end="\t",)
    print('\n')
def Check_winner(field): #
    flag_0 = False
    flag_x = False
    i = 0
    j = 0
    tamp_0 = '0'
    tamp_x = 'x'
    while (not flag_0 or not flag_x) and i < 3:
        count_0 = 0
        count_x = 0
        result = None
        while (not flag_0 or not flag_x) and j < 3:
            if field[i][j] == tamp_0:
                count_0 += 1
            elif field[i][j] == tamp_x:
                count_x += 1
            j += 1
        if count_0 == 3:
            flag_0 = True
            result = [flag_0, tamp_0]
            return result
        elif count_x == 3:
            flag_x = True
            result = [flag_x, tamp_x]
            return result
        i += 1
    while (not flag_0 or not flag_x) and i < 3:
        count_0 = 0
        count_x = 0
        result = None
        while (not flag_0 or not flag_x) and j < 3:
            if field[j][i] == tamp_0:
                count_0 += 1
            elif field[j][i] == tamp_x:
                count_x += 1
            j += 1
        if count_0 == 3:
            flag_0 = True
            result = [flag_0, tamp_0]
            return result
        elif count_x == 3:
            flag_x = True
            result = [flag_x, tamp_x]
            return result
        i += 1
    count_0 = 0
    count_x = 0
    while not flag_0 and i < 3:
        if field[i][i] == tamp_0:
            count_0 += 1
        elif field[i][i] == tamp_x:
            count_x += 1
        if count_0 == 3:
            result = [True, tamp_0]
            flag_0 = True
            return result
        elif count_x == 3:
            result = [True, tamp_x]
            flag_0 = True
            return result
        i += 1
    count_0 = 0
    count_x = 0
    i = 2
    while not flag_0 and i > -1:
        if field[i][i] == tamp_0:
            count_0 += 1
        elif field[i][i] == tamp_x:
            count_x += 1
        if count_0 == 3:
            result = [True, tamp_0]
            return result
        elif count_x == 3:
            result = [True, tamp_x]
            return result
        i -= 1
    return [False, ]
def Enter_number(field, count): #Заполнение
    number = None
    if count % 2 == 0:
        number = 'x'
    else:
        number = '0'
    print('\n')
    a = None
    b = None
    result = False
    while not result:
        a = int(input('Введите строчку: '))
        b = int(input('Введите столбец: '))
        if field[a - 1][b - 1] != '*':
            print('В этом поле уже есть значение, выберите другое')
        else:
            result = True
    field[a - 1][b - 1] = number
    return count + 1
win = False
random_number = rand(0, 1)
count = 0
if random_number == 0:
    count = 1
    print(f'Ходит {count}-й игрок')
else:
    count = 2
    print(f'Ходит {count}-й игрок')
field = ["*", "*", "*"], \
        ["*", "*", "*"], \
        ["*", "*", "*"]
Write_field(field)
while not win:
    if count % 2 == 0:
        print('Ходит второй игрок')
    else:
        print('Ходит первый игрок')
    count = Enter_number(field, count)
    Write_field(field)
    result = Check_winner(field)
    if result[0]:
        win = True
print('\n')
print(f'{result[1]} победил')

