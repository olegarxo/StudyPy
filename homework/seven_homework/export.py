def export_txt(dic_user):
    with open('datauser.txt', 'a', encoding='UTF8') as file:
        for key in dic_user:
            file.writelines(f'{key}: ' + ','.join(dic_user[key]) + '\n')
