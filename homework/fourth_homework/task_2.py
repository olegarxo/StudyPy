def Easy_multi(numb, list_multi):
    flag = True
    i = 2
    while flag:
        if numb == 1:
            flag = False
            return list_multi
        elif numb % i == 0:
             numb /= i
             list_multi.append(i)
             i = 2
        else:
             i += 1
a = int(input('Enter number: '))
list_multi = []
print(Easy_multi(a, list_multi))
