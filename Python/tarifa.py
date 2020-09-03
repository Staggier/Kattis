from os import sys

def tarifa():
    x, n = int(sys.stdin.readline()), int(sys.stdin.readline())

    r = x
    for i in range(1, n + 1):
        if r < x:
            r += x
        r += (x - int(sys.stdin.readline()))
    print(r)
    return

tarifa()
