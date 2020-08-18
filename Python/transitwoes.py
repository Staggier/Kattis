from os import sys

def transitwoes():
    inp = [int(x) for x in sys.stdin.readline().split()]
    s, t, n = inp[0], inp[1], inp[2]

    d = [int(x) for x in sys.stdin.readline().split()]
    b = [int(x) for x in sys.stdin.readline().split()]
    c = [int(x) for x in sys.stdin.readline().split()]

    i = 0
    s = d[i]

    while i < n:
        if s > t:
            print('no')
            return
        elif s > c[i]:
            s += c[i]
            i += 1
        else:
            s += b[i] + d[i + 1]
    print('yes')
    return

transitwoes()
        
        
