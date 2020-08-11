import sys

def notamused():
    inp = sys.stdin.readlines()

    days = inp.count("OPEN\n")
    i, day = 0, 1
    while i < len(inp):
        print("Day", day)
        s = inp[i].split()

        customers = {}
        names = []

        while s[0] != "CLOSE":
            if s[0] == "OPEN":
                i += 1
                s = inp[i].split()
                continue
            
            if s[1] not in names:
                names.append(s[1])
                customers[s[1]] = []
                
            customers[s[1]].append(int(s[2]))
            i += 1
            s = inp[i].split()

        names.sort()
        for name in names:
            result = 0
            for j in range(0, len(customers[name]) - 1, 2):
                result += (customers[name][j + 1] - customers[name][j]) * 0.1
            print(name, " $", '{0:.2f}'.format(result), sep="")
        print()
        i += 1
        day += 1
    return

notamused()
