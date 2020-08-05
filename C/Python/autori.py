from os import sys

def autori():
    s = ""
    for c in sys.stdin.readline().split('-'):
        s += c[0]
    print(s)
    return

autori()
