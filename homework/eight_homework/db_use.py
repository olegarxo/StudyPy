import sqlite3
def Enter_schedule():
    with sqlite3.connect('school.db') as db:
        cursor = db.cursor()
        cursor.execute(f'INSERT INTO schedule VALUES')
def Enter_students():
    with sqlite3.connect('school.db') as db:
        cursor = db.execute('select * from students')
        names = list(map(lambda x: x[0], cursor.description))
        print(names)
        cursor = db.execute('select * from students')
        names = list(map(lambda x: x[0], cursor.description))
        print(names)
def Enter_teachers():
    with sqlite3.connect('school.db') as db:
        cursor = db.cursor()
        cursor.execute('INSERT INTO teachers VALUES')
Enter_students()