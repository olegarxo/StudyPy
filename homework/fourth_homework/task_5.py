from math import fabs as fab
def ListNum(string):   #Преобразует функцию, забирая ненужные символы
    string = string.replace(' ', '').replace('^', '').split('=')
    left_string = string[0].split('+')
    return left_string
def Read_file(open_file):   #Читает первую строку и записывает ее в переменную
    with open(open_file, 'r+') as f:
        text = f.readline()
    return text
def Dict_numdeg_val(sum_list):   #основная магия
    degree_val = { }
    flag = True
    for i in sum_list:
        j = - 1
        k = 0
        flag = True
        count = 0
        tamp_deg = 0
        tamp_num = 0
        leng = len(i)
        while (flag):
            if i[-1] == 'x':
               tamp_deg = 1
               degree_val[tamp_deg] = 0
               flag = False
               count = j
            elif fab(j) == leng + 1:
                degree_val[0] = tamp_deg
                flag = False
                count = j
                return degree_val
            elif i[j] == 'x':
                degree_val[tamp_deg] = 0
                flag = False
                count = j
            else:
                tamp_deg += int(int(i[j]) * (10 ** (fab(j) - 1)))
                j -= 1
        flag = True
        while (flag):
            if (leng + count) == 0:
                flag = False
            else:
                tamp_num += int(i[k]) * (10**(leng + (count - 1)))
                degree_val[tamp_deg] = tamp_num
            k += 1
            count -= 1
    return degree_val
def Sum_dict(item_one, item_two):
    for key, value in item_one.items():
        item_one[key] = value + item_two.get(key, 0)
    return item_one
def Reade_funk(item_one):
    with open('f3.txt', 'w+') as f:
        for key, value in item_one.items():
            if key == 0:
                f.write(f'{value}')
                f.write('= 0')
            else:
                f.write(f'{value}x^{key} + ')
open_file1 = 'f1.txt' #input(('Вставьте имя первого файла из папки : '))
open_file2 = 'f2.txt'   #input(('Вставьте имя первого файла из папки : '))
text_one = Read_file(open_file1)
text_two = Read_file(open_file2)
new_text_one = ListNum(text_one)
new_text_two = ListNum(text_two)
new_dic_one = Dict_numdeg_val(new_text_one)
new_dyc_two = Dict_numdeg_val(new_text_two)
if len(new_text_two) > len(new_text_one):
    tamp = Sum_dict(new_dyc_two, new_dic_one)
else:
    tamp = Sum_dict(new_dic_one, new_dyc_two)
print(Reade_funk(tamp))
exit()
