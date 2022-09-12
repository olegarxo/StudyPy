import math
print(math.ceil(2.5))
def Comp_num(lists):
    leng = len(lists)
    flag = True
    count = 0
    compit_list = []
    while flag:
        if count == math.ceil(leng / 2):
            flag = False
            return compit_list
        else:
            compit_list.append((lists[count] * lists[0 - (count + 1)]))
            count += 1
num = []
tamp = int(input('Enter number: '))
for i in range(tamp):
    num.append(int(input('Enter number: ')))
a = Comp_num(num)
print(a)