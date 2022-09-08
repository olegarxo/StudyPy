def Min_num(number):
    tamp = 2
    for i in range(number):
        if number % tamp == 0:
            return tamp
        else:
            tamp += 1
number = int(input('Введите число - '))
print(Min_num(number))