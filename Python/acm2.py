def acm2():
    n, i = list(map(int, input().split()))
    lst = list(map(int, input().split()))

    t = lst[i]
    del lst[i]

    lst.sort()

    i, c, time, ans = 0, 1, 300 - t, t
    while time >= 0 and i < len(lst):
        time -= lst[i]
        if time >= 0:
            c += 1
            ans += 300 - time
        i += 1          

    return str(c) + " " + str(ans) if time >= 0 or ans != t else "0 0"

print(acm2())
