import math

def beavergnaw():
    d, v = [float(x) for x in input().split()]
    while d != 0 and v != 0:
        r = d / 2
        print(math.sqrt((r ** 2) - (v / math.pi / d)))
        d, v = [float(x) for x in input().split()]
    return

beavergnaw()
