def boatparts():
    n, k = [int(x) for x in input().split()]

    lst = []
    result = 0
    for i in range(k):
        s = input()
        if s not in lst:
            lst.append(s)
            result = i + 1

    if len(lst) != n:
        return "paradox avoided"
    else:
        return result

print(boatparts())
