from import_data import import_txt as imp
from data import list_dic
name = input('Введите название файла: ')
data_import = imp(name)
list_dic.append(data_import)
for i in data_import.keys():
    print(f'{i}: {data_import[i]}', end='\n')
