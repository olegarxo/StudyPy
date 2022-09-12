lists = []
list_dec = []
flag = True
count = 1
leng = len(lists)
a = int(input('Сколько хотите чисел в списке '))
for i in range(a):
    b = float(input('Введите число: '))
    lists.append(b)
    list_dec.append(b - int(b))
for i in range(leng):
    for g in range(leng - i):
        if list_dec[g] > list_dec[g + 1]:
            list_dec[g], list_dec[g + 1] = list_dec[g + 1], list_dec[g]
print(f'{lists}->{list_dec[-1] - list_dec[0]}')