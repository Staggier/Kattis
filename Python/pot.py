from os import sys

def pot():
    n, ans = int(sys.stdin.readline()), 0

    for i in range(1, n + 1):
        s = sys.stdin.readline()
        m, k = s[:len(s) - 2], s[len(s) - 2:]
        ans += int(m) ** int(k)
    print(ans)
    return

pot()
