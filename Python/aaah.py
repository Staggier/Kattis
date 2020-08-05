from os import sys

def aaah():
    inp = []
    for line in sys.stdin:
        inp.append(line)

    jon, doc = inp[0], inp[1]
    i = 0
    while True:
        if doc[i] == 'h':
            print('go')
            break
        elif jon[i] == 'h':
            print('no')
            break
        i += 1
    return

aaah()
