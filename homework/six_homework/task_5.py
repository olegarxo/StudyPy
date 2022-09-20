def sev_by(function, lists):
    tamp = list(filter(function, lists))
    print(tamp)
    return len(lists) == len(tamp)


values = list(map(int, (input('Введите числа через пробел: ').split())))
print(values)
if sev_by(lambda x: x % 2 == 0, values):
    print('same')
else:
    print('different')
