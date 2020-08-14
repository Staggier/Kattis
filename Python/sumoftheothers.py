import sys

def sumoftheothers():
    for line in sys.stdin.readlines():
        lst = [int(x) for x in line.split()]

        for i in range(len(lst)):
            if sum(lst) - lst[i] == lst[i]:
                print(lst[i])
                break

sumoftheothers()
