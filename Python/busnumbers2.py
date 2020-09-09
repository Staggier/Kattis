import math

def busnumbers2():
    lim = int(input())
    m = None

    if lim < 1729:
        return m

    foundOne = False
    
    n = lim
    while n > 1:
        for b in range(1, math.ceil((n // 2) ** (1.0 / 3.0))):
            a = round((n - (b ** 3)) ** (1.0/ 3.0))
            t = (a ** 3) + (b ** 3)
            if t == n:
                if foundOne:
                  return t
                else:
                  foundOne = True

        foundOne = False
        n -= 1

    return m

print(busnumbers2())
