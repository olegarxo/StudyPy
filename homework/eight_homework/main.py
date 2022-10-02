import sqlite3
import db_use


flag_1 = True
while flag_1:
    print('shedule\nstudent\nteachers')
    ansver = input('С какой таблицей хотите поработать')
    if ansver == 'schedule':
        db_use.Enter_schedule()
    elif ansver == 'student':
        db_use.Enter_students()
    elif ansver == 'teachers':
        db_use.Enter_teachers()
    end = input('Хотите добавить еще данные в таблицу?')
    if enыыы