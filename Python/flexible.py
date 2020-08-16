def flexible():
    k, n = [int(x) for x in input().split()]
    
    lst = [int(x) for x in input().split()]
    lst.append(0)
    lst.append(k)
    
    for i in range(n + 2):
        for j in range(n + 2):
            if i == j:
                continue
            lst.append(abs(lst[i] - lst[j]))
            
    lst.sort()
    for num in list(set(lst))[1:]:
        print(num, end=" "),
    return
    
flexible()
