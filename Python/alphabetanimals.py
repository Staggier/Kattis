import sys

def alphabetanimals():
    inp = sys.stdin.readlines()
    last, lst = inp[0], inp[2:]

    b = False
    t = []

    for name in lst:
        if last[-2] == name[0]:
            b = True
            t.append(name)

    if not b:
        return '?'

    for name1 in t:
        b = False
        for name2 in lst:
            if name1 == name2:
                continue
            if name1[-2] == name2[0]:
                b = True
                break
        if not b:
            return name1[:-1] + '!'
    return t[0][:-1]

print(alphabetanimals())
