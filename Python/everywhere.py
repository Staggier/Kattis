from os import sys

def everywhere():
    t = int(sys.stdin.readline())
    for i in range(0, t):
        n = int(sys.stdin.readline())
        lst = []
        for j in range(0, n):
            lst.append(sys.stdin.readline())
        print(len(set(lst)))
    return

everywhere()
