from os import sys

def pieceofcake2():
    inp = [int(x) for x in sys.stdin.readline().split()]
    n, h, v = inp[0], inp[1], inp[2]

    x, y = 0, 0
    if v > n - v:
        x = v
    else:
        x = n - v
    if h > n - h:
        y = h
    else:
        y = n - h

    print(x * y * 4)
    return

pieceofcake2()
