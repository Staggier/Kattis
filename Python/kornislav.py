def kornislav():
    lst = list(map(int, input().split()))
    lst.sort()
    print(min(lst[:2]) * min(lst[2:]))
    return

kornislav()
