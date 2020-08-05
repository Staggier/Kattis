from os import sys

def abc():
    inp = []
    for line in sys.stdin:
        inp.append(line)

    num = []
    for n in inp[0].split():
        num.append(int(n))

    num.sort()
    
    d = {"A":num[0], "B":num[1], "C":num[2]}
    s = list(inp[1])
    print(d.get(s[0]), d.get(s[1]), d.get(s[2]))
    return

abc()
