from random import randint, random

b = int(random() * 30)
a = int(input('Введите четверть'))
if a == 1:
    print(f'Диапазон чисел X от 0 до {b}')
    print(f'Диапазон чисел X от 0 до {b}')
elif a == 2:
    print(f'Диапазон чисел X от 0 до {-b}')
    print(f'Диапазон чисел Y от 0 до {b}')
elif a == 3:
    print(f'Диапазон чисел X от 0 до {-b}')
    print(f'Диапазон чисел Y от 0 до {-b}')
elif a == 4:
    print(f'Диапазон чисел X от 0 до {b}')
    print(f'Диапазон чисел Y от 0 до {-b}')
