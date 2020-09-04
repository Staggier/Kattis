from os import sys

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

def zamka():
    l, d, x = [int(x) for x in sys.stdin.readlines().split()]
    n, k = 0, 0

    if x % l is 0:
        n = x
    else:
        i, d = l, 1
        while True:
            if (
            
    if d % x is 0:
        k = d
    else:
        

    print(n, '\n', k)
    return

zamka()
