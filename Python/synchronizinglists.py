def synchronizinglists():
    while True:
        n = int(input())
        if n == 0:
            break

        lst1, lst2, lst3 = [], [], []
        for i in range(n):
            num = int(input())
            lst1.append(num)
            lst3.append(num)

        for i in range(n):
            num = int(input())
            lst2.append(num)

        lst1.sort()
        lst2.sort()
        d = {}

        for i in range(n):
            d[lst1[i]] = lst2[i]

        for i in range(n):
            print(d[lst3[i]])
        print("\n", end="")
        
    return

synchronizinglists()
