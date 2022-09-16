from calendar import c
import numbers
from random import randint as rand


def Write_field(list_field):
    for i in list_field:
        print('\n')
        for j in i:
            print(j, end= "\t")
def Check_winner(field, win):
    win = False
    tamp = field[i][j]
    for i in range(0, 3):
        for j in range(0, 3):
            if field[i][j] == tamp:
                win = True
                return tamp, win
            else:
                win = False
                return tamp, win
    for i in range(0, 3):
        for j in range(0, 3):
            if field[j][i] == tamp:
                win = True
                return tamp, win
            else:
                win = False
                return tamp, win
    for i in range(0, 3):
        if field[i][i] == tamp:
                win = True
                return tamp, win
        else:
            win = False
            return tamp, win
    for i in range(2, -1, -1):
        if field[i][i] == tamp:
                win = True
                return tamp, 
        else:
            win = False
            return tamp, win
def Enter_number(field, count):
    number = None
    if count % 2 == 0:
        number = 'x'
    else: number = '0'
    print('\n')
    a = int(input('Введите строчку: '))
    b = int(input('Введите столбец: '))
    field[a][b] = number
    return count + 1
win = False
random_number = rand(0,1)
count = 0
if random_number == 0: count = 1 
else: count = 2
field = ["*","*","*"], ["*","*","*"], ["*","*","*"]

while not win:
    Write_field(field)
    Enter_number(field, count)
    Write_field(field)
    Check_winner(field, win)


