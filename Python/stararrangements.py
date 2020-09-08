def func():
    n = int(input())

    i = 2
    while i < n:
        b = True
        t = 
        c1, c2 = 0, 0
        while t <= n:
            if b:
                b = False
                t += i
                c1 += 1
            else:
                b = True
                t += (i - 1)
                c2 += 1
            if t == n:
                if c1 != c2:
                    print(i, ",", i - 1, sep="")
                    print(i, ",", i, sep="")
                else:
                    print(i, ",", i - 1, sep="")
        
        i += 1
    return

func()
