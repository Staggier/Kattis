from os import sys

def twostones():
    n = int(sys.stdin.readline())
    if n % 2 is 0:
        print('Bob')
    else:
        print('Alice')
    return

twostones()
