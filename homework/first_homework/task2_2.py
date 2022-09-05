a = []
a.append(int(input('Введите Х - ')))
a.append(int(input('Введите Y - ')))
if a[0] == 0 or a[1] == 0:
    print('Координаты не могут ровняться нулю')
else:
    if a[0] > 0 and a[1] > 0:
        print('1 четверть')
    elif a[0] < 0 and a[1] > 0:
        print('2 четверть')
    elif a[0] < 0 and a[1] < 0:
        print('3 четверть')
    elif a[0] > 0 and a[1] < 0:
        print('4 четверть')
    else:
        print('Ошибка ввода')

