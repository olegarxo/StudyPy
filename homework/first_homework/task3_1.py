from random import randint
b = int(randint(1,30))
a = int(input('Введите четверть'))
if a == 1:
    print(f'Диапазон чисел X от 0 до {b}')
    print('А именоо: ')
    for i in range(b):
        print(i, end=' ')
    print()
    print(f'Диапазон чисел Y от 0 до {b}')
    print('А именоо: ')
    for i in range(b):
        print(i, end=' ')
elif a == 2:
    print(f'Диапазон чисел X от 0 до {-b}')
    print('А именоо: ')
    for i in range(b,-1,-1):
        print(-i, end=' ')
    print()
    print(f'Диапазон чисел Y от 0 до {b}')
    print('А именоо: ')
    for i in range(b + 1):
        print(i, end=' ')
elif a == 3:
    print(f'Диапазон чисел X от 0 до {b}')
    print('А именоо: ')
    for i in range(b,-1,-1):
        print(-i, end=' ')
    print()
    print(f'Диапазон чисел Y от 0 до {b}')
    print('А именоо: ')
    for i in range(b,-1,-1):
        print(-i, end=' ')
elif a == 4:
    print(f'Диапазон чисел X от 0 до {b}')
    print('А именоо: ')
    for i in range(b,-1,-1):
        print(-i, end=' ')
    print()
    print(f'Диапазон чисел Y от 0 до {b}')
    print('А именоо: ')
    for i in range(b + 1):
        print(i, end=' ')
