import sys

def simpleaddition():
    return sum([int(x) for x in sys.stdin.readlines()])

print(simpleaddition())
