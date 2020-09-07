from os import sys

def avion():
    ans = ""
    c = 1
    for line in sys.stdin.readlines():
        lst = line.split('-')
        for s in lst:
            if "FBI" in s:
                ans += " " + str(c)
                break
        c += 1
    print(ans[1:] if ans != "" else "HE GOT AWAY!")
    return

avion()
