from os import sys

def grassseed():
    s, l = float(sys.stdin.readline()), int(sys.stdin.readline())

    c = 0
    for i in range(0, l):
        inp = sys.stdin.readline().split()
        c += s * float(inp[0]) * float(inp[1])

    print('{0:07f}'.format(c))
    return

grassseed()
