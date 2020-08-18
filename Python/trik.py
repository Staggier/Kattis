from os import sys

def trik():
    s = sys.stdin.readline()
    spot = 1

    for c in s:
        if c == 'A':
            spot = 2 if spot == 1 else 1 if spot == 2 else spot
        elif c == 'B':
            spot = 3 if spot == 2 else 2 if spot == 3 else spot
        elif c == 'C':
            spot = 3 if spot == 1 else 1 if spot == 3 else spot
    print(spot)
    return

trik()
