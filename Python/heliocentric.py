import sys

def heliocentric():
    num = 1
    for line in sys.stdin.readlines():
        n, k = [int(x) for x in line.split()]
        
        i = 0
        while ((n + i) % 365) != 0 or ((k + i) % 687) != 0:
            i += 1
        print("Case ", num, ": ", i, sep="")
        num += 1
    return

heliocentric()  
