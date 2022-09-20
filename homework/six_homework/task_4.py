#пара-ра-рам рам-пам-папам па-ра-па-дам
glas = ['а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я']
text = input().split()
count = [sum(i in glas for i in line) for line in text]
if len(set(count)) == 1:
    print('Есть рифма')
else:
    print('Рифмы нет')
