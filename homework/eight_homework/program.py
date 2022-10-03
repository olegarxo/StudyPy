import db_use


def Interaction_user():
    flag_1 = True
    while flag_1:
        flag_2 = True
        print('shedule\nstudent\nteachers')
        ansver = input('С какой таблицей хотите поработать')
        if ansver == 'schedule':
            db_use.Enter_schedule()
        elif ansver == 'student':
            db_use.Enter_students()
        elif ansver == 'teachers':
            db_use.Enter_teachers()
        while flag_2:
            end = input('Хотите добавить еще данные в таблицу? Да/НЕТ')
            if end.lower() == 'нет':
                flag_1 = False
                flag_2 = False
            elif end.lower() == 'да':
                flag_2 = False
            else:
                print('Вы ввели некоректные данные, попробуйте еще раз')
