def peragrams():
    s = input()
    d = {}
    lst = []
    
    for c in s:
        if d.get(c) is None:
            d[c] = 1
            lst.append(c)
        else:
            d[c] += 1
            
    if len(lst) == 1:
        return 0
    
    result = 0
    b = True
    
    for c in lst:
        if d[c] % 2 == 1:
            if b:
                b = False
            else:
                result += 1
    return result

print(peragrams())
