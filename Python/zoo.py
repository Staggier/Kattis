def zoo():
    c = 1
    while True:
        n = int(input())
        if n == 0:
            break
        
        d = {}
        lst = []
        
        for i in range(n):
            s = input().split()
            if d.get(s[-1].lower()) is None:
                d[s[-1].lower()] = 1
                lst.append(s[-1].lower())
            else:
                d[s[-1].lower()] += 1
        
        print("List ", c, ":", sep = "")
        c += 1
        
        for name in sorted(lst):
            print(name, "|", d[name])
        
    return
    
zoo()
