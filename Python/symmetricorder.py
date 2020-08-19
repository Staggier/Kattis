def symmetricorder():
    c = 1
    while True:
        n = int(input())
        if n == 0:
            break
        print("SET", c)
        lst = [""] * n
        b = True
        i = 0
        while i < n // 2:
            if b:
                lst[i] = input()
                b = False
            else:
                lst[(n - 1) - i] = input()
                b = True
                i += 1
        if n % 2 == 1:
            lst[i] = input()
        for i in range(0, n):
            print(lst[i])
        c += 1
    return
    
symmetricorder()
