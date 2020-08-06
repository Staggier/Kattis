from os import sys

def cetvrta():
    x, y = [], []
    for i in range(0, 3):
        inp = [int(x) for x in sys.stdin.readline().split()]
        x.append(inp[0])
        y.append(inp[1])

    x.sort()
    y.sort()

    a, b, c, d = min(x), max(x), min(y), max(y)
    a = a if x.count(a) < x.count(b) else b
    b = c if y.count(c) < y.count(d) else d
                          
    print(a, b)
    return

cetvrta()
        
        
                   
        
