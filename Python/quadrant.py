from os import sys

def quadrant():
    x, y = int(sys.stdin.readline()), int(sys.stdin.readline())

    if x > 0 and y > 0:
        print(1)
    elif x > 0 and y < 0:
        print(4)
    elif x < 0 and y > 0:
        print(2)
    else:
        print(3)
    return

quadrant()
