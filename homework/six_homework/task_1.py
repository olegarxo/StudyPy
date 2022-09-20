def print_operation_table(function, line, colum):
    if line is None:
        line = 9
    if colum is None:
        colum = 9
    for i in range(1, line + 1):
        print('\n')
        for j in range(1, colum + 1):
            print(function(i, j), end='\t')
line = input('Enter line bi table: ')
colum = input('Enter colum bi table: ')
if line == '':
    line = None
else:
    line = int(line)
if colum == '':
    colum = None
else:
    colum = int(colum)
print_operation_table(lambda x, y: x * y, line, colum)