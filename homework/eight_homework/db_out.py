import sqlite3

con = sqlite3.connect('school.db')


def Out_schedule():
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM schedule')
    [print(*row, sep='\t', end='\t') for row in cursorObj.fetchall()]


def Out_students():
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM students')
    [print(*row, sep='\t', end='\t') for row in cursorObj.fetchall()]


def Out_teachers():
    cursorObj = con.cursor()
    cursorObj.execute('SELECT * FROM teachers')
    [print(*row, sep='\t', end='\t') for row in cursorObj.fetchall()]



