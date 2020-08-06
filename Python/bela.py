from os import sys

def bela():
    inp = sys.stdin.readline().split()
    n, s = int(inp[0]), inp[1]

    d, nd = [11, 4, 3, 20, 10, 14, 0, 0], [11, 4, 3, 2, 10, 0, 0, 0]
    cards = {'A':0, 'K':1, 'Q':2, 'J':3, 'T':4, '9':5, '8':6, '7':7}

    p = 0
    for i in range(0, n):
        for c in range(0, 4):
            inp = sys.stdin.readline()
            t = inp[1]
            p += d[cards[inp[0]]] if t == s else nd[cards[inp[0]]]
            
    print(p)
    return

bela()
