def towering():
    lst = [int(x) for x in input().split()]
    
    a, b = lst[6], lst[7]
    lst = lst[:6]
    
    t = []
    b = True
    for i in range(6):
        for j in range(6):
            if i == j:
                continue
            for k in range(6):
                if k == i or k == j:
                    continue
                if lst[i] + lst[j] + lst[k] == a:
                    t = [lst[i], lst[j],  lst[k]]
                    b = False
                    break
            if not b:
                break
        if not b:
            break
        
    for num in t:
        del lst[lst.index(num)]
    
    t = sorted(t, reverse=True)
    lst = sorted(lst, reverse=True)
    
    for num in t:
        print(num, end=" ")
    for num in lst:
        print(num, end=" ")
    
    return

towering()
