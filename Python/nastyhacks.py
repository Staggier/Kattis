from os import sys

def nastyhacks():
    n = int(sys.stdin.readline())

    for i in range(1, n + 1):
        lst = [int(x) for x in sys.stdin.readline().split()]

        a, b, c = lst[0], lst[1], lst[2]
        if a == b - c:
            print('does not matter')
        elif a > b - c:
            print('do not advertise')
        else:
            print('advertise')
    return

nastyhacks()
