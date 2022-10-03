import sqlite3


def Enter_schedule():
    flag = True
    while flag:
        with sqlite3.connect('school.db') as db:
            cursor = db.cursor()
            comand = db.execute('SELECT * FROM schedule')
            names = list(map(lambda x: x[0], comand.description))
            ansver = input('Хотите добавить данные? ДА/НЕТ: ')
            if ansver.lower() == 'да':
                print(*names, sep='\n')
                class_number = input('Введите номер класса: ')
                number_lesson = input('Введите какой по счету урок: ')
                start_lesson = input('Введите начал занятия: ')
                end_lesson = input('Введите конец занятия: ')
                lesson_name = input('Введите название предмета: ')
                teasher_name = input('Введите имя преподавателя: ')
                entities = (class_number, number_lesson, start_lesson, end_lesson, lesson_name, teasher_name)
                cursor.execute('INSERT INTO schedule VALUES(?, ?, ?, ?, ?, ?)', entities)
            elif ansver.lower() == 'нет':
                flag = False
            else:
                print('Введен некоректный ключ, попробуйте еще раз')


def Enter_students():
    flag = True
    while flag:
        with sqlite3.connect('school.db') as db:
            cursor = db.cursor()
            comand = db.execute('select * from students')
            names = list(map(lambda x: x[0], comand.description))
            ansver = input('Хотите добавить данные? ДА/НЕТ: ')
            if ansver.lower() == 'да':
                print(*names, sep='\n')
                name = input('Введите имя: ')
                class_number = input('Введите класс: ')
                tel_number = input('Введите номер телефона: ')
                date = input('Введите дату рождения: ')
                entities = (name, class_number, tel_number, date)
                cursor.execute('INSERT INTO students VALUES(?, ?, ?, ?)', entities)
            elif ansver.lower() == 'нет':
                flag = False
            else:
                print('Введен некоректный ключ, попробуйте еще раз')



def Enter_teachers():
    flag = True
    while flag:
        with sqlite3.connect('school.db') as db:
            cursor = db.cursor()
            comand = db.execute('SELECT * FROM teachers')
            names = list(map(lambda x: x[0], comand.description))
            ansver = input('Хотите добавить данные? ДА/НЕТ: ')
            if ansver.lower() == 'да':
                print(*names, sep='\n')
                name = input('Введите имя преподавателя: ')
                birthday = input('Введите дату рождения: ')
                tel_number = input('Введите номер телефона: ')
                adress = input('Введите адресс проживания: ')
                main_sumject = input('Введите основной предмет: ')
                main_class = input('Введите основной класс: ')
                entities = (name, birthday,  tel_number, adress, main_sumject, main_class)
                cursor.execute('INSERT INTO teachers VALUES(?, ?, ?, ?, ?, ?)', entities)
            elif ansver.lower() == 'нет':
                flag = False
            else:
                print('Введен некоректный ключ, попробуйте еще раз')



