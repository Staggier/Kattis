from os import sys

def hangingout():
    inp = sys.stdin.readline().split()
    s, x, c, r = int(inp[0]), int(inp[1]), 0, 0
    
    for i in range(0, x):
        line = sys.stdin.readline().split()
        t = int(line[1])
        if line[0] == "enter":
            if r + t > s:
                c += 1
            else:
                r += t
        else:
            r -= t

    print(c)
    return

hangingout()
