def Fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibo(n - 1) + Fibo(n - 2)
lists = []
for i in range(20):
    a = Fibo(i)
    lists.append(a)
    lists.insert(0, -a)
print(lists)