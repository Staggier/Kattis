from os import sys

def dicecup():
    inp = [int(x) for x in sys.stdin.readline().split()]
    n, m = min(inp), max(inp)

    if n == m:
        print(n + 1)
    else:      
        for i in range(n + 1, m + 2):
            print(i)

dicecup()
