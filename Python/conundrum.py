from os import sys

def conundrum():
    s = sys.stdin.readline()
    t = ['P', 'E', 'R']

    c = 0
    for i in range(0, len(s) - 1):
        c += 1 if s[i] == t[i % 3] else 0
    print(c)
    return

conundrum()
        
