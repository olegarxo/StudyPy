def Fibonachi(end_point):
    a =[]
    a[0] = 0
    a[1] = 1
    i = 0
    if end_point == 0:
        print(a[0])
    elif end_point == 1:
        print(a[1])
    else: 
        while i < end_point - 1:
            a.append(a[i] - a[i + 1])
    print(a[end_point])

end = int(input('Введите N-e число фибаначи - '))
Fibonachi(end)
