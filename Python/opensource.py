import sys

def modsort(lst):
    b = False
    n = len(lst)
    
    while not b:
        b = True
        for j in range(n - 1):
            if len(list(set(lst[j][1]))) == len(list(set(lst[j + 1][1]))):
                if lst[j][0] > lst[j + 1][0]:
                    t = lst[j]
                    lst[j] = lst[j + 1]
                    lst[j + 1] = t
                    b = False
    return lst

def opensource(j, inp):
    lst = []
    result = []
    last = ""

    i = -1
    for line in inp[j:]:
        if line == '1\n' or line == '0\n':
            if line == '1\n':
                j += 1
                break
            return
        if line.isupper():
            result.append([line[:len(line) - 1], []])
            i += 1
        else:
            lst.append(line)
            result[i][1].append(line)
        j += 1


    for line in lst:
        c = 0
        for t in result:
            if line in t[1]:
                c += 1
        if c != 1:
            for t in result:
                if line in t[1]:
                    for i in range(t[1].count(line)):
                        del t[1][t[1].index(line)]

    result = sorted(result, key=lambda a : len(list(set(a[1]))), reverse=True)
    a = modsort(result)
    
    for t in a:
        print(t[0], len(list(set(t[1]))), sep=" ")
    opensource(0, inp[j:])

opensource(0, sys.stdin.readlines())

