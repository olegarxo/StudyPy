import db_use
import db_out


def Interaction_user():
    flag_1 = True
    flag_2 = True
    while flag_1 == True or flag_2 == True:
        while flag_1:
            flag_2 = True
            print('shedule\nstudent\nteachers')
            ansver = input('С какой таблицей хотите поработать: ')
            if ansver == 'schedule':
                db_use.Enter_schedule()
                flag_1 = False
            elif ansver == 'student':
                db_use.Enter_students()
                flag_1 = False
            elif ansver == 'teachers':
                db_use.Enter_teachers()
                flag_1 = False
            else:
                print('Вы ввели некоректные данныые, попробуйте еще раз')
        while flag_2:
            end = input('Хотите добавить еще данные в таблицу? Да/НЕТ')
            if end.lower() == 'нет':
                flag_2 = False
            elif end.lower() == 'да':
                flag_1 = True
                flag_2 = False
            else:
                print('Вы ввели некоректные данные, попробуйте еще раз')


def Data_user():
    flag_1 = True
    while flag_1:
        print('shedule\nstudent\nteachers')
        ansver = input('Из какой таблицы хотите вывести данные?: ')
        if ansver == 'schedule':
            db_out.Out_schedule()
        elif ansver == 'student':
            db_out.Out_students()
        elif ansver == 'teachers':
            db_out.Out_teachers()
        else:
            print('Вы ввели некоректные данныые, попробуйте еще раз')
