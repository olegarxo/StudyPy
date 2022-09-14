def ListNum(string):
    string = string.replace(' ', '').replace('^', '').split('=')
    left_string = string[0].split('+')
    return left_string
def Read_file(open_file):
    f = open(open_file, 'r+')
    text: str = f.readline()
    open_file.close()
    return text
open_file1 = open(input('Вставьте имя первого файла из папки : '), 'w+')
open_file2 = open(input('Вставьте имя первого файла из папки : '), 'w+')
text_one = Read_file(open_file1)
text_two = Read_file(open_file2)
print(text_one)
print(text_two)

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