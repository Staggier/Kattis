from os import sys

def oddities():
    n = int(sys.stdin.readline())

    for i in range(1, n + 1, 2):
        num = int(sys.stdin.readline())

        if num % 2 == 0:
            print(num, 'is even')
        else:
            print(num, 'is odd')
    return

oddities()
        
