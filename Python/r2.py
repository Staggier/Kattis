from os import sys

def r2():
    inp = [int(x) for x in sys.stdin.readline().split()]
    r1, s = inp[0], inp[1]
    print(s * 2 - r1)

r2()
