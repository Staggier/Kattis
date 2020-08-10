def haypoints():
    w, l = [int(x) for x in input().split()]
    
    d = {}
    for word in range(w):
        s = input().split()
        d[s[0]] = int(s[1])
    
    line = 0
    while line < l:
        result = 0
        while True:
            s = input().split()
            if s[0][0] == '.':
                break
            
            for word in s:
                if d.get(word) is not None:
                    result += d[word]
        print(result)            
        line += 1
    return

haypoints()
