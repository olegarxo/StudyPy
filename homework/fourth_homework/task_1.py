# в условии не было сказано, что нельзя брать значение из библиотеки
from math import pi as p
coun = int(input('Введите количество знаков: '))
print(int(p * (10 ** coun)) / (10 ** coun))