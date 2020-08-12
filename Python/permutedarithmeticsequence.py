def permutedarithmeticsequence():
    n = int(input())
    
    for i in range(n):
        lst = [int(x) for x in input().split()]
        
        t = lst[1:]
        s = 0
        
        b1 = True
        for j in range(lst[0] - 1, 0, -1):
            if s != 0 and (t[j] - t[j - 1]) != s:
                b1 = False
                break
            else:
                s = t[j] - t[j - 1]
        
        if b1:
            print("arithmetic")
            continue
        t.sort()
        
        b2 = True
        s = 0
        for j in range(lst[0] - 1, 0, -1):
            if s != 0 and (t[j] - t[j - 1]) != s:
                b2 = False
                break
            else:
                s = t[j] - t[j - 1]
        
        if b2:
            print("permuted arithmetic")
        else:
            print("non-arithmetic")
            
    return
    
permutedarithmeticsequence()
