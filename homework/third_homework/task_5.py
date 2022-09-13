a = int(input('Enter number: '))
doub = []
while a > 0:
    doub.append(a % 2)
    a = a // 2
for i in range(len(doub) // 2):
    doub[i], doub[-(i+1)] = doub[-(i+1)], doub[i]
print(doub)
