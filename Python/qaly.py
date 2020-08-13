from os import sys
def qaly():
    n = int(sys.stdin.readline())
    ans = 0.0

    for i in range(1, n + 1):
        inp = sys.stdin.readline().split()
        ans += float(inp[0]) * float(inp[1])

    print(ans)
    return

qaly()
