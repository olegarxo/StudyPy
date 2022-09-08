import random
def Number_shir(count, heigh_tabe, heigh_boy):
    tamp = 1
    for i in range(count):
        if heigh_tabe[i] <= heigh_boy:
            return tamp
        elif i == count - 1:
            return count + 1
        tamp += 1
count = int(input('Введите количество учеников в ширенге'))
rand = random.Random()
heigh = []
heigh_boy = int(input('Введите рост мальчика'))
tamp = 200
for i in range(count):
    minus_heigh = rand.randint(0, 5)
    heigh.append(tamp - minus_heigh)
    tamp -= minus_heigh
place = Number_shir(count, heigh, heigh_boy)
print(place)
