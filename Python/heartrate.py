from os import sys

def heartrate():
    n = int(sys.stdin.readline())

    for i in range(1, n + 1):
        inp = [float(x) for x in sys.stdin.readline().split()]
        
        temp, bpm = 60 / inp[1], 60 * inp[0] / inp[1]
        print('{0:.4f}'.format(bpm - temp), '{0:.4f}'.format(bpm), '{0:.4f}'.format(bpm + temp))
    return

heartrate()
