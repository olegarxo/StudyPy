def Count_num(count):
    global summ
    if count == 0:
        return
    summ += count
    Count_num(count - 1)
summ = 0
count = int(input('Введите'))
Count_num(count)
print(summ)
#!!!Не смог разобраться без глобльной переменной!!!
#def Count_num(count, summ):
#    if count == 0:
#        return summ
#    summ += count
#    Count_num(count - 1, summ)
#count = int(input('Введите'))
#summ = Count_num(count, 0)
#print(summ)