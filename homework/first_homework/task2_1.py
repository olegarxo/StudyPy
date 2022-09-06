def inputPoint():
    point = ["X", "Y", "Z"]
    a = []
    for i in range(3):
        a.append(input(f"Введите значение {point[i]}: "))
    return a


def checkPredicate(point):
    left = not (point[0] or point[1] or point[2])
    right = not point[0] and not point[1] and not point[2]
    result = left == right
    return result


statement = inputPoint()

if checkPredicate(statement) == True:
    print(f"Утверждение истинно")
else:
    print(f"Утверждение ложно")