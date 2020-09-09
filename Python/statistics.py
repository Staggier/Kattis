import sys

def statistics():
    t = 1
    for line in sys.stdin.readlines():
        Min, Max = 10 ** 6, -1 * (10 ** 6)
        for num in [int(x) for x in line.split()][1:]:
            if num > Max:
                Max = num
            if num < Min:
                Min = num
        print("Case ", t, ": ", sep="", end="")
        print(Min, Max, Max - Min, sep = " ")
        t += 1
        
    return
            
statistics()
