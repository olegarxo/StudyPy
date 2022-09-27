def create_data():
    some_data = {}
    flag_one = True
    key = ''
    val = []
    while flag_one:
        a = (input('Хотите добавить данные в базу? ДА/НЕТ\n').lower().replace(' ', ''))
        if a == 'да':
            flag_two = True
            key = input('Введите ФИО: ')
            val.append(input('Введите номер телефона через(-) \n'))
            while flag_two:
                tamp = (input('Хотите добавить еще номер телефона человеку? ДА/НЕТ\n').lower())
                if tamp == 'да':
                    val.append(input('Введите номер телефона через(-) '))
                elif tamp == 'нет':
                    flag_two = False
                    some_data[key] = val
                else:
                    print('Вы ввели неправильный ключи')
                    flag_two = True
        elif a == 'нет':
            flag_one = False
            some_data[key] = val
            return some_data
        else:
            print('Вы ввели неправильный ключи')
            flag_one = True

