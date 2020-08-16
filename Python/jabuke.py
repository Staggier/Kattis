def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3)) + (x2 * (y3 - y1)) + (x3 * (y1 - y2))) / 2
    
def contains(x1, y1, x2, y2, x3, y3, x4, y4):
    a1 = area(x1, y1, x2, y2, x3, y3)
    a2 = area(x4, y4, x2, y2, x3, y3)
    a3 = area(x1, y1, x4, y4, x3, y3)
    a4 = area(x1, y1, x2, y2, x4, y4)
    
    return a1 == a2 + a3 + a4
    
def jabuke():
    coords = []
    for i in range(3):
        x, y = [int(z) for z in input().split()]
        coords.append(x)
        coords.append(y)
    
    n = int(input())
    x1, y1, x2, y2, x3, y3 = coords
    
    a = area(x1, y1, x2, y2, x3, y3)
    result = 0
    
    for i in range(n):
        x, y = [int(z) for z in input().split()]
        if contains(x1, y1, x2, y2, x3, y3, x, y):
            result += 1
    
    print(a, result, sep="\n")
    return
    
jabuke()
