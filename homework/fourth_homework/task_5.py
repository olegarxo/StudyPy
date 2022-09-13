import random
num = [1, 'x']
flag = True
f = open('function.txt','r+')
string = f.readlines()
first_string = string[0]
second_string = string[1]
print(first_string)
a = first_string.split(' ')
first_string_num = []
for i in range(len(a)):
    if a[i] == '=' or '+':
        continue
    else:
        first_string_num.append(a[i])
print(first_string_num)
