from os import sys

def nodup():
    words = sys.stdin.readline().split()

    d = {}
    for word in words:
        if d.get(word) is None:
            d[word] = 0
            continue
        else:
            print('no')
            return
    print('yes')
    return

nodup()
