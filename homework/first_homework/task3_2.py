from math import sqrt
def Enter_coordinates(number):
    point = []
    point.append(int(input(f'Введите Х {number}-й точки - ')))
    point.append(int(input(f'Введите Y {number}-й точки - ')))
    return point
def DistanceonPoint(point_one, point_two):
    dist = sqrt(((point_two[0] - point_one[0]) ** 2) + ((point_two[1] - point_one[1]) ** 2))
    return dist
pointA = Enter_coordinates(1)
pointB = Enter_coordinates(2)
dist = DistanceonPoint(pointA, pointB)
print(f'Дистанция между точками равна {round(dist,2)}')
