from math import fabs as fab
def ListNum(string):
    string = string.replace(' ', '').replace('^', '').split('=')
    left_string = string[0].split('+')
    return left_string
def Read_file(open_file):
    with open(open_file, 'r+') as f:
        text = f.readline()
    return text
def Dict_numdeg_val(sum_list):
    degree_val = { }
    flag = True
    for i in sum_list:
        j = - 1
        k = 0
        tamp_deg = 0
        tamp_num = 0
        leng = len(i)
        while (flag):
            tamp_deg += int(i[j]) * (10 * fab(j))
            if i[j] == 'x':
                degree_val[tamp_deg] = 0
                flag = False
        while (flag):
            tamp_num += int(i[k]) * (10 * fab(j))



open_file1 = input(('Вставьте имя первого файла из папки : '))
open_file2 = input(('Вставьте имя первого файла из папки : '))
text_one = Read_file(open_file1)
text_two = Read_file(open_file2)
print(text_one)
print(text_two)
new_text_one = ListNum(text_one)
new_text_two = ListNum(text_two)
print(new_text_one)
print(new_text_two)
exit()
text_one = ListNum(Read_file(open_file1))
text_two = ListNum(Read_file(open_file2))
first_string_new = []
print(first_string)
for i in first_string:
    print(i)
    if i == '=' or 'x' or '^':
        first_string_new.append('')
    else:
        first_string_new.append(i)
print(first_string_new)
print(list_str)
tamp = 0
i = 0
while flag:
    if list_str[i] == '^' or ' ':
        list_str.pop(i)
    elif list_str == '=':
        flag = False
    i += 1
print(list_str)