from os import sys

def aboveaverage():
    c = int(sys.stdin.readline())

    for t in range(1, c + 1):
        lst = [int(x) for x in sys.stdin.readline().split()]
        average = sum(lst[1::])/lst[0]

        count = 0
        for n in lst[1::]:
            if n > average:
                count += 1

        print('{0:.3f}%'.format((count / (lst[0])) * 100))

aboveaverage()

    
