def import_txt(dic_user):
    data_colum = {}
    with open(f'{dic_user}'+'.txt', 'r', encoding='UTF8') as file:
        for colum in file:
            tamp = colum.split(':')
            tamp[1] = tamp[1].replace(' ', '')
            data_colum[tamp[0]] = tamp[1]
        return data_colum
