def different(n):
    d = {}
    for c in str(n):
        if d.get(c) is None:
            d[c] = 1
        else:
            return False
    return True
    
def divisible(n):
    k = n
    
    while k != 0:
        t = k % 10
        if t == 0 or n % t != 0:
            return False
        k = k // 10
    return True

def heirsdilemma():
    n, k = [int(x) for x in input().split()]
    
    result = 0
    for i in range(n, k + 1):
        if different(i) and divisible(i):
            result += 1
    return result

print(heirsdilemma())
