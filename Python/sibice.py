from os import sys
import math

def sibice():
    inp = [int(x) for x in sys.stdin.readline().split()]
    n, w, h = inp[0], inp[1], inp[2]

    for i in range(1, n + 1):
        if math.sqrt((w ** 2) + (h ** 2)) >= int(sys.stdin.readline()):
            print('DA')
        else:
            print('NE')
    return

sibice()
