p = 3
for i in range(4, 100):
    p += 4 / ((i - 2) * (i - 1) * i)
    p -= 4 / (i * (i + 1) * (i + 2))
print(p)
coun = int(input('Введите количество знаков: '))
print(int(p * (10 ** coun)) / (10 ** coun))